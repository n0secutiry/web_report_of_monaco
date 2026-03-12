from sqlalchemy import select, update

from app.database.models import StudentModel, CourseModel, GroupModel


class StudentService:
    def __init__(self, db):
        self.db = db

    def add_new_student(self, first_name, last_name, course_list):
        new_student = StudentModel(
            first_name=first_name,
            last_name=last_name
        )

        stmt = select(CourseModel).where(CourseModel.id.in_(course_list))
        course_from_db = self.db.execute(stmt).scalars().all()

        new_student.courses = list(course_from_db)

        self.db.add(new_student)
        self.db.commit()

    def remove_student_from_group(self, student_id, group_id):
        stmt = select(StudentModel).where(StudentModel.id == student_id)
        student = self.db.execute(stmt).scalar()

        if not student:
            return {"message": "Student not found"}, 404

        if student.group_id != group_id:
            return {"message": "Student is not in this group"}, 400

        student.group_id = None
        self.db.commit()

        return {"message": "Student removed from group"}, 200
