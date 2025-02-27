import random
import allure

from notes_api.conftest import base_api
from notes_api.utils.data_utils import generate_string_data, generate_number_data
from notes_api.utils.user_api import UserApi


class TestUpdateUserProfile(UserApi):
    profile_endpoint = 'users/profile'

    @allure.feature('update_user_profile')
    def test_update_user_name(self, update_user):
        updated_name = generate_string_data(random.randrange(4, 15))
        updated_phone = generate_number_data(random.randrange(8, 20))
        updated_company = generate_string_data(random.randrange(4, 15))
        payload = {
            'name': updated_name,
            'phone': updated_phone,
            'company': updated_company
        }

        resp = self.update_user_profile('profile', payload, update_user['data']['token'], base_api=base_api)

        assert resp['success'] is True
        assert resp['status'] == 200
        assert resp['message'] == 'Profile updated successful'
        assert resp['data']['name'] == updated_name
        assert resp['data']['phone'] == updated_phone
        assert resp['data']['company'] == updated_company
