import re

# 1. строка: 'a' + 0 или больше 'b'
s = "abbb"
print(bool(re.fullmatch(r"ab*", s)))  # True если подходит


# 2. строка: 'a' + 2 или 3 'b'
s = "abb"
print(bool(re.fullmatch(r"ab{2,3}", s)))


# 3. найти lowercase слова с _
text = "hello_world test_value Hello_World"
print(re.findall(r"[a-z]+_[a-z]+", text))


# 4. одна большая буква + маленькие
text = "Hello World from Python"
print(re.findall(r"[A-Z][a-z]+", text))


# 5. 'a' потом что угодно и заканчивается 'b'
s = "axxxb"
print(bool(re.fullmatch(r"a.*b", s)))


# 6. заменить пробел , . на :
text = "Hello, world. Python is good"
print(re.sub(r"[ ,\.]", ":", text))


# 7. snake_case → camelCase
s = "snake_case_string"
parts = s.split("_")
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print(camel)


# 8. split по большим буквам
s = "HelloWorldPython"
print(re.split(r"(?=[A-Z])", s))


# 9. добавить пробел перед большой буквой
s = "HelloWorldPython"
print(re.sub(r"([A-Z])", r" \1", s).strip())


# 10. camelCase → snake_case
s = "camelCaseString"
print(re.sub(r"([A-Z])", r"_\1", s).lower())