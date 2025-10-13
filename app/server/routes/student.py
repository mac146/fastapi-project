from fastapi import APIRouter,Body
from fastapi.encoders import jsonable_encoder

from app.server.database import(
    add_student,
    delete_student,
    retrive_student,
    retrive_students,
    update_student,
)

from app.server.models.students import (
    responseModel,
    ErrorResponseModel,
    StudentSchema,
    StudentModel,
)

router=APIRouter()

@router.post('/',response_description="Student data added into the database")
async def add_student_data(student:StudentSchema=Body(...)):
    student=jsonable_encoder(student)
    new_student=await add_student(student)
    return responseModel(new_student,'student added succesfully')

@router.get('/',response_description='students data retreived')
async def get_students():
    students=await retrive_students()
    if students:
        return responseModel(students, "Students data retrieved successfully")
    return responseModel(students, "Empty list returned")

@router.get('/{id}',response_description='student data retreived')
async def get_student(id):
    student=await retrive_student(id)
    if student:
        return responseModel(student, "Students data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

@router.post('/{id}',response_description='updating student data')
async def update_student_data(id:str,req:StudentModel=Body(...)):
    req={k:v for k ,v in req.dict().items() if v is not None}
    updated_student=await update_student(id,req)
    if updated_student:
        return responseModel(
            "Student with ID: {} data update is successful".format(id),
            "Student data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )

@router.delete('/{id}',response_description='deleting student data')
async def delete_student_data(id:str):
    deleted_student=await delete_student(id)
    if deleted_student:
        return responseModel(
            "Student with ID: {} data deleted is successful".format(id),
            "Students data updated successfully",
        )
    
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )