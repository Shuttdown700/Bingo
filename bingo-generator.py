#!/usr/bin/env python3

import random
import sys
from datetime import datetime

# Hardcoded Title as requested
BINGO_TITLE = "Innovation Buzzword Bingo"

def generate_card_html(terms, date_str, is_last):
    """Creates the HTML for a single card table centered on a page."""
    card_terms = terms[:12] + ["FREE SPACE"] + terms[12:24]
    pagebreak = "" if is_last else " newpage"
    
    # We add a 'print-page' wrapper to handle the vertical centering
    html = [f'<div class="print-page{pagebreak}">',
            '  <div class="card-container">',
            '    <div class="card-header">',
            f'      <h1>{BINGO_TITLE}</h1>',
            '      <p class="unit-text">3rd Infantry Division</p>',
            f'      <p class="date">{date_str}</p>',
            '    </div>',
            '    <table>']
    
    for i in range(0, 25, 5):
        html.append('      <tr>')
        for term in card_terms[i:i+5]:
            cls = ' class="free-space"' if term == "FREE SPACE" else ""
            html.append(f'        <td{cls}>{term}</td>')
        html.append('      </tr>')
        
    html.append('    </table>\n  </div>\n</div>')
    return "\n".join(html)

def main():
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} [terms.txt] [output.html] [count]")
        sys.exit(1)

    # 1. Load the Bingo terms
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            terms = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading terms: {e}")
        sys.exit(1)

    if len(terms) < 24:
        print(f"Error: Found only {len(terms)} terms. Need at least 24.")
        sys.exit(1)

    # 2. Load the HTML template
    try:
        with open('template.html', 'r', encoding='utf-8') as f:
            template = f.read()
    except Exception as e:
        print(f"Error: template.html not found ({e})")
        sys.exit(1)

    # 3. Process logic
    all_cards_html = []
    num_cards = int(sys.argv[3])
    date_str = datetime.now().strftime("%d %B %Y").upper()

    for i in range(num_cards):
        random.shuffle(terms)
        all_cards_html.append(generate_card_html(terms, date_str, i == num_cards - 1))

    # 4. Inject into template and save
    final_html = template.replace("{{TITLE}}", BINGO_TITLE)
    final_html = final_html.replace("{{CARDS}}", "\n".join(all_cards_html))

    try:
        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Success! {num_cards} ink-efficient cards generated in '{sys.argv[2]}'.")
    except Exception as e:
        print(f"Error writing output: {e}")

if __name__ == "__main__":
    main()