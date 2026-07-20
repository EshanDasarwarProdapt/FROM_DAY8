from pydantic import BaseModel, ConfigDict

class JobBase(BaseModel):
    title:str
    description:str
    salary:float
    company:str

class JobCreate(JobBase):
    pass

class JobUpdate(JobBase):
    title:str | None=None
    description:str | None=None
    salary :float | None=None
    company:str | None=None

class JobResponse(JobBase):
    id:int

    # class Config:
    #     form_attributes = True 

    model_config = ConfigDict(from_attributes=True)