# Prompt Evaluation Tool

## Overview
This project is a rule-based system designed to simulate and evaluate AI-generated responses based on clarity, depth, and technical relevance.

## Motivation
The goal was to understand how AI outputs can be analyzed, tested, and improved by identifying weak responses and refining evaluation logic.

## Features
- Simulated AI responses for different prompts
- Rule-based scoring system (0–3 scale)
- Evaluation based on:
  - Clarity
  - Depth
  - Technical relevance
- Penalty for vague or low-quality responses
- Results stored in structured JSON format

## How It Works
1. A prompt is passed into the system
2. A simulated AI response is generated
3. The response is evaluated using defined rules
4. A score and reasoning are assigned
5. Results are stored in `results.json`

## Example Output

Prompt: Explain APIs in simple terms  
Score: 3/3  
Reasons: Good length, Clear explanation, Technically relevant  

Prompt: Explain blockchain  
Score: 1/3  
Reasons: Penalized for vague response  

## Tech Stack
- Python
- JSON

## Future Improvements
- Integrate real AI APIs instead of simulated responses
- Add prompt comparison and ranking
- Improve scoring using machine learning

## Author
Sarthak Arya