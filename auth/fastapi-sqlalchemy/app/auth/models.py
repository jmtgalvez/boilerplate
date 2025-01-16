from typing import Optional
from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()

# type class
class Credentials(BaseModel):
  username: str
  password: str
  
# sqlalchemy class table
class Employee(Base):
  __tablename__ = 'tblemplist'

  emp_id: Mapped[str] = mapped_column(String(191), primary_key=True)
  name: Mapped[str] = mapped_column(String(191))
  nickname: Mapped[str] = mapped_column(String(191))
  gender: Mapped[str] = mapped_column(String(191))
  department: Mapped[str] = mapped_column(String(191))
  section: Mapped[str] = mapped_column(String(191))
  sub_section: Mapped[str] = mapped_column(String(191))
  position: Mapped[str] = mapped_column(String(191))
  job_level: Mapped[str] = mapped_column(String(191))
  email: Mapped[str] = mapped_column(String(191))
  phone_number: Mapped[str] = mapped_column(String(191))
  telephone_number: Mapped[str] = mapped_column(String(191))
  rfid: Mapped[str] = mapped_column(String(191))
  employee_status: Mapped[str] = mapped_column(String(191)) 
  employee_picture: Mapped[str] = mapped_column(String(191))