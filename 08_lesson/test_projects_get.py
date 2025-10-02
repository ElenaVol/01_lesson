import pytest

BASE_URL = "https://ru.yougile.com/api-v2"

class TestProjectsGetPositive:
    
    def test_get_project_success(self, api_client, create_test_project):
        project_id = create_test_project
        
        response = api_client.get(f"{BASE_URL}/projects/{project_id}")
        
        assert response.status_code == 200
        response_json = response.json()
        
        required_fields = ["id", "title", "description", "createdAt", "updatedAt"]
        for field in required_fields:
            assert field in response_json
        
        assert response_json["id"] == project_id
        assert response_json["title"] == "Test Project for Testing"
        assert response_json["description"] == "Project created for testing operations"
        
        print(f"✅ Успешно получен проект с ID: {project_id}")
