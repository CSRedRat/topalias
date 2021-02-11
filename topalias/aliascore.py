# -*- coding: utf-8 -*-
"""Main module. Not for executing, only library. Run project from cli.py"""

import io
import logging
import os
import random
import re
import sys

from statistic import most_used_utils
from statistic import top_command


NOTHING = "Empty"

DEBUG = False
HOME = os.path.expanduser("~")
CURRENT = os.path.expanduser(".")
path = [CURRENT, HOME]
SUGGESTION_COUNT = 20
ALIASES_FILTER = False
HISTORY_FILE = ".bash_history"

logging.basicConfig(
    stream=sys.stdout,
    format="%(levelname)s:%(message)s",
    level=(logging.DEBUG if DEBUG else logging.ERROR),
)


def find_first(filename: str, paths: list) -> str:  # type: ignore
    """Find file in PATH
    :rtype: str
    :param filename: what file search
    :param paths: where search file with directory order
    :type filename: str
    :type paths: list
    """
    for directory in paths:
        full_path = os.path.join(directory, filename)
        logging.debug(
            "Full path and file check: %s, %s",
            full_path,
            os.path.isfile(full_path),
        )
        if os.path.isfile(full_path):
            return full_path
    return NOTHING


def find_history() -> str:  # pylint: disable=inconsistent-return-statements
    """Find command history file"""
    history_path = find_first(HISTORY_FILE, path)
    if history_path != NOTHING:
        logging.debug("History file: %s", history_path)
        return history_path
    print("File {} not found in any of the directories".format(HISTORY_FILE))
    if DEBUG:
        file_dir = os.path.dirname(os.path.realpath(__file__))
        if HISTORY_FILE == ".zsh_history":
            data_path = os.path.join(file_dir, "data/.zsh_history")
        else:
            data_path = os.path.join(file_dir, "data/.bash_history")
        logging.debug("History file: %s", data_path)
        return data_path


def find_aliases() -> str:  # pylint: disable=inconsistent-return-statements
    """Find defined aliases file for shell"""
    aliases_name = ".bash_aliases"
    aliases_path = find_first(aliases_name, path)
    if aliases_path != NOTHING:
        return aliases_path
    print("File {} not found in any of the directories ".format(aliases_name))
    if DEBUG:
        file_dir = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(file_dir, "data/.bash_aliases")


used_alias = []


def collect_alias():
    """Top used aliases"""
    try:
        with open(find_aliases(), "r", encoding="utf-8") as aliases_data:
            for line in aliases_data:
                if not line.startswith("#", 0, 1) or line:
                    s = line.rstrip()
                    alias_name = list(s.split(" "))
                    if alias_name[0] == "alias":
                        used_alias.append(alias_name[1].split("=")[0])
    except FileNotFoundError:
        print("Try: topalias -f /path/to/home/folder/with/history")
        print(
            "Collect debug info with --debug flag and add issue: https://github.com/CSRedRat/topalias/issue",
        )
        print("Try: topalias history")


acronyminator = re.compile(r"(?:(?<=\s)|^)(?:[a-z]|\d+)")


def welcome(event: str) -> None:
    """Event message inside the program."""
    print("console util {}".format(event))


def filter_alias_length(raw_command_bank, min_length: int) -> list:  # type: ignore
    """Return acronyms with minimal length"""
    filtered_bank = []
    for command in raw_command_bank:
        gen_alias = "".join(acronyminator.findall(command))
        if len(gen_alias) >= min_length:
            filtered_bank.append(command)
        else:
            logging.info("COMMAND_FILTERED: %s", command)

    return filtered_bank


def print_stat(raw_lines, filtered) -> None:
    """Any statistics"""
    rows_count = len(raw_lines)
    unique_count = len(set(raw_lines))
    filtered_count = unique_count - len(set(filtered))
    top_utils = most_used_utils(load_command_bank(filtering=ALIASES_FILTER))
    top_utils_text_line = ""
    for paired_rank in top_utils:  # noqa: WPS440, WPS519
        top_utils_text_line += "{}: {}, ".format(
            paired_rank[0],
            paired_rank[1],
        )
    top_utils_text_line = top_utils_text_line[:-2]
    print(
        "\ncommands in history: {}, unique commands: {}, filtered by length: {}\n".format(
            rows_count,
            unique_count,
            filtered_count,
        ),
        "most used utils: {}".format(top_utils_text_line),
    )
    if used_alias:
        top_aliases = most_used_utils(load_command_bank(), aliases=used_alias)
        top_aliases_text_line = ""
        for paired_rank in top_aliases:  # noqa: WPS440, WPS519
            top_aliases_text_line += "{}: {}, ".format(
                paired_rank[0],
                paired_rank[1],
            )
        top_aliases_text_line = top_aliases_text_line[:-2]
        if top_aliases:
            print(" most used aliases: {}".format(top_aliases_text_line))


