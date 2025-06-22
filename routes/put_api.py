from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from dependencies.db_call import MongoDBConnector

# Define request and response models
class EmployeeUpdateRequest(BaseModel):
    PHONE_NUMBER:str
    SALARY:int
    MANAGER_ID: int            
    DEPARTMENT_ID:int



router = APIRouter(
    prefix="/dev/api/v1/mongodb",
    tags=["dataaccessservice"],
    responses={404: {"description": "NotFound"}}
)

@router.put("/update_employee/{employee_id}")
async def update_employee(employee_id: int, update_data: EmployeeUpdateRequest):
    try:
        # Remove None values from update data
        db = MongoDBConnector()
        update_dict = update_data.model_dump(exclude_unset=True)
        if update_dict:
            if db.connect("testdb"):
                # Perform the update operation
                result = db.update("employee",employee_id, update_dict)
                if result == 1:
                    return "Successfully updated the data"
                else:
                     return "can't able to updated the data"
        db.close()

       
    except Exception as ex:
        print(f"Error in update_employee: {ex}")

