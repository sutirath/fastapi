from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.post("/")
def home():
    return {"message":"Hello TutLinks.com"}
