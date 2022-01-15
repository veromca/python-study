from fastapi import FastAPI
from python.mysqltest.MysqlTest import MysqlTest
from python.mysqltest.MysqlTest import ReptileEntity
from pydantic import BaseModel
from python.baseconfig.logger import Logger
log = Logger(__name__)
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
    color: str = None
    size: str = None

@app.get('/addLogs/count={count}')
def addLogs(count: int=None):
    for i in range(count):
        log.info("saveReptile API "+str(i)+" success")
    res = {"res: add "+str(count)+' success!'}
    return res

@app.post('/saveReptile')
def saveReptile(request_data: Item):
    log.info("saveReptile API 参数："+request_data.color+','+request_data.size)
    color = request_data.color
    size = request_data.size
    res = {"res: color-"+color+",size-"+size}
    return res

if __name__ == '__main__':
    import uvicorn
    log.info("启动...")
    uvicorn.run(app=app,
                host="0.0.0.0",
                port=8080,
                workers=1)