from fastapi import FastAPI, File

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}
