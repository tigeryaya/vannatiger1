# vannatiger1

系統—Windows(Linux)
 
打開powershell
→wsl -d ubuntu
//進入到linux
 
安裝set up
條件—LLM(自訂),database(Postgres)
 
→pip3 install 'vanna[postgres]'
安裝vanna
→sudo apt install postgresql postgresql-contrib
安裝postgres
 
創建python檔
from vanna import VannaDB_VectorStore, VannaBase
 
class MyCustomLLM(VannaBase):
    def __init__(self, config=None):
        super().__init__(config=config)
 
    def submit_prompt(self, prompt, **kwargs) -> str:
        return "这是你的 LLM 响应"
 
# 初始化 Vanna 类，继承 VannaDB_VectorStore 和自定义的 MyCustomLLM 类
class MyVanna(VannaDB_VectorStore, MyCustomLLM):
    def __init__(self, config=None):
        MY_VANNA_MODEL = 'llama70b.gaia.domains'  # 使用你自己的 LLM 模型
        MY_VANNA_API_KEY = 'your_api_key'  # 你的 API 密钥
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key=MY_VANNA_API_KEY, config=config)
        MyCustomLLM.__init__(self, config=config)
 
# 实例化 Vanna 类
vn = MyVanna()
 
# 示例：连接到 PostgreSQL 数据库
vn.connect_to_postgres(
    host='your_host', //ex:localhost
    dbname='your_dbname',
    user='your_user',
    password='your_password',
    port='your_port'//默認是5432
)
 
# 执行 SQL 查询
result = vn.ask(question="SELECT * FROM my_table WHERE name = 'John Doe'")
print(result)
 
 
在Linux連結vanna和postgres→
psql -h your_host -U user_name -d vanna -p 5432
 
執行python檔
→
Python3 檔名.py
 
 —-------------------------------------
以上是用python方式詢問
啟動後到localhost:8084
