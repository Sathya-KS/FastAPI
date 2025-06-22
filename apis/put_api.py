from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample data (replace with your actual data source)
users = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}

@app.put("/users/{user_id}")
async def update_user(user_id: str, user_data: dict):


    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id].update(user_data)
    return users[user_id]

# Example usage:
# To update user1's age to 31:
# Send a PUT request to /users/user1 with the following JSON in the request body:
# {
#     "age": 31
# }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)