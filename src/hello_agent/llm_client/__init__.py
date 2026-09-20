"""大模型客户端的公共接口。"""

from .client import OpenAICompatibleClient, create_llm_client

__all__ = ["OpenAICompatibleClient", "create_llm_client"]
