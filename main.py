from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
def main():
    return str('Hello World!! ')


