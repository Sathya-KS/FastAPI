from fastapi import FastAPI,APIRouter
from pydantic import BaseModel
from typing import Optional

from dependencies.db_call import SQLDatabaseConnection,MongoDBConnector

#app = FastAPI()

router = APIRouter(
                   prefix="/dev/api/v1/mongodb",
                   tags = ["dataaccessservice"],
                   responses = {404:{"description":"NotFound"}}
)

class Values(BaseModel):
    EMPLOYEE_ID: int
    FIRST_NAME: str
    LAST_NAME: str
    EMAIL: str
    PHONE_NUMBER: str
    HIRE_DATE: str
    JOB_ID: str
    SALARY: int
    COMMISSION_PCT:str #Optional[float] = None  # Default to None
    MANAGER_ID: int
    DEPARTMENT_ID: int



    # EMPLOYEE_ID:int
    # EMPLOYEE_NAME:str
    # PHONE_NUMBER:int

    
# @router.get("/update")
# async def update_data():
#     try:

#         db = SQLDatabaseConnection()
#         if db.connect():
#             row = db.fetch_employee(100)
#             db.close()
#         return row[2]
#     except Exception as ex:
#         print(ex)


@router.post("/insert_employee_details")
async def insert_employee_details(values:Values):
    try:
        values_dict = values.model_dump()
        db = MongoDBConnector()
        if db.connect("testdb"):
            documents = db.insert_one("employee",values_dict)
           
            # if documents:
            #     for doc in documents:
            #         print(doc)
            db.close()
        return "Successfully inserted the data"
    except Exception as ex:
        print(ex)