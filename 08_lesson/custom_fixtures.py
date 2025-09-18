import pytest
import requests
import os

BASE_URL = "https://ru.yougile.com/api-v2"

API_TOKEN = os.getenv("YOUGILE_API_TOKEN")

# Добавляем проверку токена
if not API_TOKEN:
    pytest.fail("YOUGILE_API_TOKEN не установлен в переменных окружения")

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для создания авторизованного клиента API"""
    session = requests.Session()
    
    session.headers.update({
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    
    return session

@pytest.fixture
def cleanup_project(api_client):
    """Фикстура для очистки созданных тестовых проектов"""
    created_project_ids = []
    
    yield created_project_ids
    
    for project_id in created_project_ids:
        try:
            api_client.delete(f"{BASE_URL}/projects/{project_id}")
        except:
            pass

@pytest.fixture
def create_test_project(api_client, cleanup_project):
    """Фикстура для создания тестового проекта"""
    project_data = {
        "title": "Test Project for Get",
        "description": "Project created for testing get operations"
    }
    
    response = api_client.post(
        f"{BASE_URL}/projects",
        json=project_data
    )
    
    assert response.status_code == 201
    project_id = response.json()["id"]
    cleanup_project.append(project_id)
    
    return project_id