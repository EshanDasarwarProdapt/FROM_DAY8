# pyrefly: ignore [missing-import]
from pathlib import Path
import sys

from fastapi import FastAPI

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from app.models.job import job
    from app.schema.job_schema import JobCreate
else:
    from .models.job import job
    from .schema.job_schema import JobCreate

app = FastAPI()


@app.get("/")
def home():
    job_instance = job(
        title="Python Dev",
        description="Develop FastAPI Application",
        salary=750000,
        company="ABC Technologies",
    )

    job_schema = JobCreate(
        title=job_instance.title,
        description=job_instance.description,
        salary=job_instance.salary,
        company=job_instance.company,
    )

    return {
        "Model": job_instance.__dict__,
        "Schema": job_schema.model_dump(),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)