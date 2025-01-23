from typing import Any

import requests

from test_data.constants import BASE_URL


class BaseAPI:


    def get(self, endpoint, params=None):
        response = requests.get(f'{BASE_URL}{endpoint}', params=params)
        response.raise_for_status()
        return response

    def post(self, endpoint, payload):
        response = requests.post(f'{BASE_URL}{endpoint}', json=payload)
        response.raise_for_status()
        return response

    def delete(self, endpoint):
        response = requests.delete(f'{BASE_URL}{endpoint}')
        return response

    def check_status_code (
            self,
            returned_status_code: int,
            expected_status_code: int
    ):
        if not  returned_status_code == expected_status_code:
            raise Exception (
                f'Expected status code {expected_status_code}, got {returned_status_code}'
            )


    def compare_response_and_input(
            self,
            input_content : dict[str, Any],
            response_content : dict[str, Any]
    ):
        for key, value in input_content:
            if not response_content[key] == value:
                raise ValueError(
                    f"Mismatch for field '{key}': expected '{value}', got '{response_content[key]}'"
                )