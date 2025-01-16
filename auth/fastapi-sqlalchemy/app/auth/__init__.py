from fastapi import APIRouter, Request

from .db import *
from .utils import *
from .models import *

router = APIRouter(prefix='/auth', tags=['auth'])

@router.get('/')
def read_root():
    emps = get_employees()
    return {'message': 'Hello World', 'employees': emps }

@router.get('/employee/{emp_id}')
def get_employee(emp_id: str):
    emp = find_employee(emp_id=emp_id)
    return {'message': 'Hello World', 'employee': emp }

@router.put('/employee/{emp_id}')
def edit_employee(emp_id: str, data: dict):
    try:
        emp = update_employee(emp_id=emp_id, data=data)
        return {'message': 'Hello World', 'employee': emp }
    except Exception as e:
        return error_handler(e)

@router.delete('/employee/{emp_id}')
def delete_employee(emp_id: str):
    try:
        emp = update_employee(emp_id=emp_id, data={'employee_status': 'Inactive'})
        return {'message': 'Hello World', 'employee': emp }
    except Exception as e:
        return error_handler(e)

@router.post('/register')
async def register(credentials: Credentials, request: Request):
    username, password = credentials
    try:
        emp = insert_credentials(credentials)
        return {'message': 'Register Successful', 'employee': emp }
    except Exception as e:
        return error_handler(e)

@router.post('/login')
async def login(crendentials: Credentials, request: Request):
    # print(request.client.host)
    emp = find_employee(emp_id=crendentials.username)
    print(emp)
    return {'message': 'Login Successful', 'employee': emp }
