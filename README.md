# Visualization Agent with Reflection - Chart Improvement

This activity demonstrates the reflection design pattern for data visualization, where one LLM generates matplotlib charts and another critiques and improves them through iterative feedback.

## Overview

The visualization agent follows a reflection-based workflow:
1. **Generate**: Create matplotlib code from natural language instruction
2. **Execute**: Run the code to generate the initial chart
3. **Evaluate**: Have another LLM critique the chart by analyzing the image
4. **Refine**: Improve the visualization code based on feedback
5. **Compare**: Generate side-by-side comparison of original vs improved charts

## Prerequisites

Ensure you have a `.env` file in the root of the repository with API keys for:
- `OPENAI_API_KEY` - OpenAI API access
- `ANTHROPIC_API_KEY` - Anthropic Claude access

Install dependencies from the root directory:
```bash
pip install -r requirements.txt
```

## Files

- `reflection_chart_generation.ipynb` - Main notebook demonstrating visualization reflection workflow
- `utils.py` - Utility functions for image processing and chart generation
- Generated outputs:
  - `chart_v1.jpg` - Initial visualization
  - `chart_v2_chart.jpg` - Improved visualization after feedback

## Data Schema

`coffee_sales.csv` contains:
- `date` (M/D/YY) - Sale date
- `time` (HH:MM) - Sale time
- `cash_type` - Payment method (card/cash)
- `card` - Credit card identifier
- `price` - Sale amount in dollars
- `coffee_name` - Type of coffee drink
- Calculated: `quarter`, `month`, `year`

## Running the Activity

1. **Open and run the notebook**:
   - Open `reflection_chart_generation.ipynb.ipynb` in Jupyter
   - Run all cells sequentially

2. **The notebook will**:
   - Load the gapminder dataset
   - Execute visualization workflows with different model combinations
   - Generate charts and improvement feedback

   ```

## Key Learning Points

- **Visual Reflection**: How LLMs can critique visual content through image analysis
- **Code Improvement**: Iterative enhancement of matplotlib code based on feedback
- **Multi-Modal AI**: Using vision-capable models to evaluate chart quality
- **Model Specialization**: Different models for generation vs evaluation tasks
- **Comparative Analysis**: Side-by-side evaluation of improvements

## Expected Outputs

The workflow demonstrates visual improvement through reflection:

1. **Original Chart**: Initial visualization with potential issues (formatting, clarity, etc.)
2. **Evaluation Feedback**: Detailed critique of chart quality, readability, and effectiveness
3. **Refined Chart**: Improved version addressing the feedback points

## Example Improvements

Common enhancements made through reflection:
- Better color schemes and contrast
- Improved axis labels, legends and titles
- Enhanced data presentation clarity
- More professional styling and formatting
- Better chart type selection for the data

## Model Combinations Tested

The notebook compares different LLM pairings:
- GPT-4o-mini (generation) + GPT-4o (evaluation)

This demonstrates how different AI models can collaborate effectively in a multi-agent reflection system.