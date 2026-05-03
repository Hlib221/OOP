from google.adk.agents.llm_agent import Agent

def safe_divide(a: float, b: float) -> dict:
    """Ділить два числа з перевіркою на нуль."""
    if b == 0:
        return {"error": "Ділення на нуль неможливе", "result": None}
    return {"result": a / b, "error": None}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='safe_calculator',
    description="Безпечний калькулятор",
    instruction="""
    Ти калькулятор. Використовуй інструмент safe_divide для ділення чисел. 
    Якщо отримуєш помилку (наприклад, ділення на нуль), чемно повідом про це користувача.
    """,
    tools=[safe_divide]
)