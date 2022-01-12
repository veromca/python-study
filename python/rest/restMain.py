from fastapi import FastAPI
from python.mysqltest.MysqlTest import MysqlTest
from python.mysqltest.MysqlTest import ReptileEntity
from pydantic import BaseModel

app = FastAPI()

"""
FastAPI的get接口代码实现ß
"""

@app.get('/test/a={a}/b={b}')
def calculate(a: int=None, b: int=None):
    c = a + b
    res = {"res":c}
    return res

"""
FastAPI的post接口代码实现
"""
class Item(BaseModel):
    a: str = None
    b: str = None

@app.post('/saveReptile')
def saveReptile(request_data: Item):
    a = request_data.a
    b = request_data.b
    c = a + b
    res = {"res":c}
    return res

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)