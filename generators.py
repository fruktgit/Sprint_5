from faker import Faker

fake = Faker()

def generate_email():
    """Генерирует уникальный email в формате имя_фамилия_номер@домен"""
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    cohort_number = fake.random_int(min=1, max=999)  # Номер когорты
    unique_suffix = fake.random_int(min=100, max=999)  # Уникальные 3 цифры
    domain = fake.free_email_domain()
    return f"{first_name}_{last_name}_{cohort_number}_{unique_suffix}@{domain}"

def generate_password(length=8):
    """Генерирует пароль с использованием Faker"""
    return fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)

def generate_password_wrong(length=5):
    """Генерирует пароль с использованием Faker"""
    return fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)

class PersonData:
    user_name = 'Viktor'
    login = 'Viktor@test.ru'
    password = '12343212'