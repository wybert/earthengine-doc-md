 
#  Detecting Changes in Sentinel-1 Imagery (Part 3)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Run me first](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#run_me_first)
  * [Datasets and Python modules](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#datasets_and_python_modules)
  * [Part 3. Multitemporal change detection](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#part_3_multitemporal_change_detection)
    * [A time series](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#a_time_series)
    * [An omnibus test for change](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#an_omnibus_test_for_change)
    * [A question of scale](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#a_question_of_scale)
    * [A sequential omnibus test](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#a_sequential_omnibus_test)
    * [Outlook](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3#outlook)


Author(s): [ mortcanty ](https://github.com/mortcanty)
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/tutorials/detecting-changes-in-sentinel-1-imagery-pt-3/index.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/tutorials/detecting-changes-in-sentinel-1-imagery-pt-3/index.ipynb)  
---|---  
### Run me first
Run the following cell to initialize the API. The output will contain instructions on how to grant this notebook access to Earth Engine using your account.
```
importee
# Trigger the authentication flow.
ee.Authenticate()
# Initialize the library.
ee.Initialize(project='my-project')

```

### Datasets and Python modules
One [dataset](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S1_GRD) will be used in the tutorial:
  * COPERNICUS/S1_GRD_FLOAT 
    * Sentinel-1 ground range detected images


The following cell imports some python modules which we will be using as we go along and enables inline graphics.
```
importmatplotlib.pyplotasplt
importnumpyasnp
fromscipy.statsimport norm, gamma, f, chi2
importIPython.displayasdisp
%matplotlib inline

```

This cell carries over the chi square cumulative distribution function and the determinant of a Sentinel-1 image from [Part 2](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2).
```
defchi2cdf(chi2, df):
"""Calculates Chi square cumulative distribution function for
    df degrees of freedom using the built-in incomplete gamma
    function gammainc().
  """
  return ee.Image(chi2.divide(2)).gammainc(ee.Number(df).divide(2))
defdet(im):
"""Calculates determinant of 2x2 diagonal covariance matrix."""
  return im.expression('b(0)*b(1)')

```

And to make use of interactive graphics, we import the _folium_ package:
```
importfolium
defadd_ee_layer(self, ee_image_object, vis_params, name):
"""Adds Earth Engine layers to a folium map."""
  map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
  folium.raster_layers.TileLayer(
    tiles = map_id_dict['tile_fetcher'].url_format,
    attr = 'Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
    name = name,
    overlay = True,
    control = True).add_to(self)
# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer

```

## Part 3. Multitemporal change detection
Continuing from [Part 2](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2), in which we discussed bitemporal change detection with Sentinel-1 images, we turn our attention to the multitemporal case. To get started, we obviously need ...
### A time series
Here is a fairly interesting one: a region in South Yorkshire, England where, in November 2019, extensive flooding occurred along the River Don just north of the city of Doncaster.
```
geoJSON = {
 "type": "FeatureCollection",
 "features": [
  {
   "type": "Feature",
   "properties": {},
   "geometry": {
    "type": "Polygon",
    "coordinates": [
     [
      [
       -1.2998199462890625,
       53.48028242228504
      ],
      [
       -0.841827392578125,
       53.48028242228504
      ],
      [
       -0.841827392578125,
       53.6958933974518
      ],
      [
       -1.2998199462890625,
       53.6958933974518
      ],
      [
       -1.2998199462890625,
       53.48028242228504
      ]
     ]
    ]
   }
  }
 ]
}
coords = geoJSON['features'][0]['geometry']['coordinates']
aoi = ee.Geometry.Polygon(coords)

```

The image collection below covers the months of September, 2019 through January, 2020 at 6-day intervals:
```
im_coll = (ee.ImageCollection('COPERNICUS/S1_GRD_FLOAT')
      .filterBounds(aoi)
      .filterDate(ee.Date('2019-09-01'),ee.Date('2020-01-31'))
      .filter(ee.Filter.eq('orbitProperties_pass', 'DESCENDING'))
      .filter(ee.Filter.eq('relativeOrbitNumber_start', 154))
      .map(lambda img: img.set('date', ee.Date(img.date()).format('YYYYMMdd')))
      .sort('date'))
timestamplist = (im_coll.aggregate_array('date')
         .map(lambda d: ee.String('T').cat(ee.String(d)))
         .getInfo())
timestamplist

```
```
['T20190902',
 'T20190908',
 'T20190914',
 'T20190920',
 'T20190926',
 'T20191002',
 'T20191008',
 'T20191014',
 'T20191020',
 'T20191026',
 'T20191101',
 'T20191107',
 'T20191113',
 'T20191119',
 'T20191125',
 'T20191201',
 'T20191207',
 'T20191213',
 'T20191219',
 'T20191225',
 'T20191231',
 'T20200106',
 'T20200112',
 'T20200118',
 'T20200124',
 'T20200130']

```

It will turn out to be convenient to work with a list rather than a collection, so we'll convert the collection to a list and, while we're at it, clip the images to our AOI:
```
defclip_img(img):
"""Clips a list of images."""
  return ee.Image(img).clip(aoi)
im_list = im_coll.toList(im_coll.size())
im_list = ee.List(im_list.map(clip_img))
im_list.length().getInfo()

```
```
26

```

Here is an RGB composite of the VV bands for three images in early November, after conversion to decibels. Note that some changes, especially those due to flooding, already show up in this representation as colored pixels.
```
defselectvv(current):
  return ee.Image(current).select('VV')
vv_list = im_list.map(selectvv)
location = aoi.centroid().coordinates().getInfo()[::-1]
mp = folium.Map(location=location, zoom_start=11)
rgb_images = (ee.Image.rgb(vv_list.get(10), vv_list.get(11), vv_list.get(12))
       .log10().multiply(10))
mp.add_ee_layer(rgb_images, {'min': -20,'max': 0}, 'rgb composite')
mp.add_child(folium.LayerControl())

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_QwJv_Ib8MFKH_0.png)
Now we have a series of 26 SAR images and, for whatever reason, would like to know where and when changes have taken place. A first reaction might be:
_What's the problem? Just apply the bitemporal method we developed in Part 2 to each of the 25 time intervals._
Well, one problem is the rate of false positives. If the bitemporal tests are statistically independent, then the probability of **not** getting a false positive over a series of length is the product of not getting one in each of the intervals, i.e., and the overall first kind error probability is its complement:
For our case, even with a small value of , this gives a whopping 22.2% false positive rate:
```
alpha = 0.01
1-(1-alpha)**25

```
```
0.22217864060085335

```

Actually things are a bit worse. The bitemporal tests are manifestly not independent because consecutive tests have one image in common. The best one can say in this situation is
or for and . If we wish to set a false positive rate of at most, say, 1% for the entire series, then each bitemporal test must have a significance level of and a correspondingly large false negative rate . In other words many significant changes may be missed.
How to proceed? Perhaps by being a bit less ambitious at first and asking the simpler question: _Were there any changes at all over the interval?_ If the answer is affirmative, we can worry about how many there were and when they occurred later. Let's formulate this question as ...
### An omnibus test for change
We'll start again with the easier single polarization case. For the series of _VV_ intensity images acquired at times , our null hypothesis is that, at a given pixel position, there has been no change in the signal strengths over the entire period, i.e.,
The alternative hypothesis is that there was at least one change (and possibly many) over the interval. For the more mathematically inclined this can be written succinctly as
which says: there exist indices for which is not equal to .
Again, the likelihood functions are products of gamma distributions:
and is maximized for while is maximized for . So with a bit of simple algebra our likelihood ratio test statistic is
and is called an _omnibus test statistic_. Note that, for , we get the bitemporal LRT given by [Eq. (2.10)](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2#the_likelihood_ratio_test).
We can't expect to find an analytical expression for the probability distribution of this LRT statistic, so we will again invoke Wilks' Theorem and work with
According to Wilks, it should be approximately chi square distributed with degrees of freedom under . (Why?)
The input cell below evaluates the test statistic Eq. (3.6) for a list of single polarization images. We prefer from now on to use as default the equivalent number of looks 4.4 that we discussed at the end of [Part 1](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-1#equivalent_number_of_looks) rather than the actual number of looks , in the hope of getting a better agreement.
```
defomnibus(im_list, m = 4.4):
"""Calculates the omnibus test statistic, monovariate case."""
  deflog(current):
    return ee.Image(current).log()
  im_list = ee.List(im_list)
  k = im_list.length()
  klogk = k.multiply(k.log())
  klogk = ee.Image.constant(klogk)
  sumlogs = ee.ImageCollection(im_list.map(log)).reduce(ee.Reducer.sum())
  logsum = ee.ImageCollection(im_list).reduce(ee.Reducer.sum()).log()
  return klogk.add(sumlogs).subtract(logsum.multiply(k)).multiply(-2*m)

```

Let's see if this test statistic does indeed follow the chi square distribution. First we define a small polygon _aoi_sub_ over the Thorne Moors (on the eastern side of the AOI) for which we hope there are few significant changes.
```
geoJSON = {
 "type": "FeatureCollection",
 "features": [
  {
   "type": "Feature",
   "properties": {},
   "geometry": {
    "type": "Polygon",
    "coordinates": [
     [
      [
       -0.9207916259765625,
       53.63649628489509
      ],
      [
       -0.9225082397460938,
       53.62550271303527
      ],
      [
       -0.8892059326171875,
       53.61022911107819
      ],
      [
       -0.8737564086914062,
       53.627538775780984
      ],
      [
       -0.9207916259765625,
       53.63649628489509
      ]
     ]
    ]
   }
  }
 ]
}
coords = geoJSON['features'][0]['geometry']['coordinates']
aoi_sub = ee.Geometry.Polygon(coords)
location = aoi.centroid().coordinates().getInfo()[::-1]
mp = folium.Map(location=location, zoom_start=11)
mp.add_ee_layer(rgb_images.clip(aoi_sub), {'min': -20, 'max': 0}, 'aoi_sub rgb composite')
mp.add_child(folium.LayerControl())

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_KXBkOhWQJd0__0.png)
Here is a comparison for pixels in _aoi_sub_ with the chi square distribution with degrees of freedom. We choose the first 10 images in the series () because we expect fewer changes in September/October than over the complete sequence , which extends into January.
```
k = 10
hist = (omnibus(vv_list.slice(0,k))
    .reduceRegion(ee.Reducer.fixedHistogram(0, 40, 200), geometry=aoi_sub, scale=10)
    .get('constant')
    .getInfo())
a = np.array(hist)
x = a[:,0]
y = a[:,1]/np.sum(a[:,1])
plt.plot(x, y, '.', label='data')
plt.plot(x, chi2.pdf(x, k-1)/5, '-r', label='chi square')
plt.legend()
plt.grid()
plt.show()

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_his4vdFXt8l2_0.png)
It appears that Wilks' Theorem is again a fairly good approximation. So why not generate a change map for the full series? The good news is that we now have the overall false positive probability under control. Here we set it to .
```
# The change map for alpha = 0.01.
k = 26; alpha = 0.01
p_value = ee.Image.constant(1).subtract(chi2cdf(omnibus(vv_list), k-1))
c_map = p_value.multiply(0).where(p_value.lt(alpha), 1)
# Make the no-change pixels transparent.
c_map = c_map.updateMask(c_map.gt(0))
# Overlay onto the folium map.
location = aoi.centroid().coordinates().getInfo()[::-1]
mp = folium.Map(location=location, zoom_start=11)
mp.add_ee_layer(c_map, {'min': 0,'max': 1, 'palette': ['black', 'red']}, 'change map')
mp.add_child(folium.LayerControl())

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_CL4N3GednWs9_0.png)
So plenty of changes, but hard to interpret considering the time span. Although we can see _where_ changes took place, we know neither _when_ they occurred nor their _multiplicity_. Also there is a matter that we have glossed over up until now, and that is ...
### A question of scale
The number of looks plays an important role in all of the formulae that we have discussed so far, and for the Sentinel-1 ground range detected imagery we first used and now the ENL . When we display a change map interactively, the [zoom factor determines the image pyramid level](https://developers.google.com/earth-engine/guides/scale) at which the GEE servers perform the required calculations and pass the result to the folium map client. If the calculations are not at the nominal scale of 10m then the number of looks is effectively larger than the ENL due to the averaging involved in constructing higher pyramid levels. The effect can be seen in the output cell above: the number of change pixels seems to decrease when we zoom out. There is no problem when we export our results to GEE assets, to Google Drive or to Cloud storage, since we can simply choose the correct nominal scale for export.
In order to see the changes correctly at all zoom levels, we can force GEE to work at the nominal scale by reprojecting before displaying on the map ([use with caution](https://developers.google.com/earth-engine/guides/projections#reprojecting)):
```
c_map_10m = c_map.reproject(c_map.projection().crs(), scale=10)
mp = folium.Map(location=location, zoom_start=11)
mp.add_ee_layer(c_map, {'min': 0, 'max': 1, 'palette': ['black', 'red']}, 'Change map')
mp.add_ee_layer(c_map_10m, {'min': 0, 'max': 1, 'palette': ['black', 'blue']}, 'Change map (10m)')
mp.add_child(folium.LayerControl())

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_shwzGq2tWMva_0.png)
You will notice in the output cell above that the calculation at nominal scale (the blue pixels) now takes considerably longer to complete. Also some red pixels are not completely covered by blue ones. Those changes are a spurious result of the falsified number of looks. Nevertheless for quick previewing purposes we might prefer to do without the reprojection.
### A sequential omnibus test
Recalling the last remark at the end of [Part 2](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2#oh_and_one_more_thing_), let's now guess the omnibus LRT for the dual polarization case. From Eq. (3.5), replacing , and , we get
This is in fact a special case of a more general omnibus test statistic
which holds for polarimetric covariance matrix images, for example for the full dual pol matrix [Eq. (1.5)](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-1#single_look_complex_slc_sar_measurements) or for full quad pol matrices (), but also for diagonal and matrices.
Which brings us to the **heart of this Tutorial**. We will now decompose Eq. (3.7) into a product of independent likelihood ratio tests which will enable us to determine when changes occurred at each pixel location. Then we'll code a complete multitemporal change detection algorithm on the GEE Python API.
#### Single polarization
Rather than make a formal derivation, we will illustrate the decomposition on a series of single polarization (VV) measurements. The omnibus test Eq. (3.5) for any change over the series from to is
If we accept the null hypothesis we're done and can move on to the next pixel (figuratively of course, since this stuff is all done in parallel). But suppose we have rejected the null hypothesis, i.e., there was a least one significant change. In order to find it (or them), we begin by testing the first of the four intervals. That's just the bitemporal test from Part 2, but let's call it rather than ,
Suppose we conclude no change, that is, . Now we don't do just another bitemporal test on the second interval. Instead we test the hypothesis
So the alternative hypothesis is: _There was no change in the first interval**and** there was a change in the second interval_. The LRT is easy to derive, but let's go through it anyway.
And, taking the ratio of the maximum likelihoods,
Not too hard to guess that, if we accept again, we go on to test
with LRT statistic
and so on to and the end of the time series.
Now for the cool part (try it out yourself):
So, generalizing to a series of length :
**The omnibus test statistic may be factored into the product of LRT's which test for homogeneity in the measured reflectance signal up to and including time , assuming homogeneity up to time :**
Moreover the test statistics are stochastically independent under . This can be shown analytically, see [Conradsen et al. (2016)](https://ieeexplore.ieee.org/document/7398022) or P. 405 in my [textbook](https://www.taylorfrancis.com/books/9780429464348), but we'll show it here empirically by sampling the test statistics in the region _aoi_sub_ and examining the correlation matrix.
```
defsample_vv_imgs(j):
"""Samples the test statistics Rj in the region aoi_sub."""
  j = ee.Number(j)
  # Get the factors in the expression for Rj.
  sj = vv_list.get(j.subtract(1))
  jfact = j.pow(j).divide(j.subtract(1).pow(j.subtract(1)))
  sumj = ee.ImageCollection(vv_list.slice(0, j)).reduce(ee.Reducer.sum())
  sumjm1 = ee.ImageCollection(vv_list.slice(0, j.subtract(1))).reduce(ee.Reducer.sum())
  # Put them together.
  Rj = sumjm1.pow(j.subtract(1)).multiply(sj).multiply(jfact).divide(sumj.pow(j)).pow(5)
  # Sample Rj.
  sample = (Rj.sample(region=aoi_sub, scale=10, numPixels=1000, seed=123)
       .aggregate_array('VV_sum'))
  return sample
# Sample the first few list indices.
samples = ee.List.sequence(2, 8).map(sample_vv_imgs)
# Calculate and display the correlation matrix.
np.set_printoptions(precision=2, suppress=True)
print(np.corrcoef(samples.getInfo()))

```
```
[[ 1.  0.  -0.01 -0.04 0.03 0.06 0.02]
 [ 0.  1.  0.04 -0.01 -0.02 0.02 0.02]
 [-0.01 0.04 1.  -0.04 0.02 -0.02 0.04]
 [-0.04 -0.01 -0.04 1.  -0.04 0.01 0.03]
 [ 0.03 -0.02 0.02 -0.04 1.  0.08 -0.01]
 [ 0.06 0.02 -0.02 0.01 0.08 1.  0. ]
 [ 0.02 0.02 0.04 0.03 -0.01 0.  1. ]]

```

The off-diagonal elements are mostly small. The not-so-small values can be attributed to sampling error or to the presence of some change pixels in the samples.
#### Dual polarization and an algorithm
With our substitution trick, we can now write down the sequential test for the dual polarization (bivariate) image time series. From Eq. (3.8) we get
And of course we have again to use Wilks' Theorem to get the _P_ values, so we work with
and
The statistic is approximately chi square distributed with two degrees of freedom. Similarly is approximately chi square distributed with degrees of freedom. Readers should satisfy themselves that these numbers are indeed the correct, taking into account that each measurement has two free parameters and , see [Eq. (2.13)](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2#bivariate_change_detection).
Now for the algorithm:
**The sequential omnibus change detection algorithm**
With a time series of SAR images ,
  1. Set .
  2. Set .
  3. Perform the omnibus test for any changes change over .
  4. If no significant changes are found, stop.
  5. Successively test series with until the first significant change is met for .
  6. Set and go to 2.


Table 3.1 |  |  |  |  |  |   
---|---|---|---|---|---|---  
|  |  |  |  |  |   
5 |  |  |  |  |  |   
4 |  |  |  |  |  |   
3 |  |  |  |  |  |   
2 |  |  |  |  |  |   
Thus if a change is found, the series is truncated up to the point of change and the testing procedure is repeated for the rest of the series. Take for example a series of images. (See Table 3.1 where, to avoid ambiguity, we add superscript to each test). Suppose there is one change in the second interval only. Then the test sequence is (the asterisk means is rejected)
If there are changes in the second and last intervals,
and if there are significant changes in all four intervals,
The approach taken in the coding of this algorithm is to pre-calculate _P_ values for all of the tests and then, in a second pass, to filter them to determine the points of change.
#### Pre-calculating the _P_ value array
The following code cell performs map operations on the indices and , returning an array of _P_ values for all possible LRT statistics. For example again for , the code calculates the _P_ values for each entry in Table 3.1 as a list of lists. Before calculating each row, the time series is sliced from to . The last entry in each row is simply the product of the other entries, 
The program actually operates on the logarithms of the test statistics, Equations (3.10).
```
deflog_det_sum(im_list, j):
"""Returns log of determinant of the sum of the first j images in im_list."""
  im_ist = ee.List(im_list)
  sumj = ee.ImageCollection(im_list.slice(0, j)).reduce(ee.Reducer.sum())
  return ee.Image(det(sumj)).log()
deflog_det(im_list, j):
"""Returns log of the determinant of the jth image in im_list."""
  im = ee.Image(ee.List(im_list).get(j.subtract(1)))
  return ee.Image(det(im)).log()
defpval(im_list, j, m=4.4):
"""Calculates -2logRj for im_list and returns P value and -2logRj."""
  im_list = ee.List(im_list)
  j = ee.Number(j)
  m2logRj = (log_det_sum(im_list, j.subtract(1))
        .multiply(j.subtract(1))
        .add(log_det(im_list, j))
        .add(ee.Number(2).multiply(j).multiply(j.log()))
        .subtract(ee.Number(2).multiply(j.subtract(1))
        .multiply(j.subtract(1).log()))
        .subtract(log_det_sum(im_list,j).multiply(j))
        .multiply(-2).multiply(m))
  pv = ee.Image.constant(1).subtract(chi2cdf(m2logRj, 2))
  return (pv, m2logRj)
defp_values(im_list):
"""Pre-calculates the P-value array for a list of images."""
  im_list = ee.List(im_list)
  k = im_list.length()
  defells_map(ell):
"""Arranges calculation of pval for combinations of k and j."""
    ell = ee.Number(ell)
    # Slice the series from k-l+1 to k (image indices start from 0).
    im_list_ell = im_list.slice(k.subtract(ell), k)
    defjs_map(j):
"""Applies pval calculation for combinations of k and j."""
      j = ee.Number(j)
      pv1, m2logRj1 = pval(im_list_ell, j)
      return ee.Feature(None, {'pv': pv1, 'm2logRj': m2logRj1})
    # Map over j=2,3,...,l.
    js = ee.List.sequence(2, ell)
    pv_m2logRj = ee.FeatureCollection(js.map(js_map))
    # Calculate m2logQl from collection of m2logRj images.
    m2logQl = ee.ImageCollection(pv_m2logRj.aggregate_array('m2logRj')).sum()
    pvQl = ee.Image.constant(1).subtract(chi2cdf(m2logQl, ell.subtract(1).multiply(2)))
    pvs = ee.List(pv_m2logRj.aggregate_array('pv')).add(pvQl)
    return pvs
  # Map over l = k to 2.
  ells = ee.List.sequence(k, 2, -1)
  pv_arr = ells.map(ells_map)
  # Return the P value array ell = k,...,2, j = 2,...,l.
  return pv_arr

```

#### Filtering the _P_ values
Table 3.2 |  |  |  |  |  |   
---|---|---|---|---|---|---  
/  |  | 1 | 2 | 3 | 4 |   
1 |  |  |  |  |  |   
2 |  |  |  |  |  |   
3 |  |  |  |  |  |   
4 |  |  |  |  |  |   
The pre-calculated _P_ values in _pv_arr_ (shown schematically in Table 3.2 for ) are then scanned in nested iterations over indices and to determine the following thematic change maps:
  * cmap: the interval of the most recent change, one band, byte values ,
  * smap: the interval of the first change, one band, byte values ,
  * fmap: the number of changes, one band, byte values ,
  * bmap: the changes in each interval, bands, byte values ).


A boolean variable _median_ is included in the code. Its purpose is to reduce the salt-and-pepper effect in no-change regions, which is at least partly a consequence of the uniform distribution of the _P_ values under (see the section [A note on P values](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2#a_note_on_p_values) in Part 2). If _median_ is _True_ , the _P_ values for each statistic are passed through a median filter before being compared with the significance threshold. This is not statistically kosher but probably justifiable if one is only interested in large homogeneous changes, for example flood inundations or deforestation.
Here is the code:
```
deffilter_j(current, prev):
"""Calculates change maps; iterates over j indices of pv_arr."""
  pv = ee.Image(current)
  prev = ee.Dictionary(prev)
  pvQ = ee.Image(prev.get('pvQ'))
  i = ee.Number(prev.get('i'))
  cmap = ee.Image(prev.get('cmap'))
  smap = ee.Image(prev.get('smap'))
  fmap = ee.Image(prev.get('fmap'))
  bmap = ee.Image(prev.get('bmap'))
  alpha = ee.Image(prev.get('alpha'))
  j = ee.Number(prev.get('j'))
  cmapj = cmap.multiply(0).add(i.add(j).subtract(1))
  # Check   Rj?      Ql?         Row i?
  tst = pv.lt(alpha).And(pvQ.lt(alpha)).And(cmap.eq(i.subtract(1)))
  # Then update cmap...
  cmap = cmap.where(tst, cmapj)
  # ...and fmap...
  fmap = fmap.where(tst, fmap.add(1))
  # ...and smap only if in first row.
  smap = ee.Algorithms.If(i.eq(1), smap.where(tst, cmapj), smap)
  # Create bmap band and add it to bmap image.
  idx = i.add(j).subtract(2)
  tmp = bmap.select(idx)
  bname = bmap.bandNames().get(idx)
  tmp = tmp.where(tst, 1)
  tmp = tmp.rename([bname])
  bmap = bmap.addBands(tmp, [bname], True)
  return ee.Dictionary({'i': i, 'j': j.add(1), 'alpha': alpha, 'pvQ': pvQ,
             'cmap': cmap, 'smap': smap, 'fmap': fmap, 'bmap':bmap})
deffilter_i(current, prev):
"""Arranges calculation of change maps; iterates over row-indices of pv_arr."""
  current = ee.List(current)
  pvs = current.slice(0, -1 )
  pvQ = ee.Image(current.get(-1))
  prev = ee.Dictionary(prev)
  i = ee.Number(prev.get('i'))
  alpha = ee.Image(prev.get('alpha'))
  median = prev.get('median')
  # Filter Ql p value if desired.
  pvQ = ee.Algorithms.If(median, pvQ.focalMedian(2.5), pvQ)
  cmap = prev.get('cmap')
  smap = prev.get('smap')
  fmap = prev.get('fmap')
  bmap = prev.get('bmap')
  first = ee.Dictionary({'i': i, 'j': 1, 'alpha': alpha ,'pvQ': pvQ,
              'cmap': cmap, 'smap': smap, 'fmap': fmap, 'bmap': bmap})
  result = ee.Dictionary(ee.List(pvs).iterate(filter_j, first))
  return ee.Dictionary({'i': i.add(1), 'alpha': alpha, 'median': median,
             'cmap': result.get('cmap'), 'smap': result.get('smap'),
             'fmap': result.get('fmap'), 'bmap': result.get('bmap')})

```

The following function ties the two steps together:
```
defchange_maps(im_list, median=False, alpha=0.01):
"""Calculates thematic change maps."""
  k = im_list.length()
  # Pre-calculate the P value array.
  pv_arr = ee.List(p_values(im_list))
  # Filter P values for change maps.
  cmap = ee.Image(im_list.get(0)).select(0).multiply(0)
  bmap = ee.Image.constant(ee.List.repeat(0, k.subtract(1))).add(cmap)
  alpha = ee.Image.constant(alpha)
  first = ee.Dictionary({'i': 1, 'alpha': alpha, 'median': median,
              'cmap': cmap, 'smap': cmap, 'fmap': cmap, 'bmap': bmap})
  return ee.Dictionary(pv_arr.iterate(filter_i, first))

```

And now we run the algorithm and display the color-coded change maps: _cmap_ , _smap_ (blue early, red late) and _fmap_ (blue few, red many):
```
result = change_maps(im_list, median=True, alpha=0.05)
# Extract the change maps and display.
cmap = ee.Image(result.get('cmap'))
smap = ee.Image(result.get('smap'))
fmap = ee.Image(result.get('fmap'))
location = aoi.centroid().coordinates().getInfo()[::-1]
palette = ['black', 'blue', 'cyan', 'yellow', 'red']
mp = folium.Map(location=location, zoom_start=11)
mp.add_ee_layer(cmap, {'min': 0, 'max': 25, 'palette': palette}, 'cmap')
mp.add_ee_layer(smap, {'min': 0, 'max': 25, 'palette': palette}, 'smap')
mp.add_ee_layer(fmap, {'min': 0, 'max': 25, 'palette': palette}, 'fmap')
mp.add_child(folium.LayerControl())

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_T4dvtMlna_8R_0.png)
#### Post-processing: The Loewner order
The above change maps are still difficult to interpret. But what about _bmap_ , the map of changes detected in each interval? Before we look at them it makes sense to include the direction of change, i.e., the [Loewner order](https://ieeexplore.ieee.org/document/8736751), see [Part 2](https://developers.google.com/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-2#change_direction_the_loewner_order). In the event of significant change at time , we can simply determine the positive or negative definiteness (or indefiniteness) of the difference between consecutive covariance matrix pixels
to get the change direction. But we can do better. Instead of subtracting the value for the preceding image, , we can subtract the average over all values up to and including time for which no change has been signalled. For example for , suppose there are significant changes in the first and fourth (last) interval. Then to get their directions we examine the differences
The running averages can be conveniently determined with the so-called _provisional means algorithm_. The average of the first images is calculated recursively as
The function _dmap_iter_ below is iterated over the bands of _bmap_ , replacing the values for changed pixels with
  * 1 for positive definite differences,
  * 2 for negative definite differences,
  * 3 for indefinite differences.

```
defdmap_iter(current, prev):
"""Reclassifies values in directional change maps."""
  prev = ee.Dictionary(prev)
  j = ee.Number(prev.get('j'))
  image = ee.Image(current)
  avimg = ee.Image(prev.get('avimg'))
  diff = image.subtract(avimg)
  # Get positive/negative definiteness.
  posd = ee.Image(diff.select(0).gt(0).And(det(diff).gt(0)))
  negd = ee.Image(diff.select(0).lt(0).And(det(diff).gt(0)))
  bmap = ee.Image(prev.get('bmap'))
  bmapj = bmap.select(j)
  dmap = ee.Image.constant(ee.List.sequence(1, 3))
  bmapj = bmapj.where(bmapj, dmap.select(2))
  bmapj = bmapj.where(bmapj.And(posd), dmap.select(0))
  bmapj = bmapj.where(bmapj.And(negd), dmap.select(1))
  bmap = bmap.addBands(bmapj, overwrite=True)
  # Update avimg with provisional means.
  i = ee.Image(prev.get('i')).add(1)
  avimg = avimg.add(image.subtract(avimg).divide(i))
  # Reset avimg to current image and set i=1 if change occurred.
  avimg = avimg.where(bmapj, image)
  i = i.where(bmapj, 1)
  return ee.Dictionary({'avimg': avimg, 'bmap': bmap, 'j': j.add(1), 'i': i})

```

We only have to modify the _change_maps_ function to include the change direction in the _bmap_ image:
```
defchange_maps(im_list, median=False, alpha=0.01):
"""Calculates thematic change maps."""
  k = im_list.length()
  # Pre-calculate the P value array.
  pv_arr = ee.List(p_values(im_list))
  # Filter P values for change maps.
  cmap = ee.Image(im_list.get(0)).select(0).multiply(0)
  bmap = ee.Image.constant(ee.List.repeat(0,k.subtract(1))).add(cmap)
  alpha = ee.Image.constant(alpha)
  first = ee.Dictionary({'i': 1, 'alpha': alpha, 'median': median,
              'cmap': cmap, 'smap': cmap, 'fmap': cmap, 'bmap': bmap})
  result = ee.Dictionary(pv_arr.iterate(filter_i, first))
  # Post-process bmap for change direction.
  bmap = ee.Image(result.get('bmap'))
  avimg = ee.Image(im_list.get(0))
  j = ee.Number(0)
  i = ee.Image.constant(1)
  first = ee.Dictionary({'avimg': avimg, 'bmap': bmap, 'j': j, 'i': i})
  dmap = ee.Dictionary(im_list.slice(1).iterate(dmap_iter, first)).get('bmap')
  return ee.Dictionary(result.set('bmap', dmap))

```

Because of the long delays when the zoom level is changed, it is a lot more convenient to export the change maps to GEE Assets and then examine them, either here in Colab or in the Code Editor. This also means the maps will be shown at the correct scale, irrespective of the zoom level. Here I export all of the change maps as a single image.
```
# Run the algorithm with median filter and at 1% significance.
result = ee.Dictionary(change_maps(im_list, median=True, alpha=0.01))
# Extract the change maps and export to assets.
cmap = ee.Image(result.get('cmap'))
smap = ee.Image(result.get('smap'))
fmap = ee.Image(result.get('fmap'))
bmap = ee.Image(result.get('bmap'))
cmaps = ee.Image.cat(cmap, smap, fmap, bmap).rename(['cmap', 'smap', 'fmap']+timestamplist[1:])
# EDIT THE ASSET PATH TO POINT TO YOUR ACCOUNT.
assetId = 'users/YOUR_USER_NAME/cmaps'
assexport = ee.batch.Export.image.toAsset(cmaps,
                     description='assetExportTask',
                     assetId=assetId, scale=10, maxPixels=1e9)
# UNCOMMENT THIS TO EXPORT THE MAP TO YOUR ACCOUNT.
#assexport.start()

```

The asset _cmaps_ is shared so we can all access it:
```
cmaps = ee.Image('projects/earthengine-community/tutorials/detecting-changes-in-sentinel-1-imagery-pt-3/cmaps')
cmaps = cmaps.updateMask(cmaps.gt(0))
location = aoi.centroid().coordinates().getInfo()[::-1]
palette = ['black', 'red', 'cyan', 'yellow']
mp = folium.Map(location=location, zoom_start=13)
mp.add_ee_layer(cmaps.select('T20191107'), {'min': 0,'max': 3, 'palette': palette}, 'T20191107')
mp.add_ee_layer(cmaps.select('T20191113'), {'min': 0,'max': 3, 'palette': palette}, 'T20191113')
mp.add_ee_layer(cmaps.select('T20191119'), {'min': 0,'max': 3, 'palette': palette}, 'T20191119')
mp.add_ee_layer(cmaps.select('T20191125'), {'min': 0,'max': 3, 'palette': palette}, 'T20191125')
mp.add_ee_layer(cmaps.select('T20191201'), {'min': 0,'max': 3, 'palette': palette}, 'T20191201')
mp.add_ee_layer(cmaps.select('T20191207'), {'min': 0,'max': 3, 'palette': palette}, 'T20191207')
mp.add_child(folium.LayerControl())

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/detecting-changes-in-sentinel-1-imagery-pt-3/index_files/output_qseBmVOH7xPg_0.png)
Now interpretation is somewhat easier. The negative definite (cyan) changes which appear between Nov. 7 and Nov. 13 correspond to decreases in intensity of _VV_ and _VH_ reflectance and are due to wide-spread flooding. The positive definite changes (red), which gradually overlay the flooded areas in subsequent intervals, correspond to receding flood waters.
### Outlook
Without reliable ground truth we can't really claim that change maps of the kind we have just generated will be helpful for flood damage assessment or control, but their potential usefulness is quite obvious. In the next and final part of the Tutorial we will have a look at some more (possible) applications of sequential change detection with SAR imagery using GEE. 
Was this helpful?
