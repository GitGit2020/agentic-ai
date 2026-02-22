
def build_write_prompt(question: str, snippets: list[dict[str, str]]) -> str:
    context_block = ""

    for i, s in enumerate(snippets):
        context_block += f"""
Source {i+1}:
Title: {s['title']}
URL: {s['url']}
Content: {s['content']}
"""

    return f"""
You are a financial research analyst.

Using only the information provided in the sources below,
write a structured financial analysis.

Question:
{question}

Sources:
{context_block}

Instructions:
- Provide a final_answer of at most 250 words.
- Extract at least 3 key_facts summarizing the main causes.
- Include the URLs of the sources used.
- Do not invent facts not supported by the sources.
- Be concise and factual.

Return valid JSON only in this format:

{{
  "final_answer": "...",
  "key_facts": ["...", "...", "..."],
  "sources": ["url1", "url2"]
}}
"""


def build_reflection_prompt(
    question: str,
    snippets: list[dict[str, str]],
    draft_output: dict
) -> str:

    context_block = ""

    for i, s in enumerate(snippets):
        context_block += f"""
Source {i+1}:
Title: {s['title']}
URL: {s['url']}
Content: {s['content']}
"""

    return f"""
You are reviewing a financial research answer for accuracy and completeness.

Question:
{question}

Sources:
{context_block}

Draft Answer:
{draft_output}

Tasks:
1. Identify if any key_facts are unsupported by the sources.
2. Identify if important causes are missing.
3. Improve clarity if necessary.
4. Ensure final_answer is 250 words or fewer.
5. Ensure at least 3 key_facts.
6. Do not add information not supported by the sources.

Return improved JSON only in the same format:

{{
  "final_answer": "...",
  "key_facts": ["...", "...", "..."],
  "sources": ["url1", "url2"]
}}
"""
