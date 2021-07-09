import argparse
import sys

from pyautomaton.py_automaton import PyAutomatonMgr
from credit_karma_bot.model.application import Application as CreditKarmaApp


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "-k", "--review_credit_karma",
        action="store",
        help="Fetch Credit Karma credit score results for the specified username."
    )
    args = argument_parser.parse_args()

    # Build PyAutomaton object with config_parser's help
    PyAuto = PyAutomatonMgr()

    # Execute appropriate logic per specified optional argument
    if args.review_credit_karma:
        PyAuto.review_credit_karma(args.review_credit_karma)
    # elif args.asdf:
    #     PyAuto.asdf(args.asdf)
    else:
        print("\n*No optional args passed to the 'pyautomaton' "
              "console command, therefore no script actions performed. "
              "See help message ('pyautomaton -h') for help.*\n")


if __name__ == "__main__":
    sys.exit(main())
