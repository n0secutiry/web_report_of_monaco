import json
from app.database.models import CourseModel, StudentModel, GroupModel


def test_create_student_api(test_client, init_database):
    db_session = init_database

    course = CourseModel(name="History", description="World History")
    db_session.add(course)
    db_session.commit()

    payload = {
        "first_name": "API",
        "last_name": "User",
        "course_list": [course.id]
    }

    response = test_client.post(
        '/api/v1/students/create_new',
        data=json.dumps(payload),
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.json['message'] == "New student added!"


def test_delete_student_from_group_api(test_client, init_database):
    db_session = init_database

    group = GroupModel(name="BB-22")
    db_session.add(group)
    db_session.commit()

    student = StudentModel(first_name="Delete",
                           last_name="Me", group_id=group.id)
    db_session.add(student)
    db_session.commit()

    url = f'/api/v1/students/{student.id}/groups/{group.id}'

    response = test_client.delete(url)

    assert response.status_code == 200
    assert response.json['message'] == "Student removed from group"
