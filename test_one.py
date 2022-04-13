import requests


def test_my_first_test():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200


def test_my_second_test():
    response = requests.get("https://mail.ru/")
    assert response.status_code == 200
