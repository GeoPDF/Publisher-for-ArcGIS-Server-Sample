"""
WebMap2GeoPDFScript.py
This creates a GeoPDF document given a JSON description of a web 
map. This code conforms with the signature required for the Esri 
Web API Print object.

Copyright 2015 TerraGo Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
import uuid
import arcpy
import pubpy.geopdf_export.api as pubpy_ex

# Input WebMap json
Web_Map_as_JSON = arcpy.GetParameterAsText(0)

# The template location (installed with ArcGIS Server)
templatePath = r"C:\Program Files\ArcGIS\Server\Templates\ExportWebMapTemplates"
templateName = r"Letter ANSI A Portrait"
templateMxd = os.path.join(templatePath, (templateName + ".mxd"))
   
# Convert the WebMap to a map document
result = arcpy.mapping.ConvertWebMapToMapDocument(
	Web_Map_as_JSON, templateMxd)
mapDoc = result.mapDocument

# Use the uuid module to generate a GUID as part of the output name
# This will ensure a unique output name
temp_filename = 'WebMap_{}.pdf'.format(str(uuid.uuid1()))
Output_File = os.path.join(arcpy.env.scratchFolder, temp_filename)
arcpy.AddMessage('Output PDF path: {0}'.format(Output_File))

# Export the WebMap to GeoPDF
pubpy_ex.ExportToGeoPDF(mapDoc, Output_File)

# set Output_File
arcpy.SetParameterAsText(1, Output_File)

# Clean up - delete the map document reference
filePath = mapDoc.filePath
del mapDoc, result
os.remove(filePath)
