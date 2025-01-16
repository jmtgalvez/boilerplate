from app import app
import uvicorn
import pathlib

uvicorn.run(app, host="0.0.0.0", port=8000)