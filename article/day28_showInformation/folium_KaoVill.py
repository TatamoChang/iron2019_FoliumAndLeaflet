import folium

myMap = folium.Map([22.73444963475145, 120.28458595275877], zoom_start=14)

kaoDistrict = folium.GeoJson('../../dist/mapdata/KaoVillageRange.json')

kaoDistrict.add_to(myMap)
myMap.fit_bounds(kaoDistrict.get_bounds())
myMap.save('Folium_KaoVill.html')