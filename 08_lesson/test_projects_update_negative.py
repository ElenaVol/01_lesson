import pytest

BASE_URL = "https://ru.yougile.com/api-v2"

class TestProjectsUpdateNegative:
    """Негативные тесты для обновления проектов"""
    
    def test_update_nonexistent_project(self, api_client):
        """
        Негативный тест: попытка обновления несуществующего проекта
        """
        non_existent_id = "00000000-0000-0000-0000-000000000000"
        
        update_data = {
            "title": "Updated Title",
            "description": "Updated description"
        }
        
        response = api_client.put(
            f"{BASE_URL}/projects/{non_existent_id}",
            json=update_data
        )
        
        assert response.status_code == 404, (
            f"Ожидался статус 404 Not Found, получен {response.status_code}. "
            f"Response: {response.text}"
        )
        
        response_json = response.json()
        assert "message" in response_json or "error" in response_json, (
            "Ответ должен содержать сообщение об ошибке"
        )
        
        print("✅ Корректно обработана ошибка обновления несуществующего проекта")