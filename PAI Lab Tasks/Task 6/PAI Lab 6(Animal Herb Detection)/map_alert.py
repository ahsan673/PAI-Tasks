import folium  # type: ignore
import webbrowser
from datetime import datetime

def send_map_alert():
    lat, lon = 28.6139, 77.2090
    m = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker(
        [lat, lon],
        popup=f"Herd Detected @ {datetime.now().strftime('%H:%M:%S')}",
        icon=folium.Icon(color='red')
    ).add_to(m)

    m.save('herd_alert_map.html')
    webbrowser.open('herd_alert_map.html')
