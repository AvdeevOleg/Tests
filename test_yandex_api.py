import requests
import pytest

TOKEN = "Ваш токен API.Яндекс.Диск"
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"


def create_folder(folder_path):
    headers = {"Authorization": f"OAuth {TOKEN}"}
    response = requests.put(f"{BASE_URL}?path={folder_path}", headers=headers)
    return response


def test_create_folder():
    folder_path = "test_folder"
    response = create_folder(folder_path)
    assert response.status_code == 201 or response.status_code == 409

    # Проверка, что папка создана
    headers = {"Authorization": f"OAuth {TOKEN}"}
    response = requests.get(f"{BASE_URL}?path={folder_path}", headers=headers)
    assert response.status_code == 200


def test_create_existing_folder():
    folder_path = "test_folder"
    create_folder(folder_path)
    response = create_folder(folder_path)
    assert response.status_code == 409


def test_create_folder_invalid_token():
    folder_path = "test_folder_invalid_token"
    headers = {"Authorization": "OAuth invalid_token"}
    response = requests.put(f"{BASE_URL}?path={folder_path}", headers=headers)
    assert response.status_code == 401
