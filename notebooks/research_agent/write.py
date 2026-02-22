
import json
from research_agent.prompts import build_write_prompt


def write_structured_answer(
    question: str,
    snippets: list[dict[str, str]],
    llm
) -> dict:

    prompt = build_write_prompt(question, snippets)

    response = llm.invoke(prompt)

    try:
        parsed = json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("LLM output is not valid JSON.")

    return parsed
