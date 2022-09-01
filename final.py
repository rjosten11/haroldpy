from folium.map import Marker
import folium
map = folium.Map(location=[9.122193, 125.537603] ,zoom_start=13)

Markerr = {
    0 : {"location": [9.11911, 125.538875,], "popup" : "<img src='https://m.facebook.com/cbrupdates/photos/see-you-all-sa-opening-tomorrow-guys-christmaswithjollibee/1694852323899351/'alt='width='300' height='200'", "tooltip": "Cabadbaran Jollibee Drive Thru", "name": "Restaurant"},
    1 : {"location": [9.12130, 125.5381070,], "popup" : "<img src='https://restaurantguru.com/Gen-Tuna-Sutukil-Cabadbaran-City-2'alt='width='300' height='200'", "name": "Restaurant"},
    2 : {"location": [9.123820, 125.5379030,], "popup" : "<img src='http://cabadbaranadn.gov.ph/cbr/index.php/2019/07/27/7-eleven-is-finally-open/'alt='width='300' height='200'", "tooltip": "Seven11", "name": "Convenience Store"},
}

for x in range(len(Markerr)):
  folium.Marker(
      Markerr[x]['location'],
      popup=Markerr[x]['popup'],
      tooltip=Markerr[x]['tooltip']
  ).add_to(map)

#Path
folium.GeoJson("/content/drive/MyDrive/GeoJson/newmap.geojson", 
               name="Path", tooltip=folium.GeoJsonTooltip(['stroke']),
               style_function = lambda x: {'color': x['properties']['stroke'], 'weight': x['properties']['stroke-width']}).add_to(map)
#School
folium.GeoJson("/content/drive/MyDrive/GeoJson/churchesmap.geojson",
               name="School Boundaries",
               style_function= lambda x: BordersStyle,
               tooltip=folium.GeoJsonTooltip(['stroke']) ) .add_to(map) 


folium.LayerControl().add_to(map)

BordersStyle = {
    'color' : 'red',
    'weight': 5,
    'fillcolor': 'green',
    'fillopacity': 0.3

}
map
#map.save('/content/drive/MyDrive/Class Files/GE 124/index.html')