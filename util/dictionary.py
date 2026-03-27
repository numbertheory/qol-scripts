import argparse
import difflib
import re
import sys

import objc
from CoreServices import DCSCopyTextDefinition

# 1. Load the DictionaryServices framework
DS_PATH = "/System/Library/Frameworks/CoreServices.framework/Frameworks/DictionaryServices.framework"
ds_bundle = objc.loadBundle("DictionaryServices", globals(), bundle_path=DS_PATH)

if ds_bundle:
    objc.loadBundleFunctions(
        ds_bundle,
        globals(),
        [
            ("DCSCopyAvailableDictionaries", b"@"),
            ("DCSDictionaryGetName", b"@@"),
        ],
    )

# Distinct Whitelists
DICT_WHITELIST = [
    "New Oxford American Dictionary",
    "Oxford Dictionary of English",
    "Apple Dictionary",
]

THES_WHITELIST = ["Oxford American Writer’s Thesaurus", "Oxford Thesaurus of English"]


def get_dictionaries(whitelist):
    try:
        dicts = DCSCopyAvailableDictionaries()
        if not dicts:
            return {}
        full_map = {DCSDictionaryGetName(d): d for d in dicts}
        return {name: ref for name, ref in full_map.items() if name in whitelist}
    except Exception:
        return {}


def format_definition(word, dict_ref=None):
    raw = DCSCopyTextDefinition(dict_ref, word, (0, len(word)))
    if not raw:
        return f"\033[31mNo entry found for '{word}'.\033[0m"

    BOLD, CYAN, YELLOW, GREEN, MAGENTA, ITALIC, BLUE, RESET = (
        "\033[1m",
        "\033[36m",
        "\033[33m",
        "\033[32m",
        "\033[35m",
        "\033[3m",
        "\033[34m",
        "\033[0m",
    )

    text = raw.strip()
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

    for header in ["ORIGIN", "PHRASES", "DERIVATIVES", "USAGE", "SYNONYMS"]:
        text = text.replace(header, f"\n\n{BOLD}{GREEN}── {header} ──{RESET}")

    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("word", nargs="*", help="Word to define")
    parser.add_argument(
        "-l", "--list", action="store_true", help="List whitelisted items"
    )
    parser.add_argument(
        "-t", "--thesaurus", action="store_true", help="Use Thesaurus whitelist"
    )
    parser.add_argument(
        "-s", "--select-dict", help="Fuzzy search for a name in the active whitelist"
    )
    parser.add_argument("-d", "--dict", help="Specify EXACT dictionary/thesaurus name")
    args = parser.parse_args()

    # Determine which whitelist to use
    active_whitelist = THES_WHITELIST if args.thesaurus else DICT_WHITELIST
    default_fallback = (
        "Oxford American Writer’s Thesaurus" if args.thesaurus else "Apple Dictionary"
    )

    dict_map = get_dictionaries(active_whitelist)
    available_names = list(dict_map.keys())

    # --- Mode: List ---
    if args.list:
        label = "Thesaurus" if args.thesaurus else "Dictionary"
        print(f"\033[1mWhitelisted {label}s:\033[0m")
        for name in sorted(available_names):
            print(f" - {name}")
        sys.exit()

    # --- Mode: Selection Resolution ---
    if args.select_dict and not args.word:
        matches = difflib.get_close_matches(
            args.select_dict, available_names, n=1, cutoff=0.3
        )
        print(matches[0] if matches else default_fallback)
        sys.exit()

    # --- Mode: Definition/Synonyms ---
    if not args.word:
        parser.print_help()
        sys.exit()

    search_word = " ".join(args.word)
    final_name = default_fallback

    if args.dict:
        if args.dict in dict_map:
            final_name = args.dict
    elif args.select_dict:
        matches = difflib.get_close_matches(
            args.select_dict, available_names, n=1, cutoff=0.3
        )
        if matches:
            final_name = matches[0]

    dict_ref = dict_map.get(final_name)
    print(f"\033[2mSource: {final_name}\033[0m")
    print(format_definition(search_word, dict_ref))
