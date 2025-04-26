 
#  Change Detection in Google Earth Engine - The MAD Transformation (Part 1) 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Context](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#context)
  * [Outline](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#outline)
  * [Prerequisites](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#prerequisites)
  * [Preliminaries](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#preliminaries)
  * [Simple Differences](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#simple_differences)
    * [Landkreis Olpe](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#landkreis_olpe)
  * [The MAD Transformation](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#the_mad_transformation)
    * [Auxiliary functions](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#auxiliary_functions)
    * [The MAD transformation](https://developers.google.com/earth-engine/tutorials/community/imad-tutorial-pt1#the_mad_transformation_2)


Author(s): [ mortcanty ](https://github.com/mortcanty "View the profile for mortcanty on GitHub")
Tutorials contributed by the Earth Engine developer community are not part of the official Earth Engine product documentation. 
[ ![Colab logo](https://developers.google.com/static/earth-engine/images/colab_logo_32px.png) Run in Google Colab ](https://colab.research.google.com/github/google/earthengine-community/blob/master/tutorials/imad-tutorial-pt1/index.ipynb) |  [ ![GitHub logo](https://developers.google.com/static/earth-engine/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/google/earthengine-community/blob/master/tutorials/imad-tutorial-pt1/index.ipynb)  
---|---  
## Context
With the great tools available in Google Earth Engine (GEE) it is easy to generate satellite image differences and time series animations which visualize changes on the Earth surface, sometimes quite dramatically. Such representations are very good as eye-openers to give a conceptual, overall impression of change. They may, however, be perceived differently from person to person and not allow more than subjective interpretation. With more objective and rigorous statistical methods one can often extract more and better change information on both pixel and patch/field levels.
The Multivariate Alteration Detection (MAD) transformation was proposed and developed some time ago by [Allan Nielsen and his coworkers](https://www2.imm.dtu.dk/pubdb/pubs/1220-full.html) at the Technical University of Denmark and later [extended to an iteratively re-weighted version](https://www2.imm.dtu.dk/pubdb/pubs/4695-full.html) called IR-MAD or iMAD. The iMAD algorithm has since found widespread application for the generation of change information from visual/infrared imagery as well as for performing [relative radiometric normalization](http://www2.imm.dtu.dk/pubdb/pubs/5362-full.html) of image pairs.
This tutorial is intended to familiarize GEE users with the iMAD method so that they may use it with confidence in their research wherever they think it might be appropriate. It is based on material taken from Chapter 9 of [Canty (2019)](https://www.taylorfrancis.com/books/image-analysis-classification-change-detection-remote-sensing-morton-john-canty/10.1201/9780429464348). In preparing the tutorial we have tried to take as much advantage as possible of the GEE platform to illustrate and demonstrate the theory interactively.
## Outline
The tutorial is split into three parts, of which this is the first:
```
1.TheMADTransformation
2.TheiMADAlgorithm
3.RadiometricNormalizationandHarmonization

```

In Part 3, a convenient Jupyter widget interface for running the iMAD algorithm from a Docker container is also described.
## Prerequisites
Little prior knowledge is required to follow the discussion, apart from some familiarity with the GEE API and a basic, intuitive understanding of the simple statistical concepts of probability distributions and their moments, in particular, mean, variance (var) and covariance (cov). Since we'll be working with multispectral imagery, in the course of the tutorial we'll frequently mention the so-called _dispersion matrix_ or _variance-covariance matrix_ , or simply _covariance matrix_ for short. The covariance matrix of a set of measured variables \\(X_i,\ i=1\dots N\\), such as the band-wise values of a multispectral image pixel, is defined as
$$ \Sigma_X\ =\ \begin{pmatrix} \sigma^2_1 & \sigma_{12} & \dots & \sigma_{1N} \cr \sigma_{21} & \sigma^2_2& \dots & \sigma_{2N} \cr \vdots & \vdots & \vdots& \vdots \cr \sigma_{N1} & \sigma_{N2} & \dots & \sigma^2_N \end{pmatrix}, $$
where
$$ \sigma_{ij} = {\rm cov}(X_i,X_j) = \langle (X_i - \bar X_i)(X_j - \bar X_j)\rangle, \quad \sigma^2_i = {\rm cov}(X_i,X_i) = {\rm var}(X_i) = \langle (X_i-\bar X_i)^2\rangle, \quad \ i,j = 1\dots N. $$
Here, \\(\bar X_i\\) denotes mean value and \\(\langle\dots\rangle\\) is ensemble average. The covariance matrix is symmetric about its principal diagonal. The _correlation_ between \\(X_i\\) and \\(X_j\\) is defined as the normalized covariance
$$ \rho_{ij} = {{\rm cov}(X_i,X_j)\over \sqrt{{\rm var}(X_i)}\sqrt{{\rm var}(X_j)}} = {\sigma_{ij} \over \sigma_i\sigma_j}. $$
Since we are in a Colab environment we will use the Python API, but it is so similar to the JavaScript version that this should pose no problems to anyone not acquainted with it.
## Preliminaries
The cells below execute the necessary formalities for accessing Earth Engine from this Colab notebook. They also import the various Python add-ons needed, including the [geemap](https://geemap.org/) interactive map package, and define a few helper routines for displaying results.
```
importee
ee.Authenticate(auth_mode='notebook')
ee.Initialize()

```
```
# Import other packages used in the tutorial
%matplotlib inline
importgeemap
importnumpyasnp
importrandom,time
importmatplotlib.pyplotasplt
fromscipy.statsimport norm, chi2
frompprintimport pprint # for pretty printing

```
```
# Truncate a 1-D array to dec decimal places
deftrunc(values, dec = 3):
  return np.trunc(values*10**dec)/(10**dec)

```
```
# Display an image in a one percent linear stretch
defdisplay_ls(image, map, name, centered = False):
  bns = image.bandNames().length().getInfo()
  if bns == 3:
    image = image.rename('B1', 'B2', 'B3')
    pb_99 = ['B1_p99', 'B2_p99', 'B3_p99']
    pb_1 = ['B1_p1', 'B2_p1', 'B3_p1']
    img = ee.Image.rgb(image.select('B1'), image.select('B2'), image.select('B3'))
  else:
    image = image.rename('B1')
    pb_99 = ['B1_p99']
    pb_1 = ['B1_p1']
    img = image.select('B1')
  percentiles = image.reduceRegion(ee.Reducer.percentile([1, 99]), maxPixels=1e11)
  mx = percentiles.values(pb_99)
  if centered:
    mn = ee.Array(mx).multiply(-1).toList()
  else:
    mn = percentiles.values(pb_1)
  map.addLayer(img, {'min': mn, 'max': mx}, name)

```

## Simple Differences
Let's begin by considering two \\(N\\)-band optical/infrared images of the same scene acquired with the same sensor at two different times, between which ground reflectance changes have occurred at some locations but not everywhere. To see those changes we can "flick back and forth" between gray scale or RGB representations of the images on a computer display. Alternatively we can simply subtract one image from the other and, provided the intensities at the two time points have been calibrated or normalized in some way, examine the difference. Symbolically the difference image is
$$ Z = X-Y $$
where
$$ X= \begin{pmatrix}X_1\cr X_2\cr\vdots\cr X_N\end{pmatrix},\quad Y= \begin{pmatrix}Y_1\cr Y_2\cr\vdots\cr Y_N\end{pmatrix} $$
are 'typical' pixel vectors (more formally: _random vectors_) representing the first and second image, respectively.
### Landkreis Olpe
For example, here is an area of interest (aoi) covering a heavily forested administrative district (Landkreis Olpe) in North Rhine Westphalia, Germany. Due to severe drought in recent years large swaths of shallow-root coniferous trees have died and been cleared away, leaving deciduous trees for the most part untouched.
Toggle code ```
aoi = ee.FeatureCollection(
  'projects/google/imad_tutorial/landkreis_olpe_aoi').geometry()

```

We first collect two Sentinel-2 scenes which bracket some of the recent clear cutting (June, 2021 and June, 2022) and print out their timestamps. For demonstration purposes we choose top of atmosphere reflectance since the MAD transformation does not require absolute surface reflectances.
```
defcollect(aoi, t1a ,t1b, t2a, t2b):
  try:
    im1 = ee.Image( ee.ImageCollection("COPERNICUS/S2_HARMONIZED")
                .filterBounds(aoi)
                .filterDate(ee.Date(t1a), ee.Date(t1b))
                .filter(ee.Filter.contains(rightValue=aoi,leftField='.geo'))
                .sort('CLOUDY_PIXEL_PERCENTAGE')
                .first()
                .clip(aoi) )
    im2 = ee.Image( ee.ImageCollection("COPERNICUS/S2_HARMONIZED")
                .filterBounds(aoi)
                .filterDate(ee.Date(t2a), ee.Date(t2b))
                .filter(ee.Filter.contains(rightValue=aoi,leftField='.geo'))
                .sort('CLOUDY_PIXEL_PERCENTAGE')
                .first()
                .clip(aoi) )
    timestamp = im1.date().format('E MMM dd HH:mm:ss YYYY')
    print(timestamp.getInfo())
    timestamp = im2.date().format('E MMM dd HH:mm:ss YYYY')
    print(timestamp.getInfo())
    return (im1, im2)
  except Exception as e:
    print('Error: %s'%e)
im1, im2 = collect(aoi, '2021-06-01', '2021-06-30', '2022-06-01', '2022-06-30')

```
```
Sun Jun 13 10:36:49 2021
Thu Jun 16 10:46:56 2022

```

In order to view the images, we instantiate an interactive map located at the center of the aoi. Since the map requires lat/long coordinates we have to reverse the long/lat order returned from the _coordinates()_ method of the _ee.Geometry.centroid()_ object:
```
# Interactive map
M1 = geemap.Map()
M1.centerObject(aoi, 11)
M1

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/imad-tutorial-pt1/index_files/output_kc_pwScrphK1_1.png)
Then we display RGB composites of the first 3 (visual) bands of the Sentinel images as well as their difference. We use the previously defined function _display_ls()_ to display the images in a one percent linear stretch.
```
visirbands = ['B2','B3','B4','B8','B11','B12']
visbands = ['B2','B3','B4']
diff = im1.subtract(im2).select(visbands)
display_ls(im1.select(visbands), M1, 'Image 1')
display_ls(im2.select(visbands), M1, 'Image 2')
display_ls(diff, M1, 'Difference')

```

Small intensity differences (the gray-ish background in the difference image above) indicate no change, large positive (bright) or negative (dark) colors indicate change. The most obvious changes are in fact due to the clear cutting. Decision thresholds can be set to define significant changes. The thresholds are usually expressed in terms of standard deviations from the mean difference value, which is taken to correspond to no change. The per-band variances of the difference images are simply
$$ {\rm var}(Z_i) = {\rm var}(X_i - Y_i) = {\rm var}(X_i) + {\rm var}(Y_i) - 2\cdot{\rm cov}(X_i,Y_i),\quad i=1\dots N, $$
or, if the bands are uncorrelated, about twice as noisy as the individual image bands. Normally \\(X_i\\) and \\(Y_i\\) are positively correlated (\\({\rm cov}(X_i,Y_i) > 0\\)) so the variance of \\(Z_i\\) is somewhat smaller. When the difference signatures in the spectral channels are combined so as to try to characterize the nature of the changes that have taken place, one speaks of _spectral change vector analysis_.
While the recent clear cuts are fairly easily identified as (some but not all of) the dark areas in the simple difference image above, it is possible to derive a better and more informative change map. This involves taking greater advantage of the statistical properties of the images.
## The MAD Transformation
Let's make a linear combination of the intensities for all \\(N\\) bands in the first image \\(X\\), thus creating a scalar image
$$ U = a_1X_1 + a_2X_2 + \dots + a_NX_N = {\bf a}^\top X. \tag{1} $$
The symbol \\({\bf a}^\top\\) denotes the transpose of the column vector \\({\bf a}=\begin{pmatrix}a_1\cr a_2\cr\vdots\cr a_N\end{pmatrix}\\), in other words the row vector \\({\bf a}^\top = (a_1,a_2 \dots a_N)\\).
The expression \\({\bf a}^\top X\\) is called an _inner vector product_. The vector of coefficients \\({\bf a}\\) is as yet unspecified. We'll do the same for the second image \\(Y\\), forming the linear combination
$$ V = b_1Y_1 + b_2Y_2 + \dots + b_NY_N = {\bf b}^\top Y, \tag{2} $$
and then look at the scalar difference \\(U-V\\). Change information is now contained, for the time being, in a single image rather than distributed among all \\(N\\) bands.
We have of course to choose the coefficient vectors \\({\bf a}\\) and \\({\bf b}\\) in some suitable way. In [Nielsen et al. (1998)](https://www2.imm.dtu.dk/pubdb/pubs/1220-full.html) it is suggested that they be determined by making the transformed images \\(U\\) and \\(V\\) _as similar as they can be_ before taking their difference. This sounds at first counter-intuitive: Why make the images similar when we want to see the dissimilarities? The crux is that, in making them match one another by taking suitable linear combinations, we ensure that pixels in the transformed images \\(U\\) and \\(V\\) at which _indeed no change has taken place_ will be as similar as possible before they are compared (subtracted). The genuine changes will then, it is hoped, be all the more apparent in the difference image.
This process of "similar making" can be accomplished in statistics with standard [_Canonical Correlation Analysis_ (CCA)](https://en.wikipedia.org/wiki/Canonical_correlation), a technique first described by Harold Hotelling in 1936. Canonical Correlation Analysis of the images represented by Equations (1) and (2) _maximizes the correlation_
$$ \rho = {{\rm cov}(U,V)\over \sqrt{{\rm var}(U)}\sqrt{{\rm var}(V)}}, \tag{3} $$
between the random variables \\(U\\) and \\(V\\), which is just what we want.
One technical point: Arbitrary multiples of \\(U\\) and \\(V\\) would clearly have the same correlation (the multiples will cancel off in numerator and denominator), so a constraint must be chosen. A convenient one is
$$ {\rm var}(U)={\rm var}(V)=1. \tag{4} $$
For those more versed in linear algebra the details of CCA are given in [Canty (2019)](https://www.taylorfrancis.com/books/image-analysis-classification-change-detection-remote-sensing-morton-john-canty/10.1201/9780429464348) beginning on page 385. It all boils down to solving two so-called _generalized eigenvalue problems_ for determining the transformation vectors \\({\bf a}\\) and \\({\bf b}\\) in Equations (1) and (2), respectively. There is not just one solution but rather \\(N\\) solutions. They consist of the \\(N\\) pairs of _eigenvectors_ \\(({\bf a}^i, {\bf b}^i)\\),
$$ {\bf a}^i=\begin{pmatrix}a_1\cr a_2\cr\vdots\cr a_N \end{pmatrix}_i,\quad {\bf b}^i=\begin{pmatrix}b_1\cr b_2\cr\vdots\cr b_N \end{pmatrix}_i, \quad i=1\dots N $$
and, correspondingly, the \\(N\\) pairs of _canonical variates_ \\((U_i, V_i),\ i= 1\dots N\\). (Readers familiar with Principal Components Analysis (PCA) will recognize the similarity. When applying PCA to an N-band image, an ordinary (rather than a generalized) eigenvalue problem is solved to maximize variance, resulting in \\(N\\) principal component bands.)
Unlike the bands of the original images \\(X\\) and \\(Y\\), which are ordered by spectral wavelength, the canonical variates are ordered by similarity or correlation. The difference images
$$ M_i = U_i - V_i = ({\bf a}^i)^\top X - ({\bf b}^i)^\top Y,\quad i=1\dots N, \tag{5} $$
contain the change information and are called the _MAD variates_.
### Auxiliary functions
To run the MAD transformation on GEE image pairs we need some helper routines. These are coded below. The first, called _covarw()_ , returns the weighted covariance matrix of an \\(N\\)-band image as well as a weighted, centered (mean-zero) version of the image. Why it is important to weight the pixels before centering or calculating the covariance matrix will become apparent in Part 2 of the tutorial.
```
defcovarw(image, weights = None, scale = 20, maxPixels = 1e10):
'''Return the weighted centered image and its weighted covariance matrix'''
  try:
    geometry = image.geometry()
    bandNames = image.bandNames()
    N = bandNames.length()
    if weights is None:
      weights = image.constant(1)
    weightsImage = image.multiply(ee.Image.constant(0)).add(weights)
    means = image.addBands(weightsImage) \
          .reduceRegion(ee.Reducer.mean().repeat(N).splitWeights(),
                scale = scale,
                maxPixels = maxPixels) \
          .toArray() \
          .project([1])
    centered = image.toArray().subtract(means)
    B1 = centered.bandNames().get(0)
    b1 = weights.bandNames().get(0)
    nPixels = ee.Number(centered.reduceRegion(ee.Reducer.count(),
                        scale = scale,
                        maxPixels = maxPixels).get(B1))
    sumWeights = ee.Number(weights.reduceRegion(ee.Reducer.sum(),
                          geometry = geometry,
                          scale = scale,
                          maxPixels = maxPixels).get(b1))
    covw = centered.multiply(weights.sqrt()) \
          .toArray() \
          .reduceRegion(ee.Reducer.centeredCovariance(),
                  geometry = geometry,
                  scale = scale,
                  maxPixels = maxPixels) \
          .get('array')
    covw = ee.Array(covw).multiply(nPixels).divide(sumWeights)
    return (centered.arrayFlatten([bandNames]), covw)
  except Exception as e:
    print('Error: %s'%e)

```

The second routine, called _corr()_ , transforms a covariance matrix to the equivalent correlation matrix by dividing by the square roots of the variances, see Equation (3).
```
defcorr(cov):
'''Transform covariance matrix to correlation matrix'''
  # diagonal matrix of inverse sigmas
  sInv = cov.matrixDiagonal().sqrt().matrixToDiag().matrixInverse()
  # transform
  corr = sInv.matrixMultiply(cov).matrixMultiply(sInv).getInfo()
  # truncate
  return [list(map(trunc, corr[i])) for i in range(len(corr))]

```

For example the code below calculates the (unweighted) covariance matrix of the visual and infrared bands of the image _im1_ and prints out the corresponding correlation matrix.
```
_, cov = covarw(im1.select(visirbands))
pprint(corr(cov))

```
```
[[np.float64(1.0),
 np.float64(0.952),
 np.float64(0.949),
 np.float64(0.063),
 np.float64(0.647),
 np.float64(0.79)],
 [np.float64(0.952),
 np.float64(0.999),
 np.float64(0.927),
 np.float64(0.291),
 np.float64(0.772),
 np.float64(0.847)],
 [np.float64(0.949),
 np.float64(0.927),
 np.float64(1.0),
 np.float64(0.008),
 np.float64(0.74),
 np.float64(0.893)],
 [np.float64(0.063),
 np.float64(0.291),
 np.float64(0.008),
 np.float64(1.0),
 np.float64(0.486),
 np.float64(0.22)],
 [np.float64(0.647),
 np.float64(0.772),
 np.float64(0.74),
 np.float64(0.486),
 np.float64(1.0),
 np.float64(0.933)],
 [np.float64(0.79),
 np.float64(0.847),
 np.float64(0.893),
 np.float64(0.22),
 np.float64(0.933),
 np.float64(1.0)]]

```

Note that the spectral bands of the image are generally highly and positively correlated with one another.
By stacking the images one atop the other we can use the helper functions to display the between image correlations
$$ \rm{corr}(X_i,Y_i), \quad i= 1\dots N. $$
They can be found in the diagonal of the upper left \\(6\times 6\\) submatrix of the correlation matrix for the stacked image.
```
im12 = im1.select(visirbands).addBands(im2.select(visirbands))
_, covar = covarw(im12)
correl = np.array(corr(covar))
print(np.diag(correl[:6, 6:]))

```
```
[0.799 0.784 0.682 0.867 0.666 0.632]

```

It is these between image correlations that the MAD algorithm tries to maximize.
The third and last auxiliary routine, _geneiv()_ , is the core of CCA and the MAD transformation. It solves the _generalized eigenproblem_ ,
$$ CX = \lambda BX $$
for two \\(N\times N\\) matrices \\(C\\) and \\(B\\), returning the \\(N\\) solutions, or eigenvectors, \\(X_i\\) and the \\(N\\) eigenvalues \\(\lambda_i, \ i=1\dots N\\).
Toggle code ```
defgeneiv(C,B):
'''Return the eigenvalues and eigenvectors of the generalized eigenproblem
             C*X = lambda*B*X'''
  try:
    C = ee.Array(C)
    B = ee.Array(B)
    # Li = choldc(B)^-1
    Li = ee.Array(B.matrixCholeskyDecomposition().get('L')).matrixInverse()
    # solve symmetric, ordinary eigenproblem Li*C*Li^T*x = lambda*x
    Xa = Li.matrixMultiply(C) \
      .matrixMultiply(Li.matrixTranspose()) \
      .eigen()
    # eigenvalues as a row vector
    lambdas = Xa.slice(1, 0, 1).matrixTranspose()
    # eigenvectors as columns
    X = Xa.slice(1, 1).matrixTranspose()
    # generalized eigenvectors as columns, Li^T*X
    eigenvecs = Li.matrixTranspose().matrixMultiply(X)
    return (lambdas, eigenvecs)
  except Exception as e:
    print('Error: %s'%e)

```

The next cell codes the MAD transformation itself in the function _mad_run()_ , taking as input two multiband images and returning the _canonical variates_
$$ U_i, \ V_i, \quad i=1\dots N, $$
the _MAD variates_
$$ M_i = U_i - V_i, \quad i=1\dots N, $$
as well as the sum of the squares of the standardized MAD variates,
$$ Z = \sum_{i=1}^N\left({M_i\over \sigma_{M_i}}\right)^2. $$
### The MAD transformation
Toggle code ```
defmad_run(image1, image2, scale = 20):
'''The MAD transformation of two multiband images'''
  try:
    image = image1.addBands(image2)
    region = image.geometry()
    nBands = image.bandNames().length().divide(2)
    centeredImage,covarArray = covarw(image,scale=scale)
    bNames = centeredImage.bandNames()
    bNames1 = bNames.slice(0,nBands)
    bNames2 = bNames.slice(nBands)
    centeredImage1 = centeredImage.select(bNames1)
    centeredImage2 = centeredImage.select(bNames2)
    s11 = covarArray.slice(0,0,nBands).slice(1,0,nBands)
    s22 = covarArray.slice(0,nBands).slice(1,nBands)
    s12 = covarArray.slice(0,0,nBands).slice(1,nBands)
    s21 = covarArray.slice(0,nBands).slice(1,0,nBands)
    c1 = s12.matrixMultiply(s22.matrixInverse()).matrixMultiply(s21)
    b1 = s11
    c2 = s21.matrixMultiply(s11.matrixInverse()).matrixMultiply(s12)
    b2 = s22
    # solution of generalized eigenproblems
    lambdas, A = geneiv(c1,b1)
    _,    B = geneiv(c2,b2)
    rhos = lambdas.sqrt().project(ee.List([1]))
    # MAD variances
    sigma2s = rhos.subtract(1).multiply(-2).toList()
    sigma2s = ee.Image.constant(sigma2s)
    # ensure sum of correlations between X and U is positive
    tmp = s11.matrixDiagonal().sqrt()
    ones = tmp.multiply(0).add(1)
    tmp = ones.divide(tmp).matrixToDiag()
    s = tmp.matrixMultiply(s11).matrixMultiply(A).reduce(ee.Reducer.sum(),[0]).transpose()
    A = A.matrixMultiply(s.divide(s.abs()).matrixToDiag())
    # ensure positive correlation between U and V
    tmp = A.transpose().matrixMultiply(s12).matrixMultiply(B).matrixDiagonal()
    tmp = tmp.divide(tmp.abs()).matrixToDiag()
    B = B.matrixMultiply(tmp)
    # canonical and MAD variates
    centeredImage1Array = centeredImage1.toArray().toArray(1)
    centeredImage2Array = centeredImage2.toArray().toArray(1)
    U = ee.Image(A.transpose()).matrixMultiply(centeredImage1Array) \
          .arrayProject([0]) \
          .arrayFlatten([bNames2])
    V = ee.Image(B.transpose()).matrixMultiply(centeredImage2Array) \
          .arrayProject([0]) \
          .arrayFlatten([bNames2])
    MAD = U.subtract(V)
    # chi square image
    Z = MAD.pow(2) \
        .divide(sigma2s) \
        .reduce(ee.Reducer.sum()) \
        .clip(region)
    return (U, V, MAD, Z)
  except Exception as e:
    print('Error: %s'%e)

```

After setting up the MAD transformation on the six visual and infrared bands of the Landkreis Olpe images,
```
U, V, MAD, Z = mad_run(im1.select(visirbands), im2.select(visirbands))

```

we display an RGB composite of the first 3 MAD variates, together with the original images and their simple difference:
```
M2 = geemap.Map()
M2.centerObject(aoi, 11)
display_ls(im1.select(visbands), M2, 'Image 1')
display_ls(im2.select(visbands), M2, 'Image 2')
display_ls(diff, M2, 'Difference')
display_ls(MAD.select(0, 1, 2), M2, 'MAD Image', True)
M2

```

![png](https://developers.google.com/static/earth-engine/tutorials/community/imad-tutorial-pt1/index_files/output_zNAGaOr8sShC_1.png)
The richness in colors in the MAD image is a consequence of the decoupling (orthogonalization) of the MAD components, as will be explained below.
Pretty colors notwithstanding, when compared with the simple difference image the result is _mittelprächtig_ (German slang for "not so hot"), and certainly no easier to interpret. However we're not finished.
The canonical variates have very nice properties indeed. They are _all mutually uncorrelated_ except for the pairs \\((U_i,V_i)\\), and these are ordered by decreasing positive correlation:
$$ \rho_i = {\rm cov}(U_i, V_i),\quad i=1\dots N, \tag{6} $$
with \\(\rho_1 \ge \rho_2 \ge\dots \ge\rho_N\\).
Stacking the images \\(U\\) and \\(V\\), these facts can be read from the \\(12\times 12\\) correlation matrix:
```
_, covar = covarw(U.addBands(V))
correl = np.array(corr(covar))
pprint(correl)
print('rho =', np.diag(correl[:6,6:]))

```
```
array([[ 1.  , 0.001, -0.  , 0.  , -0.  , 0.  , 0.923, 0.  ,
    -0.  , 0.  , -0.  , -0.  ],
    [ 0.001, 0.999, 0.  , 0.  , -0.  , -0.  , 0.  , 0.864,
     0.  , 0.  , -0.  , -0.  ],
    [-0.  , 0.  , 1.  , 0.  , 0.  , -0.  , -0.  , 0.  ,
     0.707, -0.  , 0.  , -0.  ],
    [ 0.  , 0.  , 0.  , 1.  , 0.  , 0.  , 0.  , 0.  ,
    -0.  , 0.642, 0.  , 0.  ],
    [-0.  , -0.  , 0.  , 0.  , 1.  , 0.  , -0.  , -0.  ,
     0.  , 0.  , 0.536, 0.  ],
    [ 0.  , -0.  , -0.  , 0.  , 0.  , 0.999, -0.  , -0.  ,
    -0.  , 0.  , 0.  , 0.369],
    [ 0.923, 0.  , -0.  , 0.  , -0.  , -0.  , 1.  , 0.  ,
    -0.  , 0.  , -0.  , -0.  ],
    [ 0.  , 0.864, 0.  , 0.  , -0.  , -0.  , 0.  , 1.  ,
     0.  , 0.  , -0.  , -0.  ],
    [-0.  , 0.  , 0.707, -0.  , 0.  , -0.  , -0.  , 0.  ,
     1.  , -0.  , 0.  , -0.  ],
    [ 0.  , 0.  , -0.  , 0.642, 0.  , 0.  , 0.  , 0.  ,
    -0.  , 1.  , 0.  , 0.  ],
    [-0.  , -0.  , 0.  , 0.  , 0.536, 0.  , -0.  , -0.  ,
     0.  , 0.  , 1.  , 0.  ],
    [-0.  , -0.  , -0.  , 0.  , 0.  , 0.369, -0.  , -0.  ,
    -0.  , 0.  , 0.  , 0.999]])
rho = [0.923 0.864 0.707 0.642 0.536 0.369]

```

The MAD variates themselves are consequently also mutually uncorrelated, their covariances being given by
$$ {\rm cov}(M_i,M_j) = {\rm cov}(U_i-V_i,U_j-V_j)= 0,\quad i\ne j=1\dots N, \tag{7} $$
and their variances by
$$ \sigma_{M_i}^2={\rm var}(U_i-V_i)= {\rm var}(U_i)+{\rm var}(V_i) -2{\rm cov}(U_i,V_i) = 2(1-\rho_i),\quad i=1\dots N, \tag{8} $$
where the last equality follows from the constraint Equation (4). Let's check.
```
# display MAD covariance matrix
_, covar = covarw(MAD)
covar = covar.getInfo()
[list(map(trunc,covar[i])) for i in range(len(covar))]

```
```
[[np.float64(0.079),
 np.float64(0.0),
 np.float64(-0.0),
 np.float64(0.0),
 np.float64(0.0),
 np.float64(0.0)],
 [np.float64(0.0),
 np.float64(0.14),
 np.float64(0.0),
 np.float64(-0.0),
 np.float64(-0.0),
 np.float64(0.0)],
 [np.float64(-0.0),
 np.float64(0.0),
 np.float64(0.304),
 np.float64(0.0),
 np.float64(-0.0),
 np.float64(-0.0)],
 [np.float64(0.0),
 np.float64(-0.0),
 np.float64(0.0),
 np.float64(0.372),
 np.float64(0.0),
 np.float64(0.0)],
 [np.float64(0.0),
 np.float64(-0.0),
 np.float64(-0.0),
 np.float64(0.0),
 np.float64(0.482),
 np.float64(0.0)],
 [np.float64(0.0),
 np.float64(0.0),
 np.float64(-0.0),
 np.float64(0.0),
 np.float64(0.0),
 np.float64(0.657)]]

```

The first MAD variate has minimum variance in its pixel intensities. The second MAD variate has minimum variance subject to the condition that its pixel intensities are statistically uncorrelated with those in the first variate; the third has minimum spread subject to being uncorrelated with the first two, and so on. Depending on the type of change present, any of the components may exhibit significant change information, although it tends to be concentrated in the first few MAD variates. One of the nicest aspects of the MAD transformation is that it can sort different categories of change into different, uncorrelated image bands.
However, the result, as we saw, needs some improvement. This is the subject of Part 2. 
