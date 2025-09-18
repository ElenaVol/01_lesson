import pytest

BASE_URL = "https://ru.yougile.com/api-v2"

class TestProjectsUpdatePositive:
    """Позитивные тесты для обновления проектов"""
    
    def test_update_project_title_and_description(self, api_client, create_test_project):
        """
        Позитивный тест: обновление названия и описания проекта
        """
        project_id = create_test_project
        
        update_data = {
            "title": "Updated Project Title",
            "description": "Updated project description for testing"
        }
        
        response = api_client.put(
            f"{BASE_URL}/projects/{project_id}",
            json=update_data
        )
        
        assert response.status_code == 200, (
            f"Ожидался статус 200 OK, получен {response.status_code}. "
            f"Response: {response.text}"
        )
        
        response_json = response.json()
        assert "id" in response_json
        assert response_json["id"] == project_id
        assert response_json["title"] == update_data["title"]
        assert response_json["description"] == update_data["description"]
        
        get_response = api_client.get(f"{BASE_URL}/projects/{project_id}")
        assert get_response.status_code == 200
        assert get_response.json()["title"] == update_data["title"]
        assert get_response.json()["description"] == update_data["description"]
        
        print(f"✅ Успешно обновлен проект с ID: {project_id}")