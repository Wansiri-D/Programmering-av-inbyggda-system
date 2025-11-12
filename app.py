from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK"}

@app.post("/sensor")
async def sensor(req: Request):
    data = await req.json()
    print(data)

    return {"status": "OK"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
