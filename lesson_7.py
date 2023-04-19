#функция/Задание 2: написать программу для вычисления факториала. Факториал - 1 * 2 * 3 ... * n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Enter the number"))
print(factorial(n))
#функция/Задача 8: написать функцию, которая принимает в себя время в виде "HH:mm:ss" и считает, сколько всего секунд
def time_to_seconds(time):
    h,m,s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s
time = input("Enter the time 'HH:mm:ss'")
seconds = time_to_seconds(time)
print(seconds)
#декоратор/Задача 3: написать декоратор, который проверяет все аргументы функции и выполняет функцию только в случае если все они больше 0, иначе выводит сообщение об ошибке
def check_args(func):
    def wrapper(*args):
        if all(i > 0 for i in args):
            return func(*args)
        else:
            return ValueError("All arguments must be greater than 0!")
    return wrapper
@check_args
def func(a, b):
    return a / b
result = func(1,0)
print(result)
#декоратор/Задача 4: написать декоратор для функции, который добавляет 1 к каждому целочисленному агрументу:
def add_one(func):
    def wrapper(*args):
        args = [i + 1 if isinstance(i, int) else i for i in args]
        return func(*args)
    return wrapper
@add_one
def func(*args):
    return args
result = func(1, 2, 3, "string")
print(result)