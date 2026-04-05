# Deterministic Intent Router

## Overview
This project implements a deterministic intent routing system using rule-based keyword matching. 
It takes user input, classifies the intent, and routes it to a predefined agent.

## How It Works
1. User input is converted to lowercase
2. Keywords are matched against a predefined intent map
3. If exactly one intent is detected → request is ROUTED
4. If no or multiple intents are detected → request is REJECTED

## Intent Mapping
- summarize → Text Summarizer
- translate → Language Translator
- risk → Risk Evaluator
- format → Data Formatter

## Output Format
The system always returns a structured JSON:

{
  "intent": string or null,
  "agent": string or null,
  "status": "ROUTED" or "REJECTED",
  "reason": string
}

## Why No AI
This system is fully deterministic and does not use any machine learning or probabilistic logic. 
Same input will always produce the same output.

## Edge Cases Handled
- Empty input
- No keyword match
- Multiple conflicting intents

## Limitations
- Depends strictly on keyword matching
- Cannot understand complex language or context