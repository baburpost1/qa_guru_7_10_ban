from pages.registration_page import RegistrationPage
from models.User import User


def test_registration_students_form_positive():
    registration_page = RegistrationPage()
    yasha = User(first_name='yasha', last_name='family', email='qwerty@mail.ru', gender=1, mobile="8800555353",
                 year="2000", month="5", day="1",
                 subjects='Math', hobbies='2', picture='../data/test.png',
                 address="CUrrent aDDress 12a Here", state="NCR", city="Delhi")
    registration_page.registration_user(yasha)
    registration_page.press_submit()

    #     Проверка итоговой таблицы
    registration_page.should_have_registered(full_name=f"{yasha.first_name} {yasha.last_name}",
                                             email=yasha.email, gender='Male', mobile=yasha.mobile,
                                             date_of_birth='01 June,2000',
                                             subjects='Maths', hobbies="Reading",
                                             picture="test.png", address=yasha.address,
                                             state_and_city=f"{yasha.state} {yasha.city}")
