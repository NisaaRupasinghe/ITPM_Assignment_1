"""Launcher shim for compatibility with README instructions.

This file simply imports and calls `run_test()` from the original
script so users can run `python test_automation.py ...` as documented.
"""
from IT23388970_test_automation import run_test


if __name__ == "__main__":
    run_test()
