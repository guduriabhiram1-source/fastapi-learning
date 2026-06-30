from fastapi import FastAPI

app = FastAPI()

@app.get("/student")
def student():
    return {
        "id": 1,
        "name": "Abhi",
        "age": 19,
        "course": "Python"
    }