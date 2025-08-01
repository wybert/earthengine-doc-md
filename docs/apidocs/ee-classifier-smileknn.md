 
#  ee.Classifier.smileKNN
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences. 
Creates an empty k-NN classifier.
The k-nearest neighbor algorithm (k-NN) is a method for classifying objects by a majority vote of its neighbors, with the object being assigned to the class most common amongst its k nearest neighbors (k is a positive integer, typically small, typically odd).
Usage | Returns  
---|---  
`ee.Classifier.smileKNN(_k_, _searchMethod_, _metric_)`|  Classifier  
Argument | Type | Details  
---|---|---  
`k` | Integer, default: 1 | The number of neighbors for classification.  
`searchMethod` | String, default: "AUTO" | Search method. The following are valid [AUTO, LINEAR_SEARCH, KD_TREE, COVER_TREE]. AUTO will choose between KD_TREE and COVER_TREE depending on the dimension count. Results may vary between the different search methods for distance ties and probability values. Since performance and results may vary consult with SMILE's documentation and other literature.  
`metric` | String, default: "EUCLIDEAN" | The distance metric to use. NOTE: KD_TREE (and AUTO for low dimensions) will not use the metric selected. Options are: 'EUCLIDEAN' - Euclidean distance. 'MAHALANOBIS' - Mahalanobis distance. 'MANHATTAN' - Manhattan distance. 'BRAYCURTIS' - Bray-Curtis distance.  
## Examples
### Code Editor (JavaScript)
```
// Cloud masking for Landsat 8.
functionmaskL8sr(image){
varqaMask=image.select('QA_PIXEL').bitwiseAnd(parseInt('11111',2)).eq(0);
varsaturationMask=image.select('QA_RADSAT').eq(0);

// Apply the scaling factors to the appropriate bands.
varopticalBands=image.select('SR_B.').multiply(0.0000275).add(-0.2);
varthermalBands=image.select('ST_B.*').multiply(0.00341802).add(149.0);

// Replace the original bands with the scaled ones and apply the masks.
returnimage.addBands(opticalBands,null,true)
.addBands(thermalBands,null,true)
.updateMask(qaMask)
.updateMask(saturationMask);
}

// Map the function over one year of data.
varcollection=ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
.filterDate('2020-01-01','2021-01-01')
.map(maskL8sr);

// Make a median composite.
varcomposite=collection.median();

// Demonstration labels.
varlabels=ee.FeatureCollection('projects/google/demo_landcover_labels')

// Use these bands for classification.
varbands=['SR_B2','SR_B3','SR_B4','SR_B5','SR_B6','SR_B7'];
// The name of the property on the points storing the class label.
varclassProperty='landcover';

// Sample the composite to generate training data.  Note that the
// class label is stored in the 'landcover' property.
vartraining=composite.select(bands).sampleRegions(
{collection:labels,properties:[classProperty],scale:30});

// Train a kNN classifier.
varclassifier=ee.Classifier.smileKNN(5).train({
features:training,
classProperty:classProperty,
});

// Classify the composite.
varclassified=composite.classify(classifier);
Map.setCenter(-122.184,37.796,12);
Map.addLayer(classified,{min:0,max:2,palette:['red','green','blue']});
```

Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```

### Colab (Python)
```
# Cloud masking for Landsat 8.
defmask_l8_sr(image):
  qa_mask = image.select('QA_PIXEL').bitwiseAnd(int('11111', 2)).eq(0)
  saturation_mask = image.select('QA_RADSAT').eq(0)

  # Apply the scaling factors to the appropriate bands.
  optical_bands = image.select('SR_B.').multiply(0.0000275).add(-0.2)
  thermal_bands = image.select('ST_B.*').multiply(0.00341802).add(149.0)

  # Replace the original bands with the scaled ones and apply the masks.
  return (
      image.addBands(optical_bands, None, True)
      .addBands(thermal_bands, None, True)
      .updateMask(qa_mask)
      .updateMask(saturation_mask)
  )


# Map the function over one year of data.
collection = (
    ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    .filterDate('2020-01-01', '2021-01-01')
    .map(mask_l8_sr)
)

# Make a median composite.
composite = collection.median()

# Demonstration labels.
labels = ee.FeatureCollection('projects/google/demo_landcover_labels')

# Use these bands for classification.
bands = ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7']
# The name of the property on the points storing the class label.
class_property = 'landcover'

# Sample the composite to generate training data.  Note that the
# class label is stored in the 'landcover' property.
training = composite.select(bands).sampleRegions(
    collection=labels, properties=[class_property], scale=30
)

# Train a kNN classifier.
classifier = ee.Classifier.smileKNN(5).train(
    features=training, classProperty=class_property
)

# Classify the composite.
classified = composite.classify(classifier)

m = geemap.Map()
m.set_center(-122.184, 37.796, 12)
m.add_layer(
    classified, {'min': 0, 'max': 2, 'palette': ['red', 'green', 'blue']}
)
m
```

