# Уровень 1.
# Создайте класс StringVar для работы со строковым типом данных,
# содержащий методы set() и get(). Метод set() служит для изменения
# содержимого строки, get() – для получения содержимого строки. Создайте
# объект типа StringVar и протестируйте его методы.

class StringVar:

    def __init__(self, string):
        self.string = string

    def set(self, string):
        self.string = string
        return self.string

    def get(self):
        return self.string

s = StringVar(input('Введите значение: '))
print(s.get())
print(s.set('Привет'))