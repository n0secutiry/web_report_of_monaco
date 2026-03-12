from sqlalchemy import select, func, outerjoin

from app.database.models import GroupModel, StudentModel


class GroupService:
    def __init__(self, db):
        self.db = db

    def show_groups_by_number(self, num):
        students_count = func.count(StudentModel.id)
        stmt = (
            select(GroupModel.name, students_count)
            .outerjoin(StudentModel)
            .group_by(GroupModel.name)
            .having(students_count <= num)
        )

        results_stmt = self.db.execute(stmt).all()
        result_list = list()
        for group, students in results_stmt:
            result_list.append({
                "group_name": group,
                "student_count": students
            })

        return result_list
    
    
