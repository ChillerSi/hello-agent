# 大模型客户端

使用包导入，无需修改 sys.path：

```python
from hello_agent.llm_client import create_llm_client

client = create_llm_client()
try:
    print(client.generate(prompt="你好", system_prompt="你是中文助手。"))
finally:
    client.close()
```

默认使用 `load_dotenv()` 自动查找 `.env`，通过 `os.getenv()` 读取配置。
优先级：显式参数 > 已有环境变量 > .env。
也可传入 `create_llm_client(env_file="配置路径", model="模型名称")`。
已有环境变量不会被覆盖，修改 `.env` 后请重启进程。

`client.client` 提供原生 SDK 接口；`generate()` 用于文本回复。
配置缺失、API 错误和空回复均会抛出异常。
启动方式见项目根目录 README.md。
