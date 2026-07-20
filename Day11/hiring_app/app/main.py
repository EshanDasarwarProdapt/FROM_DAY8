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

@app.get("/jobs/{job_id}")
def get_job_path(job_id:int):
    return{"job_id": job_id}

@app.get("/jobsQuery")
def get_jobs_query(location:str):
    return{"location":location}

@app.get("/jobsLocation")
def get_jobs_query(location:str, experience:int):
    return{
        "location":location,
        "experience": experience
        }