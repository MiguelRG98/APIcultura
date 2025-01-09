from fastapi import FastAPI
import uvicorn 
data = {'name': "Pedro", 'name2': "Juan"}
app = FastAPI()

@app.get("/my-first-api")
def hello():
  return data
