import folium
import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context
sitesR = pd.read_json("https://pwbroad.kcg.gov.tw/pwbmis/OpenDataProjectScope.aspx").set_index("流水碼")

kaoMap = folium.Map([22.983332, 120.577106], zoom_start=9)

#為了讓地圖知道要縮放的範圍，所以建立一個bounds儲存所有點位的座標
bounds = []
for site in sitesR.values:
    name = site[2]
    #建立locations陣列，儲存各範圍polygon所有座標點位。
    #換一個範圍就要先清空，所以建在這邊
    locations = []
    # 每一點位的polygon座標list。因為有的位置有兩個以上的範圍，這邊要先將每個範圍獨立開來。
    for rs in site[1]:
        siteLocations = rs.split(',')
        for siteLatLng in siteLocations:
            latlng = siteLatLng.split(' ')
            local = [float(latlng[0]), float(latlng[1])]
            locations.append(local)
            bounds.append(local)
        #抓到該範圍所有點後，建立polygon
        #需folium 0.6.0以上才會有polygon可以使用
        folium.Polygon(
            locations=locations,
            color='blue',
            weight=1,
            fill_color='#ffa',
            fill_opacity=0.1,
            fill=True,
            popup= name,
            tooltip='取得工程資訊',
        ).add_to(kaoMap)
#將bounds建立polygon並利用.get_bounds()取得視圖範圍，進而設定地圖的縮放範圍
bLayer = folium.Polygon(locations = bounds)
kaoMap.fit_bounds(bLayer.get_bounds())
#將地圖存成html檔
kaoMap.save('PWBsites.html')