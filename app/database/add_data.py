from sqlalchemy import select
import string
import random

from .database import get_db
from .models import GroupModel, CourseModel, StudentModel



def generate_group_name():
    with get_db() as db:
        for _ in range(10):
            letters = "".join(random.choices(string.ascii_uppercase, k=2))
            numbers = "".join(random.choices(string.digits, k=2))
            group_name = f"{letters}-{numbers}"
            new_group = GroupModel(name=group_name)
            db.add(new_group)
            print(f"Group {new_group} added!")
        db.commit()
        print("Group commited!")


def generate_course():
    courses = {
        "Mathematics": "Deals with numbers, calculations, sums, and problem-solving.",
        "Science": "Learning about the natural world, conducting experiments, and understanding concepts like gravity, life (Biology), matter (Chemistry), and energy (Physics).",
        "History": "Studying past events, dates, and cultures to understand how societies developed.",
        "English": "Reading, writing, speaking, and analyzing texts like books, poems, and essays.",
        "Physical Education": "Focuses on physical fitness, sports, and games (running, jumping).",
        "Geography": "Learning about countries, cities, landforms, and the environment.",
        "Art": "Developing creativity through drawing, painting, and visual expression.",
        "Music": "Learning to sing, play instruments, and analyze music.",
        "Information Technology": "Using computers, software (Microsoft Office, Photoshop), internet safety, and coding.",
        "Literature": "Reading and analyzing books, stories, and poetry.",
    }

    with get_db() as db:
        for name, description in courses.items():
            print(f"Name -> {name} | Description -> {description}")
            new_subject = CourseModel(name=name, description=description)
            db.add(new_subject)
            print(new_subject)
            db.commit()
        print("All course commited!")


from sqlalchemy import select # Не забудь імпорт
import random

def generate_students():
    first_names = ["Liam", "Noah", "Oliver", "Theodore", "Ethan", "Lucas", "Aiden", "Jackson", "Logan", "Leo", "Bowen", "Kylan", "Franklin", "Jaylen", "Dilan", "Antonio", "Lucian", "Maxton", "Kase", "Flynn"]
    last_names = ["Olivia", "Ava", "Charlotte", "Amelia", "Sophia", "Mia", "Harper", "Evelyn", "Isabella", "Abigail", "Saige", "Amelie", "Saoirse", "Scarlett", "Carolina", "Marina", "Kairi", "Camila", "Aisha", "Nova"]
    
    with get_db() as db:
        all_students = []
        for _ in range(200):
            new_student = StudentModel(first_name=random.choice(first_names), last_name=random.choice(last_names)) 
            all_students.append(new_student)

        stmt = select(GroupModel)
        groups = db.scalars(stmt).all() 

        stmt_course = select(CourseModel)
        courses = db.scalars(stmt_course).all()

        random.shuffle(all_students)

        for group in groups:
            if not all_students:
                break

            count = random.randint(10, 30)
            
            students_without_group = [s for s in all_students if s.group_id is None]
            
            if len(students_without_group) < count:
                count = len(students_without_group)

            current_batch = students_without_group[:count]

            for student in current_batch:
                student.group_id = group.id

        for student in all_students:
            k = random.randint(1, 3)
            if len(courses) < k:
                k = len(courses)
                
            selected_courses = random.sample(courses, k)
            student.courses = selected_courses

        db.add_all(all_students)
        db.commit()
        print("Students generated successfully!")




generate_group_name()
generate_course()
generate_students()