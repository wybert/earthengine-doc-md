 
#  Chart Overview 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [DataTable charts](https://developers.google.com/earth-engine/guides/charts_overview#datatable_charts)
  * [Earth Engine object charts](https://developers.google.com/earth-engine/guides/charts_overview#earth_engine_object_charts)
  * [Chart types](https://developers.google.com/earth-engine/guides/charts_overview#chart_types)
  * [Display and download](https://developers.google.com/earth-engine/guides/charts_overview#display_and_download)
  * [Interactivity](https://developers.google.com/earth-engine/guides/charts_overview#interactivity)
  * [Styling](https://developers.google.com/earth-engine/guides/charts_overview#styling)
  * [Limitations](https://developers.google.com/earth-engine/guides/charts_overview#limitations)


The Earth Engine JavaScript [Code Editor](https://developers.google.com/earth-engine/guides/playground) seamlessly integrates with [Google Charts](https://developers.google.com/chart/interactive/docs/gallery) for convenient tabular data visualization via `ui.Chart` functions. Charts can be displayed interactively in the Code Editor console, `ui.Panel` widgets, and in stand-alone browser tabs.
**Caution:** the `ui.Chart` widget is available for the JavaScript Code Editor API only.
## `DataTable` charts
Earth Engine uses the [Google Visualization API](https://developers.google.com/chart/interactive/docs/reference) to support charting. The API accepts a `DataTable`, which is a 2-D table where rows are observations and columns are observation attributes. All charts in Earth Engine are derived from a `DataTable`; the `ui.Chart` widget allows you to supply a `DataTable` directly. It affords the greatest opportunity for chart customization, but may be less convenient than methods for charting specific Earth Engine objects (see the following section). Learn more about creating charts from a `DataTable`:
  * [**`DataTable`charting**](https://developers.google.com/earth-engine/guides/charts_datatable)


## Earth Engine object charts
The `ui.Chart` widget provides helper methods to construct a `DataTable` and render charts from `Image`, `ImageCollection` `Feature`, `FeatureCollection`, `Array`, and `List` objects. Each function accepts a specific data type and includes methods for reducing the data to tabular format in a variety of arrangements that dictate data assignment to chart series and axes.
Visit the following links to learn how to generate a chart for each data type:
  * [**`Feature`charting**](https://developers.google.com/earth-engine/guides/charts_feature)
  * [**`FeatureCollection`charting**](https://developers.google.com/earth-engine/guides/charts_feature)
  * [**`Image`charting**](https://developers.google.com/earth-engine/guides/charts_image)
  * [**`ImageCollection`charting**](https://developers.google.com/earth-engine/guides/charts_image_collection)
  * [**`Array`charting**](https://developers.google.com/earth-engine/guides/charts_array)
  * [**`List`charting**](https://developers.google.com/earth-engine/guides/charts_array)


## Chart types
A variety of chart types can be produced; for example: scatter, line, bar, pie, and histogram. Specifically, any chart type that is available in the Google Charts [corechart](https://developers.google.com/chart/interactive/docs/basic_load_libs#basic-library-loading) package can be generated. Use the `ui.Chart.setChartType()` method to set chart type. Each page linked to in the [Earth Engine object charts](https://developers.google.com/earth-engine/guides/charts_overview#earth_engine_object_charts) and [`DataTable` charts](https://developers.google.com/earth-engine/guides/charts_overview#datatable_charts) sections include examples for generating several chart types.
Use the following strings as input to the `ui.Chart.setChartType()` method:
```
'ScatterChart'
'LineChart'
'ColumnChart'
'BarChart'
'PieChart'
'AreaChart'

```

Here is an example:
```
vardata=ee.List([0,1,2,3,4,5]);
varchart=ui.Chart.array.values(data,0,data)
.setChartType('ColumnChart');
print(chart);

```

## Display and download
`ui.Chart` widgets can be displayed three ways:
  * In the [Code Editor console](https://developers.google.com/earth-engine/guides/playground#console-tab)

```
vardata=ee.List([0,1,2,3,4,5]);
varchart=ui.Chart.array.values(data,0,data);
print(chart);

```

  * In a [`ui.Panel`](https://developers.google.com/earth-engine/guides/ui_panels#panels) widget

```
vardata=ee.List([0,1,2,3,4,5]);
varchart=ui.Chart.array.values(data,0,data);
varchartPanel=ui.Panel(chart);
Map.add(chartPanel);

```

  * In a separate browser tab; click the pop-out icon (open_in_new) in the upper-right corner of a displayed `ui.Chart` widget. The new page provides a full-window display and options to **download the chart** as a graphic (PNG or SVG) or a CSV file of the underlying data.


## Interactivity
Charts are interactive by default. Hover over points, lines, bars, etc. to see respective x, y, and series values. Axis zooming and panning are optionally permitted by [activating a chart's "explorer" functionality](https://developers.google.com/earth-engine/guides/charts_style#zoom_and_pan_chart_axes).
## Styling
Google Charts are highly customizable via styling properties. Use the `ui.Chart.setOptions()` method to set chart style properties. See the [Chart Styling](https://developers.google.com/earth-engine/guides/charts_style) guide for full details.
## Limitations
`ui.Chart` functions will only render 5,000 features. If your `FeatureCollection`, `ImageCollection`, `Array` or `List` has more elements, consider ways you might limit the data. If you have a long time series with a high cadence rate, try using a shorter time period, temporal sampling, or generate temporal composites. If the issue is spatial, try using a random subset. If you are working with pixels in a list or array, try using a slightly larger scale or smaller region.
Long-running computations can fail to generate a chart because of interactive response limits of the Code Editor. If your chart request times out, try [exporting](https://developers.google.com/earth-engine/guides/exporting) intermediate steps of your analysis and regenerating the chart from the exported assets.
