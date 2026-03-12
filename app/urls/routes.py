from app.controllers.group_contorller import GroupResource
from app.controllers.course_controller import CourseResourse
from app.controllers.student_controller import StudentResource, StudentDeleteResource



# @app.route("/")
# def main_page():
#     return {"server": "work"}
    


def init_routes(api):
    api.add_resource(GroupResource, "/api/v1/groups/<int:amount_students>")
    api.add_resource(CourseResourse, "/api/v1/courses/<string:course_name>")
    api.add_resource(StudentResource, "/api/v1/students/create_new")
    api.add_resource(StudentDeleteResource, "/api/v1/students/<int:student_id>/groups/<int:group_id>")
