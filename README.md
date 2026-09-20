# hello-agent

Agent 项目学习。源码包位于 `src/hello_agent`。

## 运行

在项目根目录安装依赖：

```powershell
.\venv\Scripts\python.exe -m pip install -e .
```

在项目根目录 `.env` 配置 `LLM_MODEL_ID`、`LLM_API_KEY`、`LLM_BASE_URL`。
景点搜索另需 `TAVILY_API_KEY`，可放在同一 `.env` 文件中。

可编辑安装后，修改源码立即生效，导入不依赖当前工作目录。从项目根目录启动：

```powershell
.\venv\Scripts\python.exe -m hello_agent.chapter1.first_agent_test
```

PyCharm 使用模块名 `hello_agent.chapter1.first_agent_test`，工作目录设为项目根目录，解释器使用项目 `venv`。在这个已安装项目的虚拟环境中，也支持直接运行脚本。更换或重建虚拟环境后，需要重新执行安装命令。

`hello_agent` 为命名空间包，不要求 `__init__.py`；`llm_client/__init__.py` 用来导出公共接口。
