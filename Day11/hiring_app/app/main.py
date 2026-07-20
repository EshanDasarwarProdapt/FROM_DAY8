# pyrefly: ignore [missing-import]
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}  

@app.post("/jobs") 
def create_jobs():
    return{"message": "Job Created"}

@app.get("/jobs")
def get_jobs():
    return{"message": "List of Jobs"}

@app.put("/jobs")
def update_job():
    return{"message": "Job Updated"}

@app.patch("/jobs")
def update_salary():
    return{"message":"Salary Updated"}

@app.delete("/jobs")
def delete_job():
    return {"message": "Job Deleted"}