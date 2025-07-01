 
#  About Google Earth Engine
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Key Features](https://developers.google.com/earth-engine/guides#key_features)
    * [Geospatial analysis, simplified and scalable](https://developers.google.com/earth-engine/guides#geospatial_analysis_simplified_and_scalable)
    * [Processing environments](https://developers.google.com/earth-engine/guides#processing_environments)
    * [Development environments](https://developers.google.com/earth-engine/guides#development_environments)
    * [Visualization and results](https://developers.google.com/earth-engine/guides#visualization_and_results)
    * [Machine learning](https://developers.google.com/earth-engine/guides#machine_learning)
  * [Access and management](https://developers.google.com/earth-engine/guides#access_and_management)


Google Earth Engine is a [Google Cloud product](https://cloud.google.com/earth-engine) for geospatial analysis at scale. It combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale computation to accelerate environmental research and applications.
## Key Features
### Geospatial analysis, simplified and scalable
Earth Engine integrates an extensive geospatial [data catalog](https://developers.google.com/earth-engine/datasets) with distributed computing, accessible through client libraries. Users can access a wide range of satellite and environmental data, as well as [incorporate their own datasets](https://developers.google.com/earth-engine/guides/image_upload). The platform simplifies geospatial analysis by automatically handling data projection, scaling, and compositing based on user-specified parameters. Its [analytical functions](https://developers.google.com/earth-engine/guides/objects_methods_overview) operate efficiently across different scales without requiring explicit data preparation steps or chunking. By managing complex data processing and computational scaling internally, Earth Engine enables users to focus on analysis rather than technical setup.
### Processing environments
Earth Engine supports [two modes of analysis](https://developers.google.com/earth-engine/guides/processing_environments):
  * **Interactive mode** : For rapid real-time data exploration and visualization of small amounts of data.
  * **Batch mode** : For large-scale computationally intensive tasks on large amounts of data.


### Development environments
Developers can choose between two primary development environments:
  * **Python client library** : A flexible interface to Earth Engine for integration with the broader Python ecosystem, facilitating advanced workflows, and interactive analysis in Jupyter notebooks.
  * **JavaScript Code Editor** : A dedicated web-based development environment for rapid prototyping, exploration, and Earth Engine App creation.


### Visualization and results
Earth Engine supports geospatial analysis from initial prototyping to final data export. Its efficient tiling and computation system, integrated with interactive map widgets, provides rapid visualization and inspection capabilities in both the Code Editor and Python environments. This allows for immediate data exploration and iteration. When ready, users can [export](https://developers.google.com/earth-engine/guides/exporting) raster and vector results to Google Cloud Storage, BigQuery, or Google Drive, as well as download data locally in formats compatible with pandas, NumPy, and Xarray. Additionally, Earth Engine supports the creation of [interactive web applications](https://developers.google.com/earth-engine/guides/apps), enabling users to share their geospatial insights with a wide audience.
### Machine learning
[Machine learning tools](https://developers.google.com/earth-engine/guides/machine-learning) for regression, classification, image segmentation, and accuracy assessment are built into Earth Engine. Once trained, models can be saved and applied repeatedly. Classical ML workflows are streamlined within Earth Engine's integrated system. For more advanced options or externally trained models, integration with [Vertex AI](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) is provided, allowing models to be brought to Earth Engine's data or enabling the construction of deep learning models and neural network-based analyses.
## Access and management
Earth Engine is available for both [commercial](https://earthengine.google.com/commercial/) and [noncommercial](https://earthengine.google.com/noncommercial/) use. Noncommercial use is offered free of charge, while commercial use is subject to a [subscription fee and compute charges](https://cloud.google.com/earth-engine/pricing). All computation and private data are associated with Google Cloud projects, providing users with control over access, resource management, and usage monitoring through the Google Cloud Console. This integration allows for centralized project management, detailed billing information, and the application of Google Cloud's robust security and compliance features. Users can take advantage of Identity and Access Management (IAM) to [control permissions](https://developers.google.com/earth-engine/cloud/access-control) and can [log activities](https://developers.google.com/earth-engine/guides/audit_logging) and [monitor resource usage](https://developers.google.com/earth-engine/guides/monitoring_usage) with Cloud Monitoring and Cloud Logging.
