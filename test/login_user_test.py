import random

from utils.data_utils import generate_string_data
from utils.user_api import UserApi


class TestLoginUser(UserApi):
    email = f"{generate_string_data(random.randrange(4, 15))}@{generate_string_data(random.randrange(4, 15))}.com"
    password = f"{generate_string_data(random.randrange(6, 15))}"
    invalid_email_string = 'A valid email address is required'
    invalid_password_string = 'Password must be between 6 and 30 characters'
    incorrect_password_string = 'Incorrect email address or password'

    def test_user_login(self, default_user):
        assert default_user['success'] is True
        assert default_user['status'] == 200
        assert default_user['message'] == 'Login successful'
        assert default_user['data']['name'] == 'tester'
        assert default_user['data']['email'] == 'a@example.com'

    def test_invalid_email(self):
        email_vals = ['', 'invalid', 'test@', 'test.com']
        for email in email_vals:
            payload = {
                "email": email,
                "password": self.password
            }

            resp = self.login_user('login', payload)

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == self.invalid_email_string

    def test_invalid_password(self):
        password_vals = ['', 'abcde', generate_string_data(random.randrange(31, 35))]
        for password in password_vals:
            payload = {
                "email": self.email,
                "password": password
            }

            resp = self.login_user('login', payload)

            assert resp['success'] is False
            assert resp['status'] == 400
            assert resp['message'] == self.invalid_password_string

    def test_incorrect_password(self):
        payload = {
            "email": self.email,
            "password": 'incorrectPassword'
        }

        resp = self.login_user('login', payload)

        assert resp['success'] is False
        assert resp['status'] == 401
        assert resp['message'] == self.incorrect_password_string
