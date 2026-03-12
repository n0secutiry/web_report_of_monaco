from app.service.student_service import StudentService
from app.database.models import StudentModel, CourseModel, GroupModel


def test_add_student_with_courses(init_database):
    db_session = init_database

    course1 = CourseModel(name="Math", description="Basic Math")
    course2 = CourseModel(name="Biology", description="Basic Biology")
    db_session.add_all([course1, course2])
    db_session.commit()

    service = StudentService(db=db_session)
    service.add_new_student("Ivan", "Test", [course1.id, course2.id])

    student = db_session.query(StudentModel).filter_by(
        first_name="Ivan").first()

    assert student is not None
    assert student.last_name == "Test"
    assert len(student.courses) == 2


def test_remove_student_from_group(init_database):
    db_session = init_database

    group = GroupModel(name="AA-11")
    db_session.add(group)
    db_session.commit()

    student = StudentModel(
        first_name="Petro", last_name="Bambper", group_id=group.id)
    db_session.add(student)
    db_session.commit()

    service = StudentService(db=db_session)
    response, status = service.remove_student_from_group(student.id, group.id)

    db_session.refresh(student)

    assert status == 200
    assert student.group_id is None
