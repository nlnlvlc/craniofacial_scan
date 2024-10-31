# 3D Scanning Craniofacial Features for Quick Physical Interface Prototyping

Coming Soon!

## Project Description

Currently, there doesn’t exist an accessible tool to collect and analyze craniofacial landmarks
amongst different groups. Modern tools include MRI and CT scanning, which require extensive
room, medical knowledge & expertise, access to medical facilities, as well as substantial financial
resources. In areas where access to these devices is available, a slew of factors, such as
ethnic/racial homogeneity and socioeconomic thresholds, severely limit the population sample
size included in testing.
This project intends to do three things:
1. Build a 3D scanner which can be used to scan faces using an iPad Pro’s LiDAR scanning
capabilities
2. Apply a mesh to the scan which can be used to identify a collection of craniofacial
landmarks based on the size and geometry of the head scan
3. Use the most prominent landmarks to check against a range of anthropometrics to ensure
the scan shows a with likely proportions (ex. Checking that the Interpupillary Distance isn’t
smaller than the max width of the scanned nasal features)

Where getting something of this accuracy currently requires expensive equipment or detailed
manual manipulation of a handmade 3D digital model, the successful completion of this project
could help create accessible and quick options for early prototyping.

## References:

* [Face Recognition from Facial Surface Metric](https://link.springer.com/chapter/10.1007/978-3-540-24671-8_18)
* [3D Scanning for Personal 3D Printing:
Build Your Own Desktop 3D Scanner](http://mesh.brown.edu/desktop3dscan/)
* [3D Reconstruction for Featurless Scenes with Curvature Hints](https://youtu.be/PrUVo3potl4?si=7t_f9_MH8kkonLsp) 
* [How effective are landmarks and their geometry for face recognition?](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6890f210cdc574caa89fa94933ec942360aa1e0c)
* [A landmark-based data-driven approach on 2.5D facial attractiveness computation](https://www.sciencedirect.com/science/article/abs/pii/S0925231217301248)
* [Emotion Recognition using Spatiotemporal Features from Facial Expression Landmarks](https://www.researchgate.net/figure/Example-of-face-and-landmarks-detection-and-the-Delaunay-triangulation-to-form-a-mesh_fig1_328676113)
* [Morphometric approach to 3D soft-tissue craniofacial analysis and classification of ethnicity, sex, and age](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0228402)
* [Modelling 3D craniofacial growth trajectories for population comparison and classification illustrated using sex-differences](https://www.nature.com/articles/s41598-018-22752-5)

## Timeline:

| Week | Tasks |
| --- | --- |
| ~~**Week 5 - 7:**~~ | ~~Setup/Build Scanning Setup. If not possible to use iPad Pro LiDAR, other camera options which allow use for depth sensing can be used~~ |
| ~~**Week 8:**~~ | ~~Test scanner on multiple face and object samples; make requires changes and identify parameters for distance and placement to ensure consistency~~ |
| **Week 10:** | Implement IR LiDAR Point Cloud Stream & Make Exportable; Delauney and Ball Pivoting w/ sample Point Clouds |
| **Week 11 - 13:** | Test of Delauney and Ball Pivoting w/ Exported Point Cloud; Attempt Python Integration with iOS App |
| **Week 14 - 15:** | Create website, put together findings, record demo |
