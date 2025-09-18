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
    
    for project_id in created_project_ids:
        try:
            api_client.delete(f"{BASE_URL}/projects/{project_id}")
        except:
            pass

@pytest.fixture
def base_project_data():
    """Базовые данные для создания проекта"""
    return {
        "title": "Test Project",
        "description": "Project created by automated tests"
    }