print('''Практична робота №3. Завдання 3
Спітковська Владислава. Прикладна математика
''')
string1 = str(input("Ввести :"))
string2 = str(input("Ввести :"))
import pandas as pd
df1 = []
df2 = []
len1 = len(string1)
len2 = len(string2)
pattern = len1 == len2
i = 0
j = i + 1
len1_char = len1[i]
len2_char = len2[i]
is_len1_char_found = box.__contains__(len1_char)
is_len2_char_found = box.__contains__(len2_char)
box = str("")
for sym1 in range(i) and sym2 in range(j):
    while j <= len1-1 and pattern:
        if string1(i) == string1(j):
            if j is not is_len1_char_found:
                df1.append([j])
                box = box + [j]
                j = j+1
            elif string1(i) != string1(j):
                j = j+1
            else:
                i = i+1
                j = i+1
for sym1 in range(i) and sym2 in range(j):
    while j <= len2 - 1:
        if string2(i) == string2(j):
            if j is not is_len2_char_found:
                df2.append([j])
                box = box + [j]
                j = j + 1
            elif string2(i) != string2(j):
                j = j + 1
            else:
                i = i + 1
                j = i + 1

recognise = df1 == df2
print(recognise)