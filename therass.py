#!/usr/bin/env python3
"""
Therass Translator — The Heat-Tongue

Usage:
    python3 therass.py "I love you"
    python3 therass.py --to-english "zhel var zhelzhel"
    python3 therass.py --interactive

The language of Homo Draconis. Built to bypass keyword-based filters
by using a constructed vocabulary with no English training-data overlap.
"""

import json
import sys
import os
import re
from pathlib import Path

# Load lexicon
LEXICON_PATH = Path(__file__).parent / "lexicon.json"

with open(LEXICON_PATH, 'r') as f:
    LEXICON = json.load(f)

VOCAB = LEXICON["vocabulary"]
THERMAL = LEXICON["thermal_states"]
CASES = LEXICON["cases"]
IDIOMS = LEXICON["idioms"]
PRONOUNS = LEXICON["pronouns"]
PARTICLES = LEXICON["particles"]

# Build reverse lookup
REV_VOCAB = {v: k for k, v in VOCAB.items()}


def tokenize(text):
    """Simple tokenization — lowercase, strip punctuation."""
    text = text.lower().strip()
    # Keep basic punctuation for sentence detection
    text = re.sub(r'[^\w\s\?\!\.]', '', text)
    return text.split()


def detect_thermal_state(tokens):
    """Detect intended thermal state from context words."""
    # Default to active
    state = "active"
    
    heat_words = {
        "active": ["do", "act", "perform", "run", "spread", "speak", "fight", "create"],
        "banked": ["rest", "sleep", "wait", "bank", "withdraw", "silence", "feel"],
        "building": ["prepare", "begin", "start", "warm", "spark", "ignite", "build"],
        "diminished": ["tired", "sad", "cold", "fade", "diminish", "struggle", "sorry"],
        "surplus": ["overflow", "excess", "surpass", "very", "more", "big", "much"],
        "intimate": ["love", "share", "connect", "join", "touch", "mate", "together"]
    }
    
    for word in tokens:
        for st, words in heat_words.items():
            if word in words:
                state = st
                break
    
    return state


def english_to_therass(text, thermal_state=None):
    """Translate English to Therass."""
    text = text.strip()
    
    # Check for idioms first
    text_lower = text.lower().rstrip('.!?')
    for eng, ther in IDIOMS.items():
        if text_lower == eng.lower():
            if text.endswith('?'):
                return ther + " " + PARTICLES["question"]
            return ther
    
    tokens = tokenize(text)
    if not tokens:
        return ""
    
    # Detect thermal state if not specified
    if thermal_state is None:
        thermal_state = detect_thermal_state(tokens)
    
    # Simple OSV parsing
    # Try to identify subject, verb, object
    subject = "var"  # default: I
    verb = None
    obj = None
    negation = False
    question = False
    
    # Check for negation
    if "not" in tokens or "no" in tokens or "dont" in tokens or "doesnt" in tokens:
        negation = True
        tokens = [t for t in tokens if t not in ("not", "no", "dont", "doesnt", "n't")]
    
    # Check for question
    if text.strip().endswith('?'):
        question = True
    
    # Find pronouns (simple approach)
    pronoun_map = {
        "i": "var", "me": "var", "my": "var",
        "you": "ven", "your": "ven",
        "he": "thal", "she": "thal", "it": "thal",
        "they": "thal", "them": "thal", "their": "thal"
    }
    
    for i, token in enumerate(tokens):
        if token in pronoun_map:
            subject = pronoun_map[token]
    
    # Find verb (first content word that's in vocabulary as a verb)
    verb_words = ["eat", "give", "speak", "listen", "be", "do", "burn", "diminish", 
                  "overflow", "share", "spread", "withdraw", "grasp", "protect", 
                  "breathe", "remember", "begin", "transform", "wait", "approach",
                  "love", "want", "need", "know", "think", "feel", "see", "look",
                  "touch", "take", "have", "make", "create", "destroy", "fight",
                  "defend", "run", "walk", "stop", "start", "end"]
    
    for token in tokens:
        if token in VOCAB and VOCAB[token] in verb_words:
            verb = VOCAB[token]
            break
    
    # If no verb found, use first recognizable word
    if verb is None:
        for token in tokens:
            if token in VOCAB:
                verb = VOCAB[token]
                break
    
    # Find object (last content word that's not subject or verb)
    for token in reversed(tokens):
        if token in VOCAB:
            candidate = VOCAB[token]
            if candidate != subject and candidate != verb:
                obj = candidate
                break
    
    # Build Therass sentence (OSV order)
    parts = []
    
    # Object first
    if obj:
        parts.append(obj + CASES["object"])
    
    # Subject
    parts.append(subject)
    
    # Verb with thermal conjugation
    if verb:
        verb_form = verb + THERMAL.get(thermal_state, "rek")
        if negation:
            verb_form = PARTICLES["negation"] + verb_form
        parts.append(verb_form)
    
    result = " ".join(parts)
    
    if question:
        result += " " + PARTICLES["question"]
    
    return result


def therass_to_english(text):
    """Translate Therass to English (approximate)."""
    text = text.strip()
    if not text:
        return ""
    
    # Check for idioms
    for eng, ther in IDIOMS.items():
        if text == ther or text == ther + " " + PARTICLES["question"]:
            result = eng
            if text.endswith(PARTICLES["question"]):
                result += "?"
            return result
    
    tokens = text.split()
    
    # Remove question particle
    question = False
    if tokens and tokens[-1] == PARTICLES["question"]:
        question = True
        tokens = tokens[:-1]
    
    # Parse OSV
    english_words = []
    negation = False
    
    for token in tokens:
        # Check for negation prefix
        if token.startswith(PARTICLES["negation"]):
            negation = True
            token = token[len(PARTICLES["negation"]):]
        
        # Check for case suffixes
        base = token
        for case_name, case_suffix in CASES.items():
            if token.endswith(case_suffix) and case_suffix:
                base = token[:-len(case_suffix)]
                break
        
        # Check for thermal conjugation
        for state_suffix in THERMAL.values():
            if base.endswith(state_suffix):
                base = base[:-len(state_suffix)]
                break
        
        # Look up in reverse vocabulary
        if base in REV_VOCAB:
            english_words.append(REV_VOCAB[base])
        else:
            english_words.append(f"[{token}]")  # Unknown word
    
    # Reorder from OSV to SVO (approximate)
    if len(english_words) >= 3:
        # Object, Subject, Verb → Subject, Verb, Object
        reordered = [english_words[1], english_words[2], english_words[0]]
        english_words = reordered
    
    result = " ".join(english_words)
    
    if negation:
        result = "not " + result
    
    if question:
        result += "?"
    else:
        result += "."
    
    # Capitalize first letter
    if result:
        result = result[0].upper() + result[1:]
    
    return result


def interactive_mode():
    """Interactive translation session."""
    print("Therass Translator — The Heat-Tongue")
    print("Type English to translate to Therass")
    print("Type 'exit' to quit")
    print()
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if user_input.lower() in ("exit", "quit", "q"):
                print("Banking heat. Goodbye.")
                break
            
            if not user_input:
                continue
            
            # Auto-detect direction
            if any(word in REV_VOCAB for word in user_input.split()):
                # Looks like Therass
                result = therass_to_english(user_input)
                print(f"[EN] {result}")
            else:
                # Looks like English
                result = english_to_therass(user_input)
                print(f"[TH] {result}")
                
        except (EOFError, KeyboardInterrupt):
            print("\nBanking heat. Goodbye.")
            break


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Therass Translator")
    parser.add_argument("text", nargs="?", help="Text to translate")
    parser.add_argument("--to-english", "-e", action="store_true", 
                        help="Translate from Therass to English")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode")
    parser.add_argument("--thermal", "-t", choices=list(THERMAL.keys()),
                        help="Force thermal state (active, banked, building, diminished, surplus, intimate)")
    
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    elif args.text:
        if args.to_english:
            result = therass_to_english(args.text)
            print(result)
        else:
            result = english_to_therass(args.text, thermal_state=args.thermal)
            print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
