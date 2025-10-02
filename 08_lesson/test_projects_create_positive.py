import pytest
import os

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")

class TestProjectsCreatePositive:
    """Позитивные тесты для создания проектов"""
    
    def test_create_project_success(self, api_client, cleanup_project, base_project_data):
        """
        Позитивный тест: успешное создание проекта с валидными данными
        """
        response = api_client.post(
            f"{BASE_URL}/projects",
            json=base_project_data
        )
        
        assert response.status_code == 201, (
            f"Ожидался статус 201 Created, получен {response.status_code}. "
            f"Response: {response.text}"
        )
        
        response_json = response.json()
        
        required_fields = ["id", "title", "description", "createdAt", "updatedAt"]
        for field in required_fields:
            assert field in response_json, f"Ответ должен содержать поле '{field}'"
        
        assert response_json["title"] == base_project_data["title"]
        assert response_json["description"] == base_project_data["description"]
        assert isinstance(response_json["id"], str)
        assert len(response_json["id"]) > 0
        assert response_json["createdAt"] is not None
        assert response_json["updatedAt"] is not None
        
        project_id = response_json["id"]
        cleanup_project.append(project_id)
        
        get_response = api_client.get(f"{BASE_URL}/projects/{project_id}")
        assert get_response.status_code == 200
        assert get_response.json()["id"] == project_id
        
        print(f"✅ Успешно создан проект с ID: {project_id}")