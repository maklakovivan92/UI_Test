import random

def generate_email():
    name = random.randint(100, 999)
    domain = random.choice(["gmail.com", "yandex.ru", "mail.ru"])
    return f"ivan_maklakov_46_{name}@{domain}"

def generate_valid_password():
    password = random.randint(100000, 999999)
    return password

def generate_invalid_password():
    password = random.randint(10000, 99999)
    return password
