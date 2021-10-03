# имя, фамилия, год рождения, город проживания, email, телефон

def users_info(name, surname, birth_year, city, email, phone):
    print(f"User {name} {surname} with birth year {birth_year} lives in {city}. Contacts: phone - {phone}, email - {email}")


users_info(name="Svetlana", surname="Shakurova", birth_year=2000, city="Moscow", email="shakurovas@bk.ru", phone="+7(951)9547603")
