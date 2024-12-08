#def test_function():
#def inner_function():
        #print(" Я области видимости функции test_function")#Вне функции выдает ошибку

def test_function():
    def inner_function():
        print(" Я области видимости функции test_function")
    inner_function() # Вызывает вложенную функцию


test_function()  # Выводит результат вызова на экран

