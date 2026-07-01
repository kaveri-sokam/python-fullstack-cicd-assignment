from fastapi import FastAPI

app = FastAPI(title="Student Management API")

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/students")
def students():
    return [{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]
