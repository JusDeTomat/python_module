#!/usr/bin/env python3

import sys


def score_analytics():
    print("=== Player Score Analytics ===")
    try:
        scores = [int(x) for x in sys.argv[1:]]
        if (scores == []):
            raise ValueError("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
        print(f"Scores processed: {scores}\n\
    Total players: {len(scores)}\n\
    Total score: {sum(scores)}\n\
    Average score: {sum(scores) / len(scores)}\n\
    High score: {max(scores)}\n\
    Low score: {min(scores)}\n\
    Score range: {max(scores) - min(scores)}")
    except ValueError as e:
        print(e)


if (__name__ == "__main__"):
    score_analytics()
