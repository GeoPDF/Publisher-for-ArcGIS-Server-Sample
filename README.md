TerraGo Publisher for ArcGIS Sample Code
========================================

# Building applications with TerraGo Publisher for ArcGIS
TerraGo Publisher for ArcGIS (Publisher) is an extension of ArcGIS that allows creation of GeoPDF documents. Publisher can be automated and extended using PubPy, allowing for integration of Publisher functionality in ArcGIS geoprocessing toolboxes, ArcGIS for Server applications, etc.

# What is PubPy?
PubPy is [ArcPy](https://arcpy.wordpress.com/ "Esri's ArcPy blog")-compatible Python extensions for TerraGo Publisher for ArcGIS. With PubPy, you can automate the creation of GeoPDF documents as well as integrate Publisher capabilities into ArcGIS for Server implentations. The design of PubPy closely follows that of ArcPy, so if you know ArcPy, PubPy should come easily. More documentation and tutorials can be found on the [PubPy support page](http://www.terragotech.com/geopdf-support/pubpy).

# Samples
This repo contains samples for different applications of PubPy and supporting files for the implementation of ArcGIS for Server applications which leverage Publisher. All samples are open source and available under the Apache 2.0 license. Use and modification is encouraged.

## MXD2GeoPDF: Create a GeoPDF document from an MXD
Creating a GeoPDF from an MXD is as simple as:

    from pubpy.geopdf_export.api import ExportMXDToGeoPDF
    ExportMXDToGeoPDF("my.mxd", "geo.pdf")

from the Python window inside of ArcMap. This theme is expanded upon in the sample [MXD2GeoPDF.py](./MXD2GeoPDF/MXD2GeoPDF.py) which is a command-line utility for creating GeoPDF documents from extant MXDs. You don't need to open ArcMap to make a GeoPDF map!

## WebMap2GeoPDF: Create GeoPDF document from an ArcGIS web map
See: [README](./WebMap2GeoPDF/README.md)