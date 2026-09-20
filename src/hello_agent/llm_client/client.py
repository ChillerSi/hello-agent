"""可复用的 OpenAI 兼容客户端，默认自动查找 .env。"""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


class OpenAICompatibleClient:
    """封装文本生成；client 属性可用于 tools 等原生 SDK 调用。"""

    def __init__(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def generate(self, prompt: str, system_prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            stream=False,
        )
        if not response.choices or not response.choices[0].message.content:
            raise ValueError("模型未返回文本内容。")
        return response.choices[0].message.content

    def close(self) -> None:
        self.client.close()


def create_llm_client(
    env_file: str | Path | None = None,
    *,
    model: str | None = None,
    api_key: str | None = None,
    base_url: str | None = None,
) -> OpenAICompatibleClient:
    """通过 load_dotenv 加载配置；显式参数 > 已有环境变量 > .env。"""
    if env_file is None:
        load_dotenv()
    else:
        path = Path(env_file)
        if not path.is_file():
            raise FileNotFoundError(f"配置文件不存在：{path}")
        load_dotenv(dotenv_path=path, override=False)
    resolved = {}
    for name, explicit in (
        ("LLM_MODEL_ID", model),
        ("LLM_API_KEY", api_key),
        ("LLM_BASE_URL", base_url),
    ):
        value = explicit if explicit is not None else os.getenv(name)
        if not value or not value.strip():
            raise ValueError(f"缺少配置 {name}，请在 .env 或环境变量中设置。")
        resolved[name] = value.strip()
    return OpenAICompatibleClient(
        model=resolved["LLM_MODEL_ID"],
        api_key=resolved["LLM_API_KEY"],
        base_url=resolved["LLM_BASE_URL"],
    )
