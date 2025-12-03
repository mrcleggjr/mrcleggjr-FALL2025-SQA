import os
import sys
import traceback
from pathlib import Path

import py_parser

FUZZ_STRINGS = [
    "",
    "a" * 10000,
    "\x00" * 100,
    "\uffff" * 100,
    "def func(:\n    pass",
    "import * from module",
    "class A:\n    def method(self):\n        return self",
    "def func():\n    return 'Hello\n",
    "def func():\n    x = 1/0",
    "def func():\n    y = unknown_var",
]
LOGFILE = str(Path(__file__).resolve().parent / "fuzz_results.txt")


def log(message):
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def fuzz_function(func, inputs):
    errors = []
    for inp in inputs:
        try:
            func(inp)
        except Exception as e:
            errors.append(traceback.format_exc())
    return errors

if __name__ == '__main__':
    if os.path.exists(LOGFILE):
        os.remove(LOGFILE)

    print("Starting fuzz testing...")
    all_errors = []
    functions_to_test = [
        py_parser.getPythonParseObject,
        py_parser.checkIfParsablePython,
        py_parser.getFunctionDefinitions,
        py_parser.getImport,
        py_parser.getFunctionAssignments,
    ]

    for func in functions_to_test:
        all_errors += fuzz_function(func, FUZZ_STRINGS)

    for error in all_errors:
        log(error)

    print(f"Fuzz testing completed. Logged {len(all_errors)} errors to {LOGFILE}.")   