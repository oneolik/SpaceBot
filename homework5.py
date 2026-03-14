import requests

url = "https://wttr.in/Невинномысск"

# задаём параметры запроса
weather_parameters = {
    "format": "j1",   # получить данные в JSON
    "lang": "ru"      # язык русский
}

# отправляем запрос
response = requests.get(url, params=weather_parameters)
data = response.json()

# январь – первые 31 день
january = [float(day["hourly"][0]["precipMM"]) for day in data["weather"][:31]]

# февраль – следующие 28 дней
february = [float(day["hourly"][0]["precipMM"]) for day in data["weather"][31:59]]

# март – следующие 31 дней
march = [float(day["hourly"][0]["precipMM"]) for day in data["weather"][59:90]]


# считаем суммы
sum_jan = sum(january)
sum_mar = sum(march)

# сравниваем и выводим
if sum_jan > sum_mar:
    print("В январе выпало больше осадков:", sum_jan, "мм")
elif sum_mar > sum_jan:
    print("В марте выпало больше осадков:", sum_mar, "мм")
else:
    print("В январе и марте выпало одинаковое количество осадков:", sum_jan == sum_mar, "мм")