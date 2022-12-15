import requests
from Libary.base_case import BaseCase
from Libary.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        last_name = register_data["lastName"]
        password = register_data["password"]

