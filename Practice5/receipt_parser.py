import re
import json

# читаем файл raw.txt
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ---------- 1. Найти все цены ----------
price_pattern = r"\d[\d\s]*,\d{2}"   # числа вида 308,00 или 1 200,00
prices = re.findall(price_pattern, text)

# ---------- 2. Найти названия товаров ----------
# товар идет после номера "1." "2." и до строки с количеством
product_pattern = r"\d+\.\s*\n(.+)"
products = re.findall(product_pattern, text)

# ---------- 3. Найти дату и время ----------
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)

date_time = datetime_match.group() if datetime_match else None

# ---------- 4. Найти метод оплаты ----------
payment_pattern = r"(Наличные|Банковская карта)"
payment_match = re.search(payment_pattern, text)

payment_method = payment_match.group() if payment_match else None

# ---------- 5. Найти итоговую сумму ----------
total_pattern = r"ИТОГО:\s*\n?([\d\s]+,\d{2})"
total_match = re.search(total_pattern, text)

total = total_match.group(1) if total_match else None

# ---------- 6. Создать структурированный вывод ----------
data = {
    "products": products,
    "prices": prices,
    "total": total,
    "payment_method": payment_method,
    "date_time": date_time
}

# вывод в JSON формате
print(json.dumps(data, indent=4, ensure_ascii=False))