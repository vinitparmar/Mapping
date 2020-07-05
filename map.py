import folium
import pandas

# reading the data form the file
data =  pandas.read_csv("datafiles/Volcanoes.txt")
lat =  list(data["LAT"])
lon =  list(data["LON"])
elev = list(data["ELEV"])
# lands on the lat long location on load of the page 
map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="OpenStreetMap")
# adds the marker at the location with pop up
fg = folium.FeatureGroup(name="My Map")

# color producer function
def color_producer(ele):
    if(ele <= 1000): return 'green'
    if(ele > 1000 and ele <= 3000): return 'orange'
    if(ele > 3000): return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+" m",color='grey',radius =6,fill_color=color_producer(el),fill_opacity=0.7))

map.add_child(fg)
map.save("Map.html")