HISTTIMEFORMAT_FIRST = "Hint: add timestamps in history log: "
HISTTIMEFORMAT_SECOND = (
    "echo \"export HISTTIMEFORMAT='%F %T '\" >> ~/.bashrc"  # noqa: WPS323
)
HISTTIMEFORMAT = "".join((HISTTIMEFORMAT_FIRST, HISTTIMEFORMAT_SECOND))

hint_bank = (
    "Hint (secure): add space ' ' before sensitive command in terminal for skip save current command in history!",
    HISTTIMEFORMAT,
    "Hint: command 'sudo !!' after you forget add sudo before command in previous command",
    "Hint: command !<command number in history> for repeat command from history",
    "Hint: ignore command in history: echo \"export HISTIGNORE='ls -l:pwd:date:ll:ls:'\" >> ~/.bashrc",
    'Hint: ignore duplicates in history: echo "export HISTCONTROL=ignoreboth" >> ~/.bashrc',
    "Hint: run 'alias' command to print all used aliases",
    "Hint: example aliases: https://github.com/CSRedRat/topalias/blob/master/topalias/data/.bash_aliases"
    + " (you can add their)",
)


def print_hint() -> None:
    """Hints for user"""
    print("\nRun after add alias: source ~/.bash_aliases")
    print(random.choice(hint_bank))


def print_all_hint() -> None:
    """Print all hints"""
    print("\nRun after add alias: source ~/.bash_aliases")
    for number, hint in enumerate(hint_bank):
        print(number, hint)


def process_bash_line(line: str, filtering: bool = False):
    """ Process bash history line """
    if (not line.startswith("#", 0, 1)) and line != "":
        clear_line = line.rstrip()
        if filtering and clear_line:
            first_word_in_command = clear_line.split()[0]
            if first_word_in_command not in used_alias:
                return clear_line
            return None
        return clear_line or None
    return None


def process_zsh_line(line: str, filtering: bool = False):
    """ Process zsh history line"""
    clear_line = line.split(";")[1].rstrip()
    if filtering and clear_line:
        first_word_in_command = clear_line.split()[0]
        if first_word_in_command not in used_alias:
            return clear_line
    elif clear_line:
        return clear_line
    return None


def load_command_bank(filtering=False):  # pylint: disable=too-many-branches
    """Read and parse shell command history file"""
    command_bank = []
    history_file_path = find_history()
    multiline_buffer = []
    try:
        with io.FileIO("{}".format(history_file_path), "r") as history_data:
            history_data_encoded = io.TextIOWrapper(
                history_data,
                encoding="UTF-8",
                errors="ignore",
            )
            for line in history_data_encoded:
                if HISTORY_FILE == ".bash_history":  # noqa: WPS223
                    if process_bash_line(line, filtering):
                        command_bank.append(process_bash_line(line, filtering))
                else:
                    # ZSH processing
                    # Multiline handler
                    # First line of multiline ends with '\'
                    if line.strip().endswith("\\") and not multiline_buffer:
                        multiline_buffer.append(line.strip()[:-1])
                        continue
                    # Next line of multiline
                    if not line.startswith(":") and multiline_buffer:
                        # If not last line in multiline
                        if line.strip().endswith("\\"):
                            multiline_buffer.append(line.strip()[:-1])
                            continue
                        # If last line in multiline
                        multiline_buffer.append(line.strip())
                    # Check if we have multiline in buffer
                    if multiline_buffer:
                        line = " ".join(multiline_buffer)  # noqa: WPS440
                        multiline_buffer = []
                    if process_zsh_line(line, filtering):
                        command_bank.append(process_zsh_line(line, filtering))

    except FileNotFoundError:
        print("Try: topalias -f /path/to/home/folder/with/history")
        print(
            "Collect debug info with --debug flag and add issue: https://github.com/CSRedRat/topalias/issue",
        )
        print("Try: topalias history")

    return command_bank


def print_history(acronym_length) -> None:
    """Main function for print top commands and suggestions aliases"""
    if DEBUG:
        logging.getLogger().setLevel(logging.DEBUG)

    command_bank = load_command_bank(filtering=ALIASES_FILTER)

    filtered_alias_bank = filter_alias_length(command_bank, acronym_length)
    top_raw_list = top_command(filtered_alias_bank, SUGGESTION_COUNT)
    print("\n")

    if HISTORY_FILE == ".zsh_history":
        aliases_output = "~/.zshrc"
    else:
        aliases_output = "~/.bash_aliases"

    for num, ranked_command in reversed(list(enumerate(top_raw_list, start=1))):
        acronym = "".join(acronyminator.findall(ranked_command[0]))
        linux_add_alias = "echo \"alias {}='{}'\" >> {}".format(
            acronym,
            ranked_command[0],
            aliases_output,
        )
        print(
            "{}. {}\n".format(num, ranked_command[0]),  # noqa: WPS221
            "executed count: {}, suggestion: {}".format(ranked_command[1], acronym),
            "\n",
            "{}".format(linux_add_alias),
        )
    print_stat(command_bank, filtered_alias_bank)
    print_hint()
