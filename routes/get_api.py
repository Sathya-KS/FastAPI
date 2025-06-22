from fastapi import FastAPI,APIRouter
from pydantic import BaseModel

from dependencies.db_call import SQLDatabaseConnection,MongoDBConnector

#app = FastAPI()

router = APIRouter(
                   prefix="/dev/api/v1/mongodb",
                   tags = ["dataaccessservice"],
                   responses = {404:{"description":"NotFound"}}
)


    
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


@router.get("/get_employee_details")
async def get_employee(employee_id:int):
    try:

        db = MongoDBConnector()
        if db.connect("testdb"):
            documents = db.find_all("employee",employee_id)
            print(documents)
            # if documents:
            #     for doc in documents:
            #         print(doc)
            db.close()
        return documents
    except Exception as ex:
        print(ex)



    




