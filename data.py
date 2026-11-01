from conftest import delete_courier

black_colour_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}

gray_colour_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["GRAY"]
}

no_colour_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}

both_colours_order = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK", "GRAY"]
}

register_existing_courier_message = 'Этот логин уже используется. Попробуйте другой.'
register_not_all_fields_message = 'Недостаточно данных для создания учетной записи'
login_not_all_fields_message = 'Недостаточно данных для входа'
login_invalid_data_message = 'Учетная запись не найдена'
delete_courier_without_id_message = 'Not Found.'
delete_courier_invalid_id_message = 'Курьера с таким id нет.'