# REVIEW PACKET

## Entry Point
main.py

## Core Execution Flow
main.py → router.py → classify_intent() → structured JSON output

## What Was Built
A deterministic intent routing system that classifies user input using rule-based keyword matching 
and maps it to predefined agents. The system ensures complete explainability and avoids any AI or probabilistic logic.

## Live Example

Input:
Summarize this document

Output:
{
  "intent": "summarize",
  "agent": "Text Summarizer",
  "status": "ROUTED",
  "reason": "Keyword 'summarize' detected"
}

## Failure Cases

1. Empty Input
Output: REJECTED with reason "Empty input"

2. No Matching Keyword
Example: "Tell me a joke"
Output: REJECTED with reason "No matching keyword found"

3. Conflicting Intents
Example: "Summarize and translate"
Output: REJECTED with reason "Conflicting intents detected"

## Proof
Run main.py and test using multiple inputs. 
The system consistently produces deterministic and explainable outputs.