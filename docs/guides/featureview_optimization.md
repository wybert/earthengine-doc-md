 
#  FeatureView Optimization
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Max features per tile](https://developers.google.com/earth-engine/guides/featureview_optimization#max_features_per_tile)
  * [Thinning ranking](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_ranking)
  * [Thinning strategy](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_strategy)
  * [Z-order ranking](https://developers.google.com/earth-engine/guides/featureview_optimization#z-order_ranking)


When [exporting a `FeatureCollection` as a `FeatureView`](https://developers.google.com/earth-engine/guides/featureview_overview#creating_a_featureview) asset, you can set parameters that prioritize which features are rendered at a given zoom level (thinning) and how overlapping features are ordered (z-order). These settings affect the speed and display characteristics of `FeatureView` objects. The following sections describe the optimization parameters and demonstrate their impact using conceptual diagrams where map tiles are delineated by dashed lines, visible features are solid-line polygons, and discarded (thinned) features are polygons with dashed lines and no fill.
The following code block is an example of a `FeatureCollection` to `FeatureView` export that highlights the optimization parameters described in this page.
```
Export.table.toFeatureView({
collection:fooFc,
assetId:'foo-featureview-demo',
description:'foo-featureview-demo',
**maxFeaturesPerTile:1500,
thinningStrategy:'HIGHER_DENSITY',
thinningRanking:['my-property DESC'],
zOrderRanking:['my-property DESC']**
});

```
**Note:** the number of features per tile and the `maxFeaturesPerTile` values in the conceptual diagrams throughout this page are for demonstration purposes only. In practice, the number of features will likely be much greater.
## Max features per tile
The max features per tile (`maxFeaturesPerTile`) parameter defines the maximum number of features to be rendered on a single map tile. This value is an upper bound, and may be significantly lower depending on the [thinning strategy](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_strategy). This value can be set to anything between 1 and 2000. Higher values show more features per tile, but tiles take longer to load.
Notice in the following table that as the `maxFeaturesPerTile` parameter value decreases, so does the number of features intersecting each map tile. A tile may have less than the max, but no more.
All features (for reference) |  `maxFeaturesPerTile: 5` Shows no more than 5 features per tile. |  `maxFeaturesPerTile: 2` Shows no more than 2 features per tile.  
---|---|---  
![](https://developers.google.com/static/earth-engine/images/FeatureView_MFPT8.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_MFPT5.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_MFPT2.svg)  
**Note:** Tile load time depends on the number of features, [style rules](https://developers.google.com/earth-engine/guides/featureview_styling), geometry types, and geometry complexity. If timeouts occur or you want to decrease load time, start by decreasing `maxFeaturesPerTile`. You may also simplify the geometries of features before exporting a `FeatureView` asset and/or simplify the style rules when displaying a `FeatureView`, but these solutions are less direct and may be less effective.
## Thinning ranking
The thinning ranking (`thinningRanking`) parameter controls how data are prioritized for thinning based on geometry type, feature size, and feature property values. It accepts a set of rules that inform the thinning algorithm about which features to thin out ahead of others when [`maxFeaturesPerTile`](https://developers.google.com/earth-engine/guides/featureview_optimization#max_features_per_tile) is reached. Each rule includes a feature property followed by sorting direction (ascending/`ASC` or descending/`DESC`); there can be one or more rules. In addition to traditional feature properties, there are two special properties that can be used to prioritize thinning: `.geometryType` and `.minZoomLevel`.
  * **`.geometryType`**– characterizes features as points, lines, or polygons. These geometry types are respectively quantified as small, medium, and large for the purpose of sorting.
  * **`.minZoomLevel`**– the lowest map zoom level at which a feature may render to a tile. Zoom levels below this value will not display the feature, zoom levels greater than or equal to this value may display the feature. Recall that low zoom levels represent a larger geographic region per map tile than higher zoom levels. Point features are assigned a value of 0 (visible at all zoom levels). Line and polygon geometries are assigned values based on their bounds (lines) or area (polygons): large features have lower`.minZoomLevel` values than smaller features.


Thinning ranking rules can be provided as either a string or a list of strings where a property name and the desired sorting direction are separated by a space:
```
// String input format for setting thinning ranking based on 3 rules.
'my-property DESC, .geometryType ASC, .minZoomLevel ASC'

// List of strings input format for setting thinning ranking based on 3 rules.
['my-property DESC','.geometryType ASC','.minZoomLevel ASC']

```

The rules above direct the thinning algorithm to prioritize features with a larger "my-property" attribute (thin features with a smaller "my-property" value first), prioritize features with a smaller geometry type (for example, thin out polygons before lines and lines before points), and prioritize features with a smaller minimum zoom level (points over large polygons over smaller polygons).
The following table illustrates how changing the `thinningRanking` rule for a `size` property affects which features are drawn. The total number of features per tile ("All features" column) is greater than 5, so thinning is applied to limit the features that are drawn (`thinningRanking: 5` column). In the first row, the features are sorted by `size` from greatest to least, meaning that larger features take priority over smaller features (features are drawn in descending order by size until `maxFeaturesPerTile` is reached). In the second row, the features are sorted by ascending size, so the smallest features are drawn first, in order of size, until `maxFeaturesPerTile` is reached.
`thinningRanking` | All features (for reference) | `maxFeaturesPerTile: 5`  
---|---|---  
`'size DESC'` Prioritize features with larger `size` (thin out features with smaller `size` first).  | ![](https://developers.google.com/static/earth-engine/images/FeatureView_EmptyThinRank.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ThinRankSizeDESCMFPT5.svg)  
`'size ASC'` Prioritize features with smaller `size` (thin out features with larger `size` first)  | ![](https://developers.google.com/static/earth-engine/images/FeatureView_EmptyThinRank.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ThinRankSizeASCMFPT5.svg)  
## Thinning strategy
The thinning strategy parameter (`thinningStrategy`) is used alongside [thinning ranking](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_ranking) (`thinningRanking`) to thin out data at export time to improve rendering performance. There are two strategies supported: `HIGHER_DENSITY` and `GLOBALLY_CONSISTENT`. When thinning at a particular zoom level, a higher density thinning strategy means that each tile may get as close as possible to the [`maxFeaturesPerTile`](https://developers.google.com/earth-engine/guides/featureview_optimization#max_features_per_tile) limit without regard for the rank of features in other tiles. The globally consistent thinning strategy means that if a feature is removed by thinning from any tile, then all features with equal or lower [thinning rank](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_ranking) will be removed from all tiles, regardless of whether a tile requires thinning (exceeds `maxFeaturesPerTile` limit). Use the `HIGHER_DENSITY` strategy to optimize for feature density and use the `GLOBALLY_CONSISTENT` strategy to optimize for consistent inter-tile representation of feature rank.
The following table demonstrates how changing `thinningStrategy` affects thinning. In this example, the data are thinned using the shape/color of the points. Blue circles, green squares, and red triangles have respective [thinning ranks](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_ranking) from best to worst. For each `thinningStrategy` (`HIGHER_DENSITY` and `GLOBALLY_CONSISTENT`), there are three different values for `maxFeaturesPerTile` specified: a number large enough to show all features, 10 features, and 9 features.
With `HIGHER_DENSITY` and 10 `maxFeaturesPerTile`, 6 red triangles (lowest priority in thinning rank) are thinned out of the top-left tile, and 1 red triangle is thinned out of the bottom-left tile. With `HIGHER_DENSITY` and 9 `maxFeaturesPerTile`, 7 red triangles are thinned out of the top-left tile, and a red triangle and green square are thinned out of the bottom-left tile. In these examples, each tile is thinned independently, without consideration of the thinning rank of features in neighboring tiles. Depending on the characteristics of the data, this thinning strategy can lead to adjacent map tiles appearing distinctly different from one another, but maximizes the number of features drawn.
Recall that `GLOBALLY_CONSISTENT` thinning means that if a feature is removed by thinning from any tile, then all other features with equal or worse [`thinningRank`](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_ranking) will also be removed. With `maxFeaturesPerTile` set to 10, the red triangles don't show up on any tile because a red triangle is thinned out in the top-left and bottom-left tiles. With `maxFeaturesPerTile` set to 9, the green squares similarly don't show up on any tile because a green square is thinned out in the bottom-left tile. This thinning strategy is less likely to produce the distinct tile appearance that the `HIGHER_DENSITY` strategy can, but has the potential to thin tiles to a number of features far below the `maxFeaturesPerTile` limit.
`thinningStrategy` | All Features (for reference) | maxFeaturesPerTile: 10 | maxFeaturesPerTile: 9  
---|---|---|---  
`'HIGHER_DENSITY'` Less aggressive thinning. Maintains high feature density through intra-tile thinning. | ![](https://developers.google.com/static/earth-engine/images/FeatureView_EmptyThinStrat.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ThinStratHDMFTP10.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ThinStratHDMFTP9.svg)  
`'GLOBALLY_CONSISTENT'` More aggressive thinning. Maintains globally consistent minimum thinning rank through inter-tile thinning. | ![](https://developers.google.com/static/earth-engine/images/FeatureView_EmptyThinStrat.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ThinStratGCMFTP10.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ThinStratGCMFTP9.svg)  
## Z-order ranking
The z-order ranking (`zOrderRanking`) parameter controls the ordering of overlapping features. It accepts a set of rules that define what features should appear under/over others when they overlap. The rule logic and format for setting feature order is the same as [thinning ranking](https://developers.google.com/earth-engine/guides/featureview_optimization#thinning_ranking), please see that section for more details.
Z-order ranking rules can be provided as either a string or a list of strings where a property name and the desired sorting direction are separated by a space:
```
// String input format for setting z-order ranking based on 3 rules.
'my-property DESC, .geometryType ASC, .minZoomLevel ASC'

// List of strings input format for setting z-order ranking based on 3 rules.
['my-property DESC','.geometryType ASC','.minZoomLevel ASC']

```

The rules above specify that features with a larger "my-property" value should appear under features with a smaller value, features with a smaller geometry type should appear under features with a larger geometry type (for example, points under lines and lines under polygons), and features with a smaller min zoom level (larger features) should appear under features with a larger min zoom level (smaller features).
The following table demonstrates how changing the `zOrderRanking` rule for a "size" property affects which features appear in front of others when they overlap. In the first row, features are sorted by size in descending order, meaning that larger sized features should appear under smaller features (larger features are drawn first). Conversely, in the second row, features are sorted by size in ascending order, meaning that smaller sized features should appear under larger features (smaller features are drawn first).
`zOrderRanking: 'size DESC'` Features with smaller `size` appear on top of features with larger `size`. |  `zOrderRanking: 'size ASC'` Features with larger `size` appear on top of features with smaller `size`.  
---|---  
![](https://developers.google.com/static/earth-engine/images/FeatureView_ZOrderRankSizeDESC.svg) | ![](https://developers.google.com/static/earth-engine/images/FeatureView_ZOrderRankSizeASC.svg)  
