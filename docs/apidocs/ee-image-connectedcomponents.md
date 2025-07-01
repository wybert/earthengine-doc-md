 
#  ee.Image.connectedComponents
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Finds connected components with the same value of the first band of the input and labels them with a globally unique value. Connectedness is specified by the given kernel. Objects larger than maxSize are considered background, and are masked. 
Usage| Returns  
---|---  
`Image.connectedComponents(connectedness, maxSize)`| Image  
Argument| Type| Details  
---|---|---  
this: `image`| Image| The image to label.  
`connectedness`| Kernel| Connectedness kernel.  
`maxSize`| Integer| Maximum size of objects to be labeled.  
Was this helpful?
