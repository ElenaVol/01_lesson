from models import Student
from sqlalchemy.exc import IntegrityError

def test_create_student(db_session):
    """Тест на добавление нового студента."""
    new_student = Student(name="Анна Петрова", email="anna@example.com")
    
    db_session.add(new_student)
    db_session.commit()

    student_from_db = db_session.query(Student).filter_by(email="anna@example.com").first()
    assert student_from_db is not None
    assert student_from_db.name == "Анна Петрова"

def test_update_student(db_session):
    """Тест на изменение данных студента."""
git
    student = Student(name="Иван Сидоров", email="ivan@example.com")
    db_session.add(student)
    db_session.commit()

    student_to_update = db_session.query(Student).filter_by(email="ivan@example.com").first()
    student_to_update.name = "Иван Иванов"
    db_session.commit()
  
    updated_student = db_session.query(Student).filter_by(email="ivan@example.com").first()
    assert updated_student.name == "Иван Иванов"

def test_delete_student(db_session):
    """Тест на удаление студента."""
 
    student = Student(name="Сергей Козлов", email="sergey@example.com")
    db_session.add(student)
    db_session.commit()

    student_to_delete = db_session.query(Student).filter_by(email="sergey@example.com").first()
    db_session.delete(student_to_delete)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(email="sergey@example.com").first()
    assert deleted_student is None