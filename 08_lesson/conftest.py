import pytest
import requests
import os

BASE_URL = "https://ru.yougile.com/api-v2"
API_TOKEN = os.getenv("YOUGILE_API_TOKEN")

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    })
    return session

@pytest.fixture
def cleanup_project(api_client):
    created_project_ids = []
    yield created_project_ids
    for project_id in created_project_ids:
        try:
            api_client.delete(f"{BASE_URL}/projects/{project_id}")
        except:
            pass

@pytest.fixture
def create_test_project(api_client, cleanup_project):
    project_data = {
        "title": "Test Project for Testing",
        "description": "Project created for testing operations"
    }
    response = api_client.post(f"{BASE_URL}/projects", json=project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    cleanup_project.append(project_id)
    return project_id