import argparse
import configparser
import sys

from pyautomaton.PyAutomaton import PyAutomatonMgr


def load_config_parser(config_file_path) -> configparser.ConfigParser:
    # Create the configuration parser
    config_parser = configparser.ConfigParser()

    # Read the configuration file
    # config_parser.read(config_file_path)
    try:
        with open(config_file_path) as config_file:
            config_parser.read_file(config_file)
    except IOError:
        print("\n--------\nError: Config file not found at the provided path: "
              "{0}.\nTerminating execution. See README.md ('Setup/Config' "
              "section) for help.\n--------\n".format(
                  config_file_path))
        sys.exit(1)
    return config_parser


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "config",
        help="Specify file path to the script's config file (see README.md)."
    )
    args = argument_parser.parse_args()

    # Load config parser at specified file path
    config_parser = load_config_parser(args.config)

    # Build PyAutomaton object with config_parser's help
    PyAuto = PyAutomaton(config_parser)

    # Execute appropriate logic per specified optional argument
    if args.asdf:
        PyAuto.asdf(args.asdf)
    elif args.qwerty:
        PyAuto.qwerty(args.qwerty)
    else:
        print("\n*No optional args passed to the 'pyautomaton' "
              "console command, therefore no script actions performed. "
              "See help message ('pyautomaton -h') for help.*\n")


if __name__ == "__main__":
    sys.exit(main())
