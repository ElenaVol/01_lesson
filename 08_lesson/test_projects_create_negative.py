import pytest
import os

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")

class TestProjectsCreateNegative:
    """Негативные тесты для создания проектов"""
    
    def test_create_project_without_title(self, api_client):
        """
        Негативный тест: попытка создания проекта без обязательного поля title
        """
        invalid_data = {
            "description": "Project without title should fail"
        }
        
        response = api_client.post(
            f"{BASE_URL}/projects",
            json=invalid_data
        )
        
        assert response.status_code in [400, 422], (
            f"Ожидалась ошибка 400 или 422, получен {response.status_code}. "
            f"Response: {response.text}"
        )
        
        response_json = response.json()
        assert "message" in response_json or "error" in response_json, (
            "Ответ должен содержать сообщение об ошибке"
        )
        
        error_message = response_json.get("message", "") or response_json.get("error", "")
        assert "title" in error_message.lower(), (
            f"Ошибка должна содержать информацию о поле title: {error_message}"
        )
        
        print("✅ Корректно обработана ошибка валидации при создании проекта без title")