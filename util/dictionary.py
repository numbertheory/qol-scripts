import sys
import re
from CoreServices import DCSCopyTextDefinition

def format_definition(word):
    # Fetch the raw text from macOS CoreServices
    raw = DCSCopyTextDefinition(None, word, (0, len(word)))

    if not raw:
        return f"\033[31mNo definition found for '{word}'.\033[0m"

    # ANSI Color Codes
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

    text = raw.strip()

    # 1. Header & Pronunciation
    text = re.sub(f"^({re.escape(word)})", f"{BOLD}{CYAN}\\1{RESET}", text, flags=re.IGNORECASE)
    text = re.sub(r"([|/][^|/]+[|/])", f"{YELLOW}\\1{RESET}", text)

    # 2. Parts of Speech
    pos_pattern = r"\b(noun|verb|adjective|adverb|preposition|conjunction|exclamation|pronoun)\b"
    text = re.sub(pos_pattern, f"{BOLD}{MAGENTA}\\1{RESET}", text)

    # 3. Structural Spacing (Main senses and sub-senses)
    text = re.sub(r"(\d+)\s", r"\n\n\1. ", text)
    text = re.sub(r"([•])", r"\n    \1", text)

    # 4. Synonym Highlighting
    # Detect the word "synonyms:" (lowercase) which often appears inline
    text = re.sub(r"(synonyms:)", f"{BOLD}{BLUE}\\1{RESET}", text, flags=re.IGNORECASE)

    # If there is a block of synonyms following "synonyms:", let's make them stand out
    # This looks for words separated by commas immediately following the label
    syn_list_pattern = r"(?<=synonyms: )([\w\s,]+?)(?=\n|•|ORIGIN|PHRASES|$)"
    text = re.sub(syn_list_pattern, f"{BLUE}\\1{RESET}", text)

    # 5. Example Sentences (Italicize)
    text = re.sub(r"(: [^•\n\d]+)", f"{ITALIC}\\1{RESET}", text)

    # 6. Major Section Headers
    headers = ["ORIGIN", "PHRASES", "DERIVATIVES", "USAGE", "SYNONYMS"]
    for header in headers:
        # Use a bright green bar to separate major sections
        text = text.replace(header, f"\n\n{BOLD}{GREEN}── {header} ──{RESET}")

    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 dict.py [word]")
        sys.exit()

    search_word = " ".join(sys.argv[1:]).strip()
    print(format_definition(search_word))
    print("\n")
