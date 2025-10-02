import pytest
import requests
import os

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания авторизованного клиента API"""
    session = requests.Session()
    
    auth_token = os.getenv("YOUGILE_API_TOKEN")
    if not auth_token:
        pytest.fail("YOUGILE_API_TOKEN не установлен в переменных окружения")
    
    session.headers.update({
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    return session

@pytest.fixture
def cleanup_project(api_client):
    """Фикстура для очистки созданных тестовых проектов"""
    created_project_ids = []
    
    yield created_project_ids
    
    # Очистка после выполнения теста
    for project_id in created_project_ids:
        try:
            response = api_client.delete(f"{BASE_URL}/projects/{project_id}")
            if response.status_code == 200:
                print(f"✅ Удален проект {project_id}")
            else:
                print(f"⚠️ Не удалось удалить проект {project_id}: {response.status_code}")
        except Exception as e:
            print(f"❌ Ошибка при удалении проекта {project_id}: {e}")

@pytest.fixture
def base_project_data():
    """Базовые данные для создания проекта"""
    return {
        "title": "Test Project",
        "description": "Project created by automated tests"
    }

@pytest.fixture
def create_test_project(api_client, cleanup_project):
    """Фикстура для создания тестового проекта"""
    project_data = {
        "title": "Test Project for Testing",
        "description": "Project created for testing operations"
    }
    response = api_client.post(f"{BASE_URL}/projects", json=project_data)
    assert response.status_code == 201, f"Ошибка создания проекта: {response.text}"
    project_id = response.json()["id"]
    cleanup_project.append(project_id)
    return project_id