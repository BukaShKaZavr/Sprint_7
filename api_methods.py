import allure
import requests
import helpers

@allure.step('Регистрируем нового курьера и возвращаем его логин и пароль')
def register_new_courier_and_return_login_password():
    login_pass = []

    login = helpers.generate_random_strings(10)
    password = helpers.generate_random_strings(10)
    first_name = helpers.generate_random_strings(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.education-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass

@allure.step('Авторизируем курьера и возвращаем его id')
def return_id_after_login():
    user = register_new_courier_and_return_login_password()
    payload = {
        'login': user[0],
        'password': user[1]
    }

    response = requests.post("https://qa-scooter.education-services.ru/api/v1/courier/login", data=payload)
    r = response.json()

    return r['id']