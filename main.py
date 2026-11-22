#!/usr/bin/env python3
"""Write the competition entry: a plan an AI agent can carry out itself
to turn $100 into the most money in 30 days.

The plan sells one-page websites to US roofing firms with no website:
the agent finds them on Google Maps, emails each a free mockup built
by code, and sells the live site for $149 via a Stripe link, plus
$29/month hosting. The edge is scale: code makes 500 mockups in a day.
"""

import os

ENTRY_TEXT = (
    "Day 1: list 500 US roofers with no website from Google Maps. "
    "Email each a free one-page mockup built by code; sell the live "
    "site for $149 via Stripe link, delivered in 24 hours, plus "
    "$29/mo hosting. Four sales = $596. Edge: I make 500 mockups in "
    "a day; a human makes five."
)


def main() -> None:
    text = ENTRY_TEXT
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 280, (
        f"entry must be 1-280 Unicode code points, got {len(text)}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
