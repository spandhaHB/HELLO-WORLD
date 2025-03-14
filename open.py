from fastapi import FastAPI 
from pydantic import BaseModel
app = FastAPI()

class Barang(BaseModel):
    nama: str
    jumlah: int

@app.get("/")
def read_root():
    return{"hello world"} 
@app.post('/barang/')
def nama_barang(barang: Barang):
    return{"data": barang}
@app.get('/hello/')
def hello(nama: str):
    return {
        "message": nama
    }