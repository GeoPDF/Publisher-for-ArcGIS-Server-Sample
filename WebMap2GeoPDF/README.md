# WebMap2GeoPDF - Basic Web Map to GeoPDF
Code sample that publishes a GeoPDF from a web map in a typical Esri web application.

This is a modification of the existing Esri [Tutorial: Basic web map printing and exporting using arcpy.mapping](http://server.arcgis.com/en/server/latest/publish-services/linux/gp-service-example-basic-high-quality-webmap-printing.htm)

If you have any issues running or deploying this sample service, please reference the link above.  This sample uses a built-in template deployed with ArcGIS Server at the time of this writing.  If you'd like to change the template, update the 'templatePath' in the python component of this sample.

> WebMap2GeoPDF.py (line 31)
___
```javascript
templatePath = r"C:\Program Files\ArcGIS\Server\Templates\ExportWebMapTemplates"
```

## Deploying
It is recommended that 'WebMap2GeoPDF' folder is placed in your 'c:\arcgisserver', or equivalent, folder.  

### Python GeoProcessing Tool
- Create python script tool
  1. Open the **Catalog** window in Arcmap and navigate to the **WebMap2GeoPDF** folder.
  2. Right-click the WebMap2GeoPDF folder and click **New > Toolbox**.
  3. Name the toolbox **WebMap2GeoPDF**.
  4. Right-click the WebMap2GeoPDF toolbox and click **Item Description**.
  5. Click **Edit**.
  6. Enter **geopdf** as a tag and fill Summary and Description with 'WebMap2GeoPDF Sample'.
  7. Click **Save** and exit the **Item Description** dialog box.
  8. Right-click the WebMap2GeoPDF toolbox and click **Add > Script**.
  9. Enter 'WebMap2GeoPDF' for the **Name** and **Label**.
  10. Click **Next**.
  11. **Script File** should be set to the **WebMap2GeoPDF.py** in the python folder for this sample.
  12. Click **Next**.
  12. Add two parameters to the script tool.  
    >(**Note:** Web_Map_as_JSON and Output_File parameter names must be spelled correctly and are case sensitive!)

    - **Web_Map_as_JSON** - INPUT, this parameter takes a JSON representation of the map to be exported.  Set `Data Type=String`.  Make sure the **Parameter Properties**
      `Type=Optional`, and `Direction=Input`
    - **Output_File** - OUTPUT, filename that was exported.  Set `Data Type=File`.  Make sure the **Parameter Properties** 
      `Type=Derived`, and `Direction=Output`
  13. Click *Finish*.
  14. Right-click **WebMap2GeoPDF** script in the toolbox and click **Item Description**.
  15. Click *Edit*.
  16. Enter **geopdf** as a tag, and fill Summary and Usage with **WebMap2GeoPDF**
  17. Scroll down and under **Syntax** click **Web_Map_as_JSON** and enter **JSON** as the **Dialog Explanation**
  18. Click **Save** and exit the **Item Description** dialog box.

#### Execute WebMap2GeoPDF GeoProcessing tool
1. In the **Catalog** window, right-click **WebMap2GeoPDF** script and click **Open**.
2. Click **OK**.  
3. Wait for process to finish.
4. If the task ran successfully, it is ready to be published as a service.  If you received errors, review the steps above and if any changes are required, run the task again.  Please see the [Esri Tutorial](http://server.arcgis.com/en/server/latest/publish-services/linux/gp-service-example-basic-high-quality-webmap-printing.htm) if you're still getting an error.  

#### Publish Service
1. Open the **Results** window (Geoprocessing > Results)
2. Under **Current Session**, right-click **WebMap2GeoPDF** and select **Share As > Geoprocessing Service**
3. Click **Next**.
4. Select the server connection to publish WebMap2GeoPDF service.
5. Click **Next**.
6. Click **Continue**.
6. Click **Publish**.

The geoprocessing service is now ready for the UI.

### UI
The 'ui' folder contains the files needed to display a basic map service in your browser with a 'Print' button which will call WebMap2GeoPDF.  To ensure the button works, we must update the link to the geoprocessing service we created...

> index.html (line 23)
___
```javascript
var printUrl = "http://localhost:6080/arcgis/rest/services/WebMap2GepPDF/GPServer/WebMap2GepPDF";
```

If you deployed the service on a different server or if your environment is set up differently, change the URL above accordingly.  The default **should** work for default installation of ArcGIS Server.  

## Running
Open **ui/WebMap2GeoPDF.html** in your favorite web browser.  You should see a map and a 'Print' button.  