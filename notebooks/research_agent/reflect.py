
import json
from research_agent.prompts import build_reflection_prompt


def reflect_and_improve(
    question: str,
    snippets: list[dict[str, str]],
    draft_output: dict,
    llm
) -> dict:

    prompt = build_reflection_prompt(
        question=question,
        snippets=snippets,
        draft_output=draft_output
    )

    response = llm.invoke(prompt)

    try:
        parsed = json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("Reflection output is not valid JSON.")

    return parsed
