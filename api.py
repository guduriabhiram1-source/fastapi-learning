from fastapi import FastAPI
app=FastAPI()
@app.get("/about")
def about():
    return{
        "company":"openai",
        "framework":"FastAPI",
        "language":"python"
    }
