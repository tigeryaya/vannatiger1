from vanna import VannaDB_VectorStore, VannaBase

# 自定义 LLM 类
class MyCustomLLM(VannaBase):
    def __init__(self, config=None):
        super().__init__(config=config)
        # 可以添加你自己的 LLM 初始化代码

    def submit_prompt(self, prompt, **kwargs) -> str:
        # 这里要处理向 LLM 提交请求的逻辑
        return "这是你的 LLM 响应"

# 初始化 Vanna 类，继承 VannaDB_VectorStore 和自定义的 MyCustomLLM 类
class MyVanna(VannaDB_VectorStore, MyCustomLLM):
    def __init__(self, config=None):
        MY_VANNA_MODEL = 'llama70b.gaia.domains'  # 使用你自己的 LLM 模型
        MY_VANNA_API_KEY = 'gaia-OTBiYjlmZDEtNTc3OS00MjI5LWI0NDgtZDIxNTNmYjEwZDRj-IYuaA5AxGFTywJWq'  # 你的 API 密钥
        VannaDB_VectorStore.__init__(self, vanna_model=MY_VANNA_MODEL, vanna_api_key=MY_VANNA_API_KEY, config=config)
        MyCustomLLM.__init__(self, config=config)

# 实例化 Vanna 类
vn = MyVanna()

# 示例：连接到 PostgreSQL 数据库
vn.connect_to_postgres(
    host='localhost', 
    dbname='vanna1', 
    user='tiger', 
    password='tigerhate1007', 
    port='5432'
)

# 执行 SQL 查询
query = "Show me all users"
result = vn.ask(question=query)  # 使用 vanna.ask() 提交自然语言查询
print(result) 
