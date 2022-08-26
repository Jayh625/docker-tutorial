from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

if __name__ == "__main__":
    hello_world()