import requests 
import pandas as pd

#openweathermap
API_KEY = "################################"

city = "Cairo"
#ارسال دولة لمعرفة طقسها, ارسال API KEY, ارسال وحدة قياس اللي هي سيليسيون
params ={
    "q":city,
    "appid":API_KEY,
    "units":"metric"
}

#طلب مع Params
r = requests.get("http://api.openweathermap.org/data/2.5/weather",params=params)

# معرفة طلب ب json
try:
    r.raise_for_status()
    data = r.json()
except  Exception as e:
    print("This is woring",e)
    exit()

#استخراج معلومات

#استخراج درجة الحراره
temp = data['main']["temp"]

#استخراج الرطوبه
humidity = data ["main"]["humidity"]

#استخراج حالة الجو
description = data["weather"][0]["description"]

#طباعة الستخراجات
print(f"Temp: {temp}°C")
print(f"Humidity: {humidity}%")
print(f"Discription: {description}")

#حفظ البيانات في excel
df = pd.DataFrame([{
    "City":city,
    "Temperature (°C)": temp,
    "Humidity (%)":humidity,
    "Desctiption":description
},
{
    "City":"Mansoura"
}])

df.to_excel("weather_data.xlsx",index=False)





#في تشات  تعلم requests محلل بيانات
#في مشروع في الاول خلصنا ولكن محتاجين نراجع و نحسنه
# اعرف اللي المفرود نفهمه