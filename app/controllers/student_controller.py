from flask import request
from flask_restful import Resource

from app.database.database import get_db
from app.service.student_service import StudentService


class StudentResource(Resource):
    def post(self):
        """
        Create a new student and assign courses.
        ---
        tags:
          - Students
        parameters:
          - in: body
            name: body
            required: true
            description: JSON object containing student details and course IDs
            schema:
              type: object
              required:
                - first_name
                - last_name
                - course_list
              properties:
                first_name:
                  type: string
                  description: First name of the student
                  example: "Taras"
                last_name:
                  type: string
                  description: Last name of the student
                  example: "Shevchenko"
                course_list:
                  type: array
                  description: List of Course IDs to assign
                  items:
                    type: integer
                  example: [1, 2, 5]
        responses:
          201:
            description: Student created successfully
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "New student added!"
          400:
            description: Invalid input (e.g. course_list is not a list)
        """
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        course_list = data.get("course_list")

        if not isinstance(course_list, list):
            return {"message": "course_list mest be list!"}, 400
        

        with get_db() as db:
            create_student = StudentService(db=db)
            new_student = create_student.add_new_student(first_name, last_name, course_list)

        return {"message": "New student added!"}, 201
    

class StudentDeleteResource(Resource):    
    def delete(self, student_id, group_id):
        """
        Remove a student from a specific group.
        ---
        tags:
          - Students
        parameters:
          - in: path
            name: student_id
            type: integer
            required: true
            description: ID of the student to update
          - in: path
            name: group_id
            type: integer
            required: true
            description: ID of the group to remove the student from
        responses:
          200:
            description: Student successfully removed from the group
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Student removed from group"
          400:
            description: Student is not in this group
          404:
            description: Student not found
        """
        with get_db() as db:
            delete_student = StudentService(db=db)
            result = delete_student.remove_student_from_group(student_id, group_id)

        return result