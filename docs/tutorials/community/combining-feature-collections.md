 
#  Combining FeatureCollections 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
  * On this page
  * [Create two ee.FeatureCollection objects](https://developers.google.com/earth-engine/tutorials/community/combining-feature-collections#create_two_eefeaturecollection_objects)
  * [Combine the ee.FeatureCollection objects](https://developers.google.com/earth-engine/tutorials/community/combining-feature-collections#combine_the_eefeaturecollection_objects)
  * [Visualize the Results](https://developers.google.com/earth-engine/tutorials/community/combining-feature-collections#visualize_the_results)
  * [Bonus Points](https://developers.google.com/earth-engine/tutorials/community/combining-feature-collections#bonus_points)


[ Edit on GitHub ](https://github.com/google/earthengine-community/edit/master/tutorials/combining-feature-collections/index.md)
[ Report issue ](https://github.com/google/earthengine-community/issues/new?title=Issue%20with%20tutorials/combining-feature-collections/index.md&body=Issue%20Description)
[ Page history ](https://github.com/google/earthengine-community/commits/master/tutorials/combining-feature-collections/index.md)
Author(s): [ sabrinaszeto ](https://github.com/sabrinaszeto)
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
This basic tutorial shows how users can combine two `ee.FeatureCollection`s into a new `ee.FeatureCollection`. 
## Create two `ee.FeatureCollection` objects
Let's begin by generating two sets of random points within the boundary of Utah state in the USA. First, define the boundary of Utah as a geometry.
```
varutahGeometry=ee.Geometry.Polygon([
[-114.05,37],
[-109.05,37],
[-109.05,41],
[-111.05,41],
[-111.05,42],
[-114.05,42]
]);

```

Then, generate two sets of different random points containing 25 points each. We ensure that the points are different by using a different seed, namely 12 and 1, to generate each set.
```
varnewFeatures=ee.FeatureCollection.randomPoints(utahGeometry,25,12);
varmoreNewFeatures=ee.FeatureCollection.randomPoints(utahGeometry,25,1);

```

## Combine the `ee.FeatureCollection` objects
Next, create a new `ee.FeatureCollection` by merging `newFeatures` and `moreNewFeatures`.
```
varcombinedFeatureCollection=newFeatures.merge(moreNewFeatures);

```

## Visualize the Results
Let's add all the `ee.FeatureCollection`s to the map. First, we set the center of the map to the coordinates defined below and set the zoom level to 6.
```
Map.setCenter(-111.445,39.251,6);

```

Now, we add all the layers, specifying the layer labels as text strings (for example, `'New Features'`) and colors to display each layer in. We will also print the results.
```
Map.addLayer(newFeatures,{},'New Features');
Map.addLayer(moreNewFeatures,{color:'red'},'More New Features');
Map.addLayer(combinedFeatureCollection,{color:'yellow'},'Combined FeatureCollection');
print(newFeatures,moreNewFeatures,combinedFeatureCollection);

```

## Bonus Points
  * What happens if you change the zoom level in `Map.setCenter` to 3 or to 12?
  * Try changing the layer label of `'More New Features'` to `'Red Points'`. Run the script again to see if it worked.


