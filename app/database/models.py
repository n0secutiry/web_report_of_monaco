from sqlalchemy import String, ForeignKey, Column, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional


class Base(DeclarativeBase):
    pass


association_table = Table(
    "student_course_association",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class GroupModel(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class StudentModel(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[Optional[int]] = mapped_column(ForeignKey("groups.id"), nullable=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))

    courses: Mapped[List["CourseModel"]] = relationship(
        secondary=association_table,
        back_populates="students"
    )


class CourseModel(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(300))

    students: Mapped[List["StudentModel"]] = relationship(
        secondary=association_table,
        back_populates="courses"
    )
