from fastapi import APIRouter, HTTPException
from models import StudentCreate
from fake_db import load_students, save_students

router = APIRouter()

@router.get("/students")
def get_all_students(
    name: str | None = None,
    min_score: float | None = None,
    max_score: float | None = None,
    page: int = 1,
    size: int = 10
):
    students_db = load_students()  # 从 JSON 文件加载学生数据

    if page < 1:
        raise HTTPException(status_code=400, detail="page must be >= 1")
    if size < 1:
        raise HTTPException(status_code=400, detail="size must be >= 1")

    if min_score is not None and max_score is not None and min_score > max_score:
        raise HTTPException(status_code=400, detail="min_score cannot be greater than max_score")

    result = students_db.copy()

    if name is not None:
        filtered = []
        for student in result:
            if student["name"] == name:
                filtered.append(student)
        result = filtered

    if min_score is not None:
        filtered = []
        for student in result:
            if student["score"] >= min_score:
                filtered.append(student)
        result = filtered

    if max_score is not None:
        filtered = []
        for student in result:
            if student["score"] <= max_score:
                filtered.append(student)
        result = filtered

    start = (page - 1) * size
    end = start + size
    paged_result = result[start:end]

    return {
        "code": 200,
        "message": "success",
        "data": {
            "total": len(result),
            "page": page,
            "size": size,
            "students": paged_result
        }
    }


@router.get("/students/{student_id}")
def get_student(student_id: int):
    students_db = load_students()  # 从 JSON 文件加载学生数据
    for student in students_db:
        if student["id"] == student_id:
            return {
                "code": 200,
                "message": "success",
                "data": student
            }
    raise HTTPException(status_code=404, detail="Student not found")


@router.post("/students")
def create_student(student: StudentCreate):
    students_db = load_students()  # 从 JSON 文件加载学生数据

    if student.score < 0 or student.score > 100:
        raise HTTPException(status_code=400, detail="score must be between 0 and 100")

    new_id = 1
    if students_db:
        new_id = students_db[-1]["id"] + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "score": student.score
    }

    students_db.append(new_student)
    save_students(students_db)  # 保存到 JSON 文件

    return {
        "code": 200,
        "message": "Student created",
        "data": new_student
    }


@router.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate):
    students_db = load_students()  # 从 JSON 文件加载学生数据

    if student.score < 0 or student.score > 100:
        raise HTTPException(status_code=400, detail="score must be between 0 and 100")

    for s in students_db:
        if s["id"] == student_id:
            s["name"] = student.name
            s["age"] = student.age
            s["score"] = student.score
            save_students(students_db)  # 保存更新后的数据
            return {
                "code": 200,
                "message": "Student updated",
                "data": s
            }

    raise HTTPException(status_code=404, detail="Student not found")


@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    students_db = load_students()  # 从 JSON 文件加载学生数据
    for i, student in enumerate(students_db):
        if student["id"] == student_id:
            deleted_student = students_db.pop(i)
            save_students(students_db)  # 保存删除后的数据
            return {
                "code": 200,
                "message": "Student deleted",
                "data": deleted_student
            }

    raise HTTPException(status_code=404, detail="Student not found")