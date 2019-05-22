def printMax(x, y):

    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми числами.'''

    x = int(x) # конвертируем в целые, если возможно
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')
printMax(3, 5)
print(printMax.__doc__)

'''Строка в первой логической строке функции является строкой документации для этой функции. 
Обратите внимание на то, что строки документации применимы также к модулям и классам, 
о которых мы узнаем в соответствующих главах. Строки документации принято записывать в форме многострочной строки,
где первая строка начинается с заглавной буквы и заканчивается точкой. Вторая строка оставляется пустой, 
а подробное описание начинается с третьей. Вам настоятельно рекомендуется следовать такому формату 
для всех строк документации всех ваших нетривиальных функций.'''