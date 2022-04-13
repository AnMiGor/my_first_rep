import requests


def test_my_first_test():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
