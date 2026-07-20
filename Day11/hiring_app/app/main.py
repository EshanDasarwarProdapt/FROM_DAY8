# from fastapi import FastAPI
# from app.models.job import Job
# from app.schemas.job_schema import JobCreate
# #This imports the FastAPI class from the fastapi package

# app = FastAPI()
# #This creates a FastAPI application object.

# @app.get('/')
# def home():
#     #create a job object model
#     job = Job(
#         title="Backend Developer",
#         description="Develop FastAPI Applications",
#         salary=750000,
#         company="ABC Technologies"
#     )
    
#     job_schema = JobCreate(
#         title=job.title,
#         description=job.description,
#         salary=job.salary,
#         company=job.company
#     )

#     return{
#         "Model": job.__dict__,
#         "Schema": job_schema.model_dump()
#     }
    
# @app.post("/jobs")
# def create_jobs(job: JobCreate):
#     #Convert Schema to Model
#     job_model = Job(
#         title=job.title,
#         description=job.description,
#         salary=job.salary,
#         company=job.company
#     )
    
#     return{
#         "message": "Job Created Successfully",
#         "data": job_model.__dict__
#     }
    
    
# # @app.get('/')
# # def home():
# #     return {"message": "Welcome to FastAPI"}

# # @app.post("/jobs")
# # def create_jobs():
# #     return {"message": "Job Created"}

# # @app.get("/jobs")
# # def get_jobs():
# #     return {"message": "List of jobs"}

# # @app.put("/jobs")
# # def update_job():
# #     return {"message": "Job Updated"}

# # @app.patch("/jobs")
# # def update_salary():
# #     return {"message": "Salary Updated"}

# # #/jobs  - static query
# # @app.delete("/jobs") 
# # def delete_job():
# #     return {"message": "Job Deleted"}

# # #Path Parameters - /jobs/13  - dynamic query
# # @app.get("/jobs/{job_id}")
# # def get_job_path(job_id:int):
# #     return {"job_id": job_id}

# # #Query Parameters - http://127.0.0.1:8000/jobs?location=Chennai
# # #Searching, Filteration, Sorting, Specific search
# # @app.get("/jobsquery")
# # def get_jobs_query(location:str):
# #     return {"location":location}

# # #Multiple query parameter
# # @app.get("/jobslocation")
# # def get_jobs_location(location: str, experience: int):
# #     return {
# #         "location": location,
# #         "experience": experience
# #     }
    
# # #/jobs?location=Chennai&experience=3

# '''
# @app.get("/")

# This is called a decorator.
# It tells FastAPI:
# "When someone sends a GET request to /, execute the function below."

# home() - Python function
# return - FastAPI automatically converts the Python dictionary into JSON
# '''

import os
import sys

# Add the project root directory to the python path to allow direct execution
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import Base, engine
from app.core.session import get_db

# Import models so SQLAlchemy registers them
from app.models.job import Job
from app.schema.job_schema import JobCreate, JobUpdate, JobResponse

app = FastAPI(
    title="Hiring Application"
)

# Create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    # Generate mock Job and JobCreate schema as expected by the existing tests
    job = Job(
        title="Python Dev",
        description="Develop FastAPI Applications",
        salary=750000.0,
        company="ABC Technologies"
    )
    job_schema = JobCreate(
        title=job.title,
        description=job.description,
        salary=job.salary,
        company=job.company
    )
    return {
        "message": "Hiring Application Started Successfully",
        "Model": job.__dict__,
        "Schema": job_schema.model_dump()
    }


@app.post("/jobs", response_model=JobResponse, status_code=201)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(
        title=job.title,
        description=job.description,
        salary=job.salary,
        company=job.company
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


@app.get("/jobs", response_model=list[JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()


@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@app.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Update only the fields that are provided
    update_data = job.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_job, key, value)
        
    db.commit()
    db.refresh(db_job)
    return db_job


@app.delete("/jobs/{job_id}", status_code=204)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return None


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)