from flask_restful import Resource

from app.database.database import get_db
from app.service.group_service import GroupService

class GroupResource(Resource):
    def get(self, amount_students):
        """Find all groups with less or equals student count.
        ---
        parameters:
          - in: path
            name: amount_students
            type: integer
            required: true
            description: Maximum number of students
        responses:
          200:
            description: A list of groups
            schema:
              type: array
              items:
                type: object
                properties:
                  group_name:
                    type: string
                  student_count:
                    type: integer
        """
        with get_db() as db:
            group_service = GroupService(db=db)
            found_result = group_service.show_groups_by_number(num=amount_students)
        return found_result