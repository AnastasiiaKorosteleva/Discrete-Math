__author__ = 'anastasiiakorosteleva'
s = [2,4,8,1,3,9,5,7,6]

new = []
for j in range(0, len(s)):
    m = 0 #индекс первого элемента
    i = 1 #индекс второго элемента
    while i < len(s): #пока индекс меньше длины строки
        if s[i] < s[m]: # если значение под индексом i меньше, чем под m,
            m = i # то присвоить m индекс i
        i += 1 # увеличить i на единицу

    new.append(s[m])
    s.remove(s[m])

print(new)