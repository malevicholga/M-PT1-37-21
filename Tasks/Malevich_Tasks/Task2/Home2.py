from datetime import datetime

p = input('Введи время в формате HH:MM \n')
t_ent = p.split(':')
h = int(t_ent[0])
m = int(t_ent[1])

a = {0: 'двенадцать', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'один', 14: 'два', 15: 'три', 16: 'четыре', 17: 'пять', 18: 'шесть', 19: 'семь', 20: 'восемь', 21: 'девять', 22: 'десять', 23: 'одиннадцать'}

b = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвертого', 5: 'пятого', 6: 'шестого', 7: 'седьмого', 8: 'восьмого', 9: 'девятого', 10: 'десятого', 11: 'одиннадцатого', 12: 'двенадцатого', 13: 'первого', 14: 'второго', 15: 'третьего', 16: 'четвертого', 17: 'пятого', 18: 'шестого', 19: 'седьмого', 20: 'восьмого', 21: 'девятого', 22: 'десятого', 23: 'одиннадцатого', 0: 'двенадцатого'}

c = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'четверть', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 21: 'двадцать одна', 22: 'двадцать две', 23: 'двадцать три', 24: 'двадцать четыре', 25: 'двадцать пять', 26: 'двадцать шесть', 27: 'двадцать семь', 28: 'двадцать восемь', 29: 'двадцать девять', 30: 'половина', 31: 'тридцать одна', 32: 'тридцать две', 33: 'тридцать три', 34: 'тридцать четыре', 35: 'тридцать пять', 36: 'тридцать шесть', 37: 'тридцать семь', 38: 'тридцать восемь', 39: 'тридцать девять', 40: 'двадцати', 41: 'девятнадцати', 42: 'восемнадцати', 43: 'семнадцати', 44: 'шестнадцати', 45: 'четверти', 46: 'четырнадцати', 47: 'тринадцати', 48: 'двенадцати', 49: 'одиннадцати', 50: 'десяти', 51: 'девяти', 52: 'восьми', 53: 'семи', 54: 'шести', 55: 'пяти', 56: 'четырех', 57: 'трех', 58: 'двух', 59: 'одной'}

d = {0: 'часов', 1: 'час', 13: 'час', 2: 'часа', 3: 'часа', 4: 'часа', 14: 'часа', 15: 'часа', 16: 'часа'}

e = {0: 'минут', 1: 'минута', 2: 'минуты', 3: 'минуты', 4: 'минуты', 21: 'минута', 22: 'минуты', 23: 'минуты', 24: 'минуты', 31: 'минута', 32: 'минуты', 33: 'минуты', 34: 'минуты', 59: 'минуты'}

s = {0: 'ровно', 1: 'без', 30: 'половина', 45: 'без четверти'}
print('Введенное время: ')

if 0 < m < 39 and m != 30:
    if m in range(1, 5) or m in range(21, 25) or m in range(31, 35):
        print(c[m], e[m], b[h+1])
    else:
        print(c[m], e[0], b[h+1])
elif m == 30:
    print(s[m], b[h+1])
elif 40 <= m <= 59:
    if m in range(40, 59):
        print(s[1], c[m], e[0], a[h+1])
    else:
        print(s[1], c[m], e[m], a[h+1])
elif m == 45:
    print(s[m], a[h+1])
else:
    if h == 1 or h == 13 or h in range(2, 5) or h in range(14, 17):
        print(s[m], a[h], d[h])
    else:
        print(s[m], a[h], d[0])

time_now = datetime.now()
print("Текущее время: ")
h_s = time_now.hour
m_s = time_now.minute

if 0 < m_s < 39 and m_s != 30:
    if m_s in range(1, 5) or m_s in range(21, 25) or m_s in range(31, 35):
        print(c[m_s], e[m_s], b[h_s+1])
    else:
        print(c[m_s], e[0], b[h_s+1])
elif m_s == 30:
    print(s[m_s], b[h_s+1])
elif 40 <= m_s <= 59:
    if m_s in range(40, 59):
        print(s[1], c[m_s], e[0], a[h_s+1])
    else:
        print(s[1], c[m_s], e[m_s], a[h_s+1])
elif m_s == 45:
    print(s[m_s], a[h_s+1])
else:
    if h_s == 1 or h_s == 13 or h_s in range(2, 5) or h_s in range(14, 17):
        print(s[m_s], a[h_s], d[h_s])
    else:
        print(s[m_s], a[h_s], d[0])