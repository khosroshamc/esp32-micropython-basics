import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("در حال اسکن شبکه‌های Wi-Fi...\n")
access_points = wlan.scan()

for ap in access_points:
    ssid, bssid, channel, rssi, authmode, hidden = ap
    ssid_name = ssid.decode("utf-8") if ssid else "(پنهان)"
    print("SSID: {:<25} | کانال: {:<3} | سیگنال: {} dBm".format(ssid_name, channel, rssi))
