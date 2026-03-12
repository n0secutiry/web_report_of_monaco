from sqlalchemy import select

from app.database.models import CourseModel, StudentModel


class CourseService:
    def __init__(self, db):
        self.db = db

    def students_related_course(self, name_course):
        stmt = (
            select(StudentModel)
            .join(StudentModel.courses)
            .where(CourseModel.name == name_course)
        )

        students = self.db.execute(stmt).scalars().all()

        result_list = []

        for student in students:
            result_list.append({
                "first_name": student.first_name,
                "last_name": student.last_name
            })
        
        return result_list