from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext

def save_user_preference(tool_context: ToolContext, preference_type: str, value: str) -> dict:
    """Зберігає вподобання користувача."""
    existing_state = tool_context.state.get(preference_type, [])
    tool_context.state[preference_type] = existing_state + [value]
    return {"status": "success", "message": f"Збережено {preference_type}"}

def recall_preference(tool_context: ToolContext, preference_type: str) -> dict:
    """Згадує вподобання користувача."""
    preferences = tool_context.state.get(preference_type, [])
    if preferences:
        return {"status": "success", "message": f"Згадано: {', '.join(preferences)}"}
    return {"status": "error", "message": "Нічого не знайдено"}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='conversation_agent',
    description="Агент з пам'яттю",
    instruction="""
    Ти дружній асистент. Запам'ятовуй ім'я та хобі користувача через save_user_preference.
    Коли питають 'як мене звати' - використовуй recall_preference.
    """,
    tools=[save_user_preference, recall_preference],
)