from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic

from routes import get_api,post_api,delete_api,put_api


app = FastAPI(root_path="/api_explore",
              title= "python",
              version="1.0.0")

security = HTTPBasic()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(get_api.router)
app.include_router(post_api.router)
app.include_router(delete_api.router)
app.include_router(put_api.router)


@app.get("/")
async def root():
    return {"message" : "Hello we are working on something cool!"}







if __name__ == "__main__":
    try:
        import uvicorn
        uvicorn.run("main:app", host="127.0.0.1", port=8000)
    except Exception as ex:
        print(ex)