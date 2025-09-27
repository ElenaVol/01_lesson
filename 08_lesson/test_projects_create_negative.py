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
        
        error_list = response.json()
        assert isinstance(error_list, list), "Ответ должен быть списком ошибок"
        assert len(error_list) > 0, "Список ошибок не должен быть пустым"
        
        all_errors = " ".join(error_list).lower()
        
        assert any("title" in error for error in error_list), (
            f"Ошибка должна содержать информацию о поле title: {error_list}"
        )
        
        title_errors = [error for error in error_list if "title" in error.lower()]
        assert len(title_errors) > 0, f"Не найдено ошибок про title: {error_list}"
        
        print("✅ Корректно обработана ошибка валидации при создании проекта без title")
        print(f"Полученные ошибки: {error_list}")