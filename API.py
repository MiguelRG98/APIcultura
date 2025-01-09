from fastapi import FastAPI
import uvicorn 
import pandas as pd
df = pd.read_csv("datos.csv")
df = df.to_json()
app = FastAPI()

@app.get("/datos")
def hello():
        return df
