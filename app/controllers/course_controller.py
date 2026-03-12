from flask_restful import Resource

from app.database.database import get_db
from app.service.course_service import CourseService


class CourseResourse(Resource):
    def get(self, course_name):
        """Find all students related to the course with a given name.
        ---
        parameters:
          - in: path
            name: course_name
            type: string
            required: true
            description: all students in course
        responses:
          200:
            description: A list of groups
            schema:
              type: array
              items:
                type: object
                properties:
                  first_name:
                    type: string
                  last_name:
                    type: string
        """
        with get_db() as db:
            course_service = CourseService(db=db)
            found_students = course_service.students_related_course(course_name)
        return found_students