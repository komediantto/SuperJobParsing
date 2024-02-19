import httpx
from .config import CONFIG


def authorize():
    headers = {"X-Api-App-Id": CONFIG.CLIENT_SECRET}

    URL = "https://api.superjob.ru/2.0/"

    response = httpx.get(
        "".join([URL, "oauth2/password/"]),
        params={
            "login": CONFIG.LOGIN,
            "password": CONFIG.PASSWORD,
            "client_id": CONFIG.CLIENT_ID,
            "client_secret": CONFIG.CLIENT_SECRET,
        },
        headers=headers,
    )
    access_token = response.json()["access_token"]

    headers["Authorization"] = f"Bearer {access_token}"
    return headers


def get_phones(id):
    try:
        response = httpx.get(
            f"https://api.superjob.ru/2.0/vacancies/{id}/", headers=authorize()
        )
        if response.status_code == 200:
            return response.json()["phone"], response.json()["phones"]
        else:
            return
    except:
        return
