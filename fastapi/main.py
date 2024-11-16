from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3]

@app.get("/contact")
def contact():
    return "Jose Flores"
