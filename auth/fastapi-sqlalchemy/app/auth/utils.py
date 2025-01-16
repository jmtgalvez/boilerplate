import jwt
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy.exc import NoResultFound, IntegrityError

from .models import *

load_dotenv()

def generate_token(emp_id: str) -> str:
  payload = {'emp_id': emp_id,  }
  token = jwt.encode(payload, 'secret', algorithm='HS256')
  return token

def transform_employee(data: dict) -> Employee:
  return {
    'emp_id': data[0],
    'name': data[1],
    'nickname': data[2],
    'gender': data[3],
    'department': data[4],
    'section': data[5],
    'sub_section': data[6],
    'position': data[7],
    'job_level': data[8],
    'email': data[9],
    'phone_number': data[10],
    'telephone_number': data[11],
    'rfid': data[12],
    'employee_status': data[13],
    'employee_picture': data[14]
  }



def error_handler(e: Exception):
    if type(e) == NoResultFound:
        return {
            'status': 400,
            'message': 'User does not exist in the database'
        }
    elif type(e) == IntegrityError:
        return {
            'status': 400,
            'message': 'User already has an account'
        }
    elif type(e) == AttributeError:
        return {
            'status': 400,
            'message': f'Invalid key: {e.args[0]}'
        }
    else:
        return {
            'status': 500,
            'message': 'Internal Server Error'
        }