**Project to test plotting lat and lon values in Django using Leaflet.** 

*Notes*  
* I'm using a basic OpenStreetMap here, there are many templates available with different styles.
* Leaflet requires the gdal package. 
  * GDAL_LIBRARY_PATH and GEOS_LIBRARY_PATH defined in settings.py.
  * Paths will likely be different when deploying to server, I also needed to remove gdal from requirements and install a separate version

*Sample observations*
* L'Industrie Pizza Lat 40.7382 Lon -74.0055
* Brooklyn Bridge Lat 40.706086 Lon -73.996864

*Image of map rendered*

<img width="1156" alt="Screenshot 2025-05-25 at 6 22 38 PM" src="https://github.com/user-attachments/assets/b0d0a51a-0777-4ad6-9dfb-4f0763dbc347" />
