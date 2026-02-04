#!/usr/bin/env python3

import os
import random
import sys
from datetime import datetime

# Hardcoded Global Variables
BINGO_TITLE = "Innovation Buzzword Bingo"
ORGANIZATION_NAME = "Marne Innovation Center"
BINGO_CARD_WIDTH = 5
FILEPATH_TEMPLATE = os.path.join(os.path.dirname(__file__), 'template.html')

def generate_card_html(terms, bool_is_last):
    """Creates the HTML for a single card table centered on a page."""
    card_terms = terms[:12] + ["FREE SPACE"] + terms[12:24]
    pagebreak = "" if bool_is_last else " newpage"
    
    date_str = datetime.now().strftime("%d %B %Y").upper()
    html = [f'<div class="print-page{pagebreak}">',
            '  <div class="card-container">',
            '    <div class="card-header">',
            f'      <h1>{BINGO_TITLE}</h1>',
            f'      <p class="unit-text">{ORGANIZATION_NAME}</p>',
            f'      <p class="date">{date_str}</p>',
            '    </div>',
            '    <table>']
    
    for i in range(0, BINGO_CARD_WIDTH*BINGO_CARD_WIDTH, BINGO_CARD_WIDTH):
        html.append('      <tr>')
        for term in card_terms[i:i+BINGO_CARD_WIDTH]:
            cls = ' class="free-space"' if term == "FREE SPACE" else ""
            html.append(f'        <td{cls}>{term}</td>')
        html.append('      </tr>')
        
    html.append('    </table>\n  </div>\n</div>')
    return "\n".join(html)

def main():
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} [bingo_terms.txt] [output.html] [count]")
        sys.exit(1)

    try:
        filepath_terms = sys.argv[1]
        with open(filepath_terms, 'r', encoding='utf-8') as f:
            terms = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading terms from '{filepath_terms}': {e}")
        sys.exit(1)

    if len(terms) < BINGO_CARD_WIDTH*BINGO_CARD_WIDTH-1:
        print(f"Error: Found only {len(terms)} terms. Need at least {BINGO_CARD_WIDTH*BINGO_CARD_WIDTH-1}.")
        sys.exit(1)

    try:
        with open(FILEPATH_TEMPLATE, 'r', encoding='utf-8') as f:
            template = f.read()
    except Exception as e:
        print(f"Error with template.html at '{FILEPATH_TEMPLATE}': {e}")
        sys.exit(1)

    all_cards_html = []
    num_cards = int(sys.argv[3])

    for i in range(num_cards):
        random.shuffle(terms)
        bool_is_last = (i == num_cards - 1)
        all_cards_html.append(generate_card_html(terms, bool_is_last))

    final_html = template.replace("{{TITLE}}", BINGO_TITLE)
    final_html = final_html.replace("{{CARDS}}", "\n".join(all_cards_html))

    try:
        filepath_output = sys.argv[2]
        with open(filepath_output, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Success! {num_cards} printable Bingo cards generated in '{filepath_output}'")
    except Exception as e:
        print(f"Error writing output to '{filepath_output}': {e}")

if __name__ == "__main__":
    main()