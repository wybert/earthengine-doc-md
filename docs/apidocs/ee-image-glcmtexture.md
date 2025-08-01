 
#  ee.Image.glcmTexture
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Computes texture metrics from the Gray Level Co-occurrence Matrix around each pixel of every band. The GLCM is a tabulation of how often different combinations of pixel brightness values (grey levels) occur in an image. It counts the number of times a pixel of value X lies next to a pixel of value Y, in a particular direction and distance. and then derives statistics from this tabulation.
This implementation computes the 14 GLCM metrics proposed by Haralick, and 4 additional metrics from Conners. Inputs are required to be integer valued.
The output consists of 18 bands per input band if directional averaging is on and 18 bands per directional pair in the kernel, if not:
ASM: f1, Angular Second Moment; measures the number of repeated pairs
CONTRAST: f2, Contrast; measures the local contrast of an image
CORR: f3, Correlation; measures the correlation between pairs of pixels
VAR: f4, Variance; measures how spread out the distribution of gray-levels is
IDM: f5, Inverse Difference Moment; measures the homogeneity
SAVG: f6, Sum Average
SVAR: f7, Sum Variance
SENT: f8, Sum Entropy
ENT: f9, Entropy. Measures the randomness of a gray-level distribution
DVAR: f10, Difference variance
DENT: f11, Difference entropy
IMCORR1: f12, Information Measure of Corr. 1
IMCORR2: f13, Information Measure of Corr. 2
MAXCORR: f14, Max Corr. Coefficient. (not computed)
DISS: Dissimilarity
INERTIA: Inertia
SHADE: Cluster Shade
PROM: Cluster prominence
More information can be found in the two papers: Haralick et. al, 'Textural Features for Image Classification', https://doi.org/10.1109/TSMC.1973.4309314 and Conners, et al, Segmentation of a high-resolution urban scene using texture operators', https://sdoi.org/10.1016/0734-189X(84)90197-X.
Usage | Returns  
---|---  
`Image.glcmTexture(_size_, _kernel_, _average_)`|  Image  
Argument | Type | Details  
---|---|---  
this: `image` | Image | The image for which to compute texture metrics.  
`size` | Integer, default: 1 | The size of the neighborhood to include in each GLCM.  
`kernel` | Kernel, default: null | A kernel specifying the x and y offsets over which to compute the GLCMs. A GLCM is computed for each pixel in the kernel that is non-zero, except the center pixel and as long as a GLCM hasn't already been computed for the same direction and distance. For example, if either or both of the east and west pixels are set, only 1 (horizontal) GLCM is computed. Kernels are scanned from left to right and top to bottom. The default is a 3x3 square, resulting in 4 GLCMs with the offsets (-1, -1), (0, -1), (1, -1) and (-1, 0).  
`average` | Boolean, default: true | If true, the directional bands for each metric are averaged.  
