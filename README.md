# 🔌 ESP32 MicroPython Basics | نمونه‌های پایه‌ی مایکروپایتون برای ESP32

دو اسکریپت آموزشی و پایه برای شروع کار با **MicroPython** روی بردهای ESP32/ESP8266.

---

## 📄 فایل‌ها

### 1️⃣ `hello_world.py` — چشمک‌زن LED (Blink)

ساده‌ترین برنامه‌ی ممکن برای تست یک برد جدید: یک LED روی پین ۲۵ رو هر ۱ ثانیه روشن و خاموش می‌کنه.

**کاربرد:** اولین تستی که معمولاً روی هر برد جدید اجرا می‌شه تا مطمئن بشی MicroPython درست نصب شده و پین‌ها کار می‌کنن. (معادل «Hello World» در دنیای سخت‌افزار!)

```python
import machine
import utime

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
```

> 🔧 روی بعضی بردها (مثل ESP32 DevKit) پین ۲۵ به LED روی برد وصل نیست؛ در اون صورت باید عدد پین رو با LED آنبورد برد خودت (معمولاً `2`) عوض کنی.

---

### 2️⃣ `wifi_accesspoint.py` — اسکنر شبکه‌های Wi-Fi

تمام شبکه‌های Wi-Fi اطراف رو اسکن می‌کنه و اسم (SSID)، کانال و قدرت سیگنال هرکدوم رو چاپ می‌کنه.

**کاربرد:** قدم اول برای هر پروژه‌ای که نیاز به اتصال Wi-Fi داره (مثلاً وب‌سرور، ارسال داده به کلاود، و...) — قبل از اتصال، باید بدونی چه شبکه‌هایی در دسترسن.

```python
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("در حال اسکن شبکه‌های Wi-Fi...\n")
access_points = wlan.scan()

for ap in access_points:
    ssid, bssid, channel, rssi, authmode, hidden = ap
    ssid_name = ssid.decode("utf-8") if ssid else "(پنهان)"
    print("SSID: {:<25} | کانال: {:<3} | سیگنال: {} dBm".format(ssid_name, channel, rssi))
```

---

## 🧰 سخت‌افزار مورد نیاز

- برد ESP32 یا ESP8266 با فرم‌ور MicroPython نصب‌شده
- برای `hello_world.py`: یک LED (یا استفاده از LED آنبورد برد)
- برای `wifi_accesspoint.py`: چیز اضافه‌ای لازم نیست، فقط ماژول Wi-Fi داخلی برد

---

## ⚙️ نصب و اجرا

1. فرم‌ور MicroPython رو روی برد نصب کن (با `esptool`)
2. فایل مورد نظر رو با **Thonny** یا **ampy** روی برد آپلود کن
3. اجرا کن و نتیجه رو ببین (چشمک LED یا لیست شبکه‌ها در Serial Monitor)

---

## 📝 مجوز

MIT License — آزاد برای استفاده، تغییر و توزیع.
