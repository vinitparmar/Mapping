import folium

map = folium.Map(location=[28.70, 77.10],zoom_start=6,titles="Stamen Terrain")

map.save("Map.html")