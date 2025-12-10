def ask_for_age():
    age = int(input("Введите ваш возраст: "))
    if age >= 18:
        print("Вы совершеннолетний")
    else:
        print("Вы несовершеннолетний")

def check_password():
    password = input("Введите пароль: ")
    if password == "secret":
        print("Пароль верный")
    else:
        print("Пароль неверный")

def check_temperature():
    temperature = float(input("Введите температуру в градусах: "))
    if temperature < 15:
        print("Холодно")
    elif 15 <= temperature <= 25:
        print("Тепло")
    else:
        print("Жарко")


def check_login_and_password():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login == "admin" and password == "password123":
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")

if __name__ == '__main__':
    ask_for_age()
    check_password()
    check_temperature()
    check_login_and_password()
