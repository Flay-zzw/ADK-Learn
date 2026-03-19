from google.adk.agents.llm_agent import Agent
from google.adk.models import LiteLlm
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

import datetime
from zoneinfo import ZoneInfo


def get_current_time() -> dict:
    """获取当前北京时间。

    Returns:
        dict: status 和 report。
    """
    now = datetime.datetime.now(ZoneInfo("Asia/Shanghai"))
    return {
        "status": "success",
        "report": f"当前北京时间：{now.strftime('%Y-%m-%d %H:%M:%S')}",
    }


root_agent = Agent(
    model=LiteLlm(model="deepseek/deepseek-chat"),
    name='root_agent',
    description='你是一个 AI 对话助手',
    instruction='用中文回答用户问题',
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "@playwright/mcp@latest"
                    ]
                ),
                timeout=30,
            ),
        ),
        get_current_time
    ],
)


