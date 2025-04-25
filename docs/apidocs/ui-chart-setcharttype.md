 
#  ui.Chart.setChartType 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ui-chart-setcharttype#examples)


Sets the chartType of this chart. 
Returns this chart.
Usage| Returns  
---|---  
`Chart.setChartType(chartType)`| ui.Chart  
Argument| Type| Details  
---|---|---  
this: `ui.chart`| ui.Chart| The ui.Chart instance.  
`chartType`| String| The chart type; e.g 'ScatterChart', 'LineChart', and 'ColumnChart'. For the complete list of charts, see: https://developers.google.com/chart/interactive/docs/gallery  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ui-chart-setcharttype#code-editor-javascript-sample) More
```
// A data table of population for selected states.
vardataTable=[
[{role:'domain',label:'State'},{role:'data',label:'Population'}],
['CA',37253956],
['NY',19378102],
['IL',12830632],
['MI',9883640],
['OR',3831074],
];
// Chart the data using accepted chart types.
print('Scatter chart',ui.Chart(dataTable).setChartType('ScatterChart'));
print('Line chart',ui.Chart(dataTable).setChartType('LineChart'));
print('Column chart',ui.Chart(dataTable).setChartType('ColumnChart'));
print('Bar chart',ui.Chart(dataTable).setChartType('BarChart'));
print('Pie chart',ui.Chart(dataTable).setChartType('PieChart'));
print('Area chart',ui.Chart(dataTable).setChartType('AreaChart'));
print('Table',ui.Chart(dataTable).setChartType('Table'));
```

Was this helpful?
