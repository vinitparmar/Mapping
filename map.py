import folium
import pandas

# reading the data form the file
data =  pandas.read_csv("datafiles/Volcanoes.txt")
lat =  list(data["LAT"])
lon =  list(data["LON"])
# lands on the lat long location on load of the page 
map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="OpenStreetMap")
# adds the marker at the location with pop up
fg = folium.FeatureGroup(name="My Map")

# for coordinates in [[28.40,77.58],[28.80,77.98]]:
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln],popup="hi ..i am a marker",icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map.html")