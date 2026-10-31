import requests
import random
import string

def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

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

def creds_for_register_all_fields():
    letters = string.ascii_lowercase

    login = ''.join(random.choice(letters) for i in range(10))
    password = ''.join(random.choice(letters) for i in range(10))
    first_name = ''.join(random.choice(letters) for i in range(10))

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

def creds_for_register_only_required_fields():
    letters = string.ascii_lowercase

    login = ''.join(random.choice(letters) for i in range(10))
    password = ''.join(random.choice(letters) for i in range(10))

    payload = {
        "login": login,
        "password": password
    }
    return payload

def return_id_after_login():
    user = register_new_courier_and_return_login_password()
    payload = {
        'login': user[0],
        'password': user[1]
    }

    response = requests.post("https://qa-scooter.education-services.ru/api/v1/courier/login", data=payload)
    r = response.json()

    return r['id']