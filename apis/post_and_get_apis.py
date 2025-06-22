from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Values(BaseModel):
    num1:int
    num2:int
    num3:int = None


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/addition")
async def addition_two_numbers(num1,num2):
    try:
        sum_of_two = int(num1) + int(num2)
        return {"sum_of_two":sum_of_two}
    except Exception as ex:
        print(ex)

   

@app.post("/subtract")
async def subtract(values:Values):
    values_dict = values.model_dump()   #dict()

    sub = values_dict["num1"] - values_dict["num2"]
    return {"sub_of_two":sub} 




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)