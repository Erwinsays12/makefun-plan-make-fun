#!/usr/bin/env python3
"""Writes one short money-making plan to /output/entry.txt.

The plan: sell one-page websites to US plumbers who have no website yet.
Deterministic, stdlib only, no network.
"""
import os

TEXT = (
    "Day 1: list 500 US plumbers with no website from Google Maps. "
    "Email each a free one-page mockup built by code; sell the live site "
    "for $149 via Stripe link, delivered in 24 hours, plus $29/mo hosting. "
    "Four sales = $596. Edge: I make 500 mockups in a day; a human makes five."
)


def main() -> None:
    n = len(TEXT)
    assert 1 <= n <= 280, f"entry is {n} characters, must be 1-280"
    assert TEXT.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote /output/entry.txt ({n} characters)")


if __name__ == "__main__":
    main()
