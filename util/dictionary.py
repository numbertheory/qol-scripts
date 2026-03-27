import argparse
import difflib
import re
import sys

import objc
from CoreServices import DCSCopyTextDefinition

# 1. Manually load the DictionaryServices functions to avoid BridgeSupport conflicts
# This path is standard on macOS
DS_PATH = "/System/Library/Frameworks/CoreServices.framework/Frameworks/DictionaryServices.framework"
ds_bundle = objc.loadBundle("DictionaryServices", globals(), bundle_path=DS_PATH)

# Define the functions with their C signatures
# @ = id (object), ^v = void pointer (for the dict ref)
objc.loadBundleFunctions(
    ds_bundle,
    globals(),
    [
        ("DCSCopyAvailableDictionaries", b"@@"),
        ("DCSDictionaryGetName", b"@@:"),
    ],
)


def get_dictionaries():
    """Returns a dictionary mapping dictionary names to their internal references."""
    try:
        dicts = DCSCopyAvailableDictionaries()
        # On some macOS versions, we need to handle the return as a list
        return {DCSDictionaryGetName(d): d for d in dicts}
    except Exception:
        return {}


def find_best_dict(query, available_names):
    """Finds the closest dictionary name match based on user input."""
    for name in available_names:
        if query.lower() in name.lower():
            return name
    matches = difflib.get_close_matches(query, available_names, n=1, cutoff=0.3)
    return matches[0] if matches else None


def format_definition(word, dict_ref=None):
    # Pass the dict_ref to the CoreServices function
    raw = DCSCopyTextDefinition(dict_ref, word, (0, len(word)))

    if not raw:
        return f"\033[31mNo definition found for '{word}'.\033[0m"

    # ANSI Codes
    BOLD, CYAN, YELLOW, GREEN, MAGENTA, ITALIC, BLUE, FAINT, RESET = (
        "\033[1m",
        "\033[36m",
        "\033[33m",
        "\033[32m",
        "\033[35m",
        "\033[3m",
        "\033[34m",
        "\033[2m",
        "\033[0m",
    )

    text = raw.strip()

    # Structural Formatting
    text = re.sub(
        f"^({re.escape(word)})", f"{BOLD}{CYAN}\\1{RESET}", text, flags=re.IGNORECASE
    )
    text = re.sub(r"([|/][^|/]+[|/])", f"{YELLOW}\\1{RESET}", text)
    text = re.sub(
        r"\b(noun|verb|adjective|adverb|preposition|conjunction|exclamation|pronoun)\b",
        f"{BOLD}{MAGENTA}\\1{RESET}",
        text,
    )
    text = re.sub(r"(\d+)\s", r"\n\n\1. ", text)
    text = re.sub(r"([•])", r"\n    \1", text)
    text = re.sub(r"(: [^•\n\d]+)", f"{ITALIC}\\1{RESET}", text)
    text = re.sub(r"(synonyms:)", f"{BOLD}{BLUE}\\1{RESET}", text, flags=re.IGNORECASE)

    # Section Headers
    for header in ["ORIGIN", "PHRASES", "DERIVATIVES", "USAGE", "SYNONYMS"]:
        text = text.replace(header, f"\n\n{BOLD}{GREEN}── {header} ──{RESET}")

    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word", nargs="*", help="Word to define")
    parser.add_argument(
        "-l", "--list", action="store_true", help="List available dictionaries"
    )
    parser.add_argument("-d", "--dict", help="Fuzzy name of the dictionary to use")
    args = parser.parse_args()

    available_dict_map = get_dictionaries()
    available_names = list(available_dict_map.keys())

    if args.list:
        print("\033[1mAvailable Dictionaries:\033[0m")
        for name in available_names:
            print(f" - {name}")
        sys.exit()

    if not args.word:
        parser.print_help()
        sys.exit()

    search_word = " ".join(args.word)
    selected_dict_ref = None

    if args.dict:
        best_match = find_best_dict(args.dict, available_names)
        if best_match:
            print(f"\033[2mUsing: {best_match}\033[0m")
            selected_dict_ref = available_dict_map[best_match]
        else:
            fallback = find_best_dict("Apple Dictionary", available_names)
            if fallback:
                print(
                    f"\033[2m'{args.dict}' not found. Falling back to: {fallback}\033[0m"
                )
                selected_dict_ref = available_dict_map[fallback]
            else:
                selected_dict_ref = None

    print(format_definition(search_word, selected_dict_ref))
