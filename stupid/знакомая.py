n = int(input())    #n - число
counter = 0     #счетчик
for i in range (n): #повторяем n раз
    x = input() #x не число, а строка 
    if len(x) == 3: #если эта строка длинной в 3 символа,
        last = x[-1] #последний символ строки
        if last == '4':    #и если последний символ - 4,
            counter = counter + 1 #мы увеличиваем счетчик на 1
print (counter)
