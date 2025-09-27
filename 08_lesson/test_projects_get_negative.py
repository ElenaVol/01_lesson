import pytest

BASE_URL = "https://ru.yougile.com/api-v2"

class TestProjectsGetNegative:
    
    def test_get_nonexistent_project(self, api_client):
        """
        Негативный тест: попытка получения несуществующего проекта
        """
        non_existent_id = "00000000-0000-0000-0000-000000000000"
        
        response = api_client.get(f"{BASE_URL}/projects/{non_existent_id}")
        
        assert response.status_code == 404
        response_json = response.json()
        assert "message" in response_json or "error" in response_json
        
        print("✅ Корректно обработана ошибка получения несуществующего проекта")