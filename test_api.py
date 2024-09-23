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


def check_repository_exists(repo_name):
    """Проверить, существует ли репозиторий в списке репозиториев."""
    url = f"{GITHUB_API_URL}/users/{config.GITHUB_USERNAME}/repos"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        repos = response.json()
        repo_names = [repo['name'] for repo in repos]
        if repo_name in repo_names:
            print(f"Репозиторий '{repo_name}' найден.")
            return True
        else:
            print(f"Репозиторий '{repo_name}' не найден.")
            return False
    else:
        print(f"Ошибка при получении списка репозиториев: {response.json()}")
        return False


def delete_repository(repo_name):
    """Удалить репозиторий на GitHub."""
    url = f"{GITHUB_API_URL}/repos/{config.GITHUB_USERNAME}/{repo_name}"
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"Репозиторий '{repo_name}' успешно удалён.")
    else:
        print(f"Ошибка при удалении репозитория: {response.json()}")
    return response.status_code == 204


if __name__ == "__main__":
    create_repository('my-test-api')
    check_repository_exists('my-test-api')
    delete_repository('my-test-api')
