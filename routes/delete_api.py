from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel
from dependencies.db_call import SQLDatabaseConnection, MongoDBConnector
from typing import Optional, Dict, Any



router = APIRouter(
    prefix="/dev/api/v1/mongodb",
    tags=["dataaccessservice"],
    responses={404: {"description": "NotFound"}}
)

@router.delete("/delete_employee/{employee_id}")
async def delete_employee(employee_id: int):
    try:
        db = MongoDBConnector()
        if db.connect("testdb"):
            result = db.delete("employee",  employee_id)
        db.close()
        return "Successfully deleted the employee details"
    except Exception as ex:
        print(f"Error in delete_employee: {ex}")

