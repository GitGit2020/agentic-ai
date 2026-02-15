# Agentic AI: Reflection and Tool Use

This repository contains practical notebooks that demonstrate the core control patterns behind agentic AI systems.

Rather than focusing on frameworks, these notebooks break down the fundamental building blocks that enable agents to reason, extend capabilities, and improve outputs.

---

## Notebooks Overview

### 1️⃣ Reflection — Chart Generation and Improvement

`reflection_chart_generation.ipynb`

Demonstrates the **reflection design pattern**, where:

- One LLM generates a visualization
- Another LLM evaluates the result
- The system revises the output based on structured feedback

Control loop introduced:

Generate → Evaluate → Revise

Key ideas:
- Output validation as a control mechanism
- Structured critique of artifacts (charts)
- Separation of generation and evaluation roles
- Iterative refinement

---

### 2️⃣ Tool Use — Retail Agent with Multiple Tools

`tool_use_retail_agent.ipynb`

Demonstrates how agents extend their capabilities using deterministic tools over external data.

The notebook introduces:

Interpret → Decide → Execute → Integrate

Key ideas:
- Detecting when model knowledge is insufficient
- Selecting the appropriate tool from multiple options
- Structured argument contracts
- Integrating tool outputs into final reasoning
- Handling tool failures gracefully
- Avoiding unnecessary tool calls

The retail example uses transactional data to simulate interaction with an external system.

---

## Core Concepts Covered

Across both notebooks, the following agentic principles are demonstrated:

- **Control Loops**: Structured reasoning before and after actions
- **Separation of Concerns**: Generation vs evaluation vs execution
- **Deterministic Tools**: External capabilities as strict interfaces
- **Structured Outputs**: JSON-based decision making
- **Failure Handling**: Robust behavior when tools return missing data
- **Conditional Capability Use**: Agents must decide when to act

---

## Prerequisites

Create a `.env` file in the root of the repository with:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`

Install dependencies:

```bash
pip install -r requirements.txt
