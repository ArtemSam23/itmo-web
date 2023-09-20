from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, EmailStr

app = FastAPI()
app.mount("/src", StaticFiles(directory="src"))


class FormResponse(BaseModel):
    email: EmailStr
    password: str


@app.get("/")
async def root():
    return FileResponse("./src/index.html", media_type='text/html')


@app.post("/form", response_model=FormResponse)
async def submit_form(email: str = Form(), password: str = Form()):
    return {"email": email, "password": password}
