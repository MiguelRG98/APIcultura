from fastapi import FastAPI
import uvicorn 
data = {'name': "Pedro", 'name2': "Juan"}
app = FastAPI()

@app.get("/datos")
def hello():
        print("Ingresa tu nombre: ")
        a = input()
        print("Hola, " + a)
