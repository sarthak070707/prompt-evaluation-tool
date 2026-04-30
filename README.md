# Prompt Evaluation Tool

## Overview
This project is a rule-based system designed to simulate and evaluate AI-generated responses. It focuses on improving output reliability by identifying weak responses and refining evaluation logic through iterative testing.

## Problem Statement
AI-generated responses can often appear correct while lacking clarity, depth, or technical relevance. Simple evaluation methods may incorrectly score vague or generic responses as high-quality outputs.

This project was built to address:
- False positives in response evaluation
- Lack of structured scoring for AI outputs
- Difficulty in identifying weak or vague responses

## Solution
A prompt evaluation system was developed to:
- Simulate AI responses for different prompts
- Evaluate responses using rule-based scoring
- Penalize vague or low-quality outputs
- Provide reasoning behind each score
- Store results in structured JSON format for analysis

## How It Works
1. A prompt is provided as input  
2. A simulated AI response is generated  
3. The response is evaluated based on:
   - **Clarity** (definition or explanation patterns)
   - **Depth** (response length)
   - **Technical relevance** (keyword-based detection)
4. A penalty is applied for vague or generic responses  
5. Final score (0–3) and reasoning are generated  
6. Results are stored in `results.json`  

## Key Features
- Rule-based evaluation system
- Scoring logic with reasoning output
- Detection and penalization of vague responses
- Structured output storage using JSON
- Iterative refinement of evaluation rules

## Example Output

**Prompt:** Explain APIs in simple terms  
**Score:** 3/3  
**Reasons:** Good length, Clear explanation, Technically relevant  

**Prompt:** Explain blockchain  
**Score:** 1/3  
**Reasons:** Good length, Clear explanation, Technically relevant, Strong penalty for vague response  

## Tech Stack
- Python  
- JSON  

## Key Learnings
- Designed a system to evaluate AI outputs using rule-based logic  
- Identified and fixed scoring flaws (false positives for generic responses)  
- Improved evaluation reliability through penalty-based scoring  
- Structured and stored evaluation results for analysis  

## Future Improvements
- Integrate real AI APIs instead of simulated responses  
- Replace rule-based scoring with ML-based evaluation  
- Add prompt comparison and ranking system  
- Build a simple UI for interaction and visualization  

## Author
Sarthak Arya
