from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail

from .config import *

conf = ConnectionConfig(
  MAIL_USERNAME="",
  MAIL_PASSWORD="",
  MAIL_FROM_NAME=MAIL_FROM_NAME,
  MAIL_FROM=MAIL_FROM,
  MAIL_PORT=MAIL_PORT,
  MAIL_SERVER=MAIL_SERVER,
  USE_CREDENTIALS=False,
  MAIL_STARTTLS=False,
  MAIL_SSL_TLS=False
)

async def send_test_email():
  html = "<h1>Sending test email...</h1>"
  message = MessageSchema(
    subject="Test Impex Email",
    recipients=["xam@ple"],
    body=html,
    subtype=MessageType.html
  )
  fm = FastMail(conf)
  await fm.send_message(message)