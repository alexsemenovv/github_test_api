import config
import requests
import time

GITHUB_API_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {config.GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def create_repository(repo_name):
    """Создать новый репозиторий на GitHub."""
    url = f"{GITHUB_API_URL}/user/repos"
    payload = {
        "name": repo_name,
        # "description": "Test repository created using GitHub API",
        "private": False  # Делаем репозиторий публичным
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    if response.status_code == 201:
        print(f"Репозиторий '{repo_name}' успешно создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.json()}")

    return response.status_code == 201


if __name__ == "__main__":
    create_repository('my-test-api')
