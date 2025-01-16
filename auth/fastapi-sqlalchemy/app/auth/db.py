import sqlalchemy as sa
from sqlalchemy import inspect, Table, Column, String
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base
from sqlalchemy.exc import NoResultFound, IntegrityError

from urllib.parse import quote_plus

from .models import *
from .utils import *

DATABASE_URL= 'mysql+pymysql://root:%s@127.0.0.1:3306/auth' % quote_plus("P@ssword")
engine = sa.create_engine(DATABASE_URL)
metadata = sa.MetaData()

creds_table = Table(
  'credentials',
  metadata,
  Column('username', String(191), primary_key=True),
  Column('password', String(191))
)

inspector = inspect(engine)
if not inspector.has_table('credentials'):
  creds_table.create(engine)

employee_table = Table(
  'tblemplist',
  metadata,
  Column('emp_id', String(191), primary_key=True),
  Column('name', String(191)),
  Column('nickname', String(191)),
  Column('gender', String(191)),
  Column('department', String(191)),
  Column('section', String(191)),
  Column('sub_section', String(191)),
  Column('position', String(191)),
  Column('job_level', String(191)),
  Column('email', String(191)),
  Column('phone_number', String(191)),
  Column('telephone_number', String(191)),
  Column('rfid', String(191)),
  Column('employee_status', String(191)),
  Column('employee_picture', String(191))
)

def insert_credentials(credentials: Credentials) -> None:
  with engine.connect() as con:
    try:
      emp = find_employee(emp_id=credentials.username)
      result = con.execute(creds_table.insert().values(username=credentials.username, password=credentials.password))
      con.commit()
      return emp
    except Exception as e:
      raise e

def get_employees() -> list:
  with engine.connect() as con:
    result = con.execute(sa.select(employee_table))
    employees = []
    for row in result:
      employees.append(transform_employee(row))
    return employees

def find_employee(emp_id: str) -> Employee: 
  print(emp_id)
  with engine.connect() as con:
    result = con.execute(employee_table.select().where(employee_table.c.emp_id == emp_id))
    if result.rowcount == 0:
      raise NoResultFound
    return transform_employee(result.fetchone())
    
def update_employee(emp_id: str, data: dict) -> Employee:
  for key in data:
    if key not in employee_table.c.keys():
      raise AttributeError(key)

  with engine.connect() as con:
    result = con.execute(employee_table.update().where(employee_table.c.emp_id == emp_id).values(data))
    con.commit()
    return find_employee(emp_id=emp_id)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_employees_orm() -> list:
  with Session() as session:
    return session.query(Employee).all()

def find_employee_orm(emp_id: str) -> Employee:
  with Session() as session:
    try:
      return session.query(Employee).filter(Employee.emp_id == emp_id).one()
    except NoResultFound:
      return None