"""Assistant bot application to manage a contact list via command-line interface."""
import sys

from colorama import init, Style

from utils.constants import (
    WELCOME_MESSAGE_TITLE,
    WELCOME_MESSAGE_SUBTITLE,
    HELLO_MESSAGE,
    APP_PURPOSE_MESSAGE,
    INVALID_COMMAND_MESSAGE,
    INVALID_EMPTY_COMMAND_MESSAGE,
    MENU_HELP_STR,
    HELP_AWARE_TIP,
    EXIT_MESSAGE,
)
from utils.input_parser import parse_input
from contacts.contacts_validator import (
    validate_are_two_arguments,
    validate_is_one_argument_username,
    validate_contact_not_in_contacts,
    validate_contact_name_exists,
    validate_phone_number,
    validate_not_phone_duplicate,
    validate_contacts_not_empty,
)
from contacts.contacts_handler import add_contact, change_contact, show_phone, show_all

# Initialize colorama for Windows compatibility
init(autoreset=True)


def show_hello_message():
    """Returns a hello message to the user."""
    return f"{HELLO_MESSAGE}\n{APP_PURPOSE_MESSAGE}."


def exit_program():
    """Exits the program with a exit message."""
    print(EXIT_MESSAGE)
    sys.exit(0)


def main():
    """
    Main function to run the assistant bot. It handles user input, command dispatching,
    validation, and help generation for a contact book CLI assistant.
    """

    contacts = {}

    # Initial greeting and help menu
    print(Style.BRIGHT + f"\n{WELCOME_MESSAGE_TITLE}".upper())
    print(f"\n{WELCOME_MESSAGE_SUBTITLE}:")
    print(f"\n{MENU_HELP_STR}")

    while True:
        # Read user input
        user_input = input(f"\nEnter a command (or {HELP_AWARE_TIP}): ")
        if not user_input:
            print(f"{INVALID_EMPTY_COMMAND_MESSAGE}.")
            continue

        # Get command and arguments from input string
        command, args = parse_input(user_input)

        # Match input command with one from the menu
        match command:
            case "hello":
                # No validation here
                # Call handling function
                print(show_hello_message())
            case "add":
                try:
                    # Run validation checks
                    validate_are_two_arguments(args, contacts)
                    validate_phone_number(args, contacts)
                    validate_contact_not_in_contacts(args, contacts)
                    # Call handling function
                    print(add_contact(args, contacts))
                except ValueError as exc:
                    print(f"{exc}")
            case "change":
                try:
                    # Run validation checks
                    validate_are_two_arguments(args, contacts)
                    validate_phone_number(args, contacts)
                    validate_contact_name_exists(args, contacts)
                    validate_not_phone_duplicate(args, contacts)
                    # Call handling function
                    print(change_contact(args, contacts))
                except ValueError as exc:
                    print(f"{exc}")
            case "phone":
                try:
                    # Run validation checks
                    validate_is_one_argument_username(args, contacts)
                    # Partial match is supported. Check if name is in the
                    # contacts list (with partial match) postponed to the
                    # handler function
                    # Call handling function
                    print(show_phone(args, contacts))
                except ValueError as exc:
                    print(f"{exc}")
            case "all":
                try:
                    # Run validation checks
                    validate_contacts_not_empty(args, contacts)
                    # Call handling function
                    print(show_all(args, contacts))
                except ValueError as exc:
                    print(f"{exc}")
            case "help":
                # No validation here
                print(MENU_HELP_STR)
            case "close" | "exit":
                # No validation here
                exit_program()
            case _:
                # No validation here
                print(f"{INVALID_COMMAND_MESSAGE}. {HELP_AWARE_TIP.capitalize()}.")


def main_alternative():
    """
    Main function to run the assistant bot. It handles user input, command dispatching,
    validation, and help generation for a contact book CLI assistant.
    """
    contacts = {}

    def show_help():
        """
        Generate formatted help text from available commands.

        Returns:
            str: Aligned list of commands with their descriptions.
        """
        help_entries = []

        # Prepare all command strings with their details
        for command, metadata in menu.items():
            # Skip commands that are hidden from help (visible=False by design)
            if not metadata.get("visible", True):
                continue

            # Format aliases: "exit (or close)"
            aliases = metadata.get("aliases", [])
            alias_str = f" (or {', '.join(aliases)})" if aliases else ""

            # Build the command string with arguments
            command_str = f"{command}{alias_str} {metadata['args_str']}".strip()

            # Append command string and description to the help list
            help_entries.append((command_str, metadata["description"]))

        # Find the longest command string to align the output
        max_command_length = max(len(cmd_str) for cmd_str, _ in help_entries)

        # Format help lines with aligned commands and descriptions
        formatted_help_lines = [
            f"{cmd_str.ljust(max_command_length)} - {description}"
            for cmd_str, description in help_entries
        ]
        # Add a blank line before the list starts
        formatted_help_lines.insert(0, "")

        return "\n".join(formatted_help_lines)

    menu = {
        "hello": {
            # A string showing expected arguments help text
            # in <command> (required argument)
            # or [command] (optional argument) format
            # or empty if none are required.
            "args_str": "",
            # A string describing what this command does
            "description": "Greet the user",
            # Optional: a tuple of functions to validate args,
            # or None if no validation is required.
            # Functions called in declaration order.
            "validators": None,
            # The function that handles this command after all validations
            "handler": lambda _, __: show_hello_message(),
        },
        "add": {
            "args_str": "<username> <phone>",
            "description": "Add a new contact",
            "validators": (
                validate_are_two_arguments,
                validate_phone_number,
                validate_contact_not_in_contacts,
            ),
            "handler": add_contact,
        },
        "change": {
            "args_str": "<username> <new_phone>",
            "description": "Update contact's phone number",
            "validators": (
                validate_are_two_arguments,
                validate_phone_number,
                validate_contact_name_exists,
                validate_not_phone_duplicate,
            ),
            "handler": change_contact,
        },
        "phone": {
            "args_str": "<username>",
            "description": "Show contact's phone number",
            "validators": (
                validate_is_one_argument_username,
                # Note: Partial match is supported. Validation check if name is
                #       in the contacts (with partial match) postponed to the
                #       handler function
            ),
            "handler": show_phone,
        },
        "all": {
            "args_str": "",
            "description": "Display all contacts",
            "validators": (validate_contacts_not_empty,),
            "handler": show_all,
        },
        "help": {
            "args_str": "",
            "description": "Show available commands",
            "validators": None,
            "handler": lambda _, __: show_help(),
        },
        "exit": {
            "aliases": ["close"],
            "args_str": "",
            "description": "Exit the app",
            "validators": None,
            "handler": lambda _, __: exit_program(),
        },
        "close": {
            "visible": False,
            "args_str": "",
            "description": "Exit the app",
            "validators": None,
            "handler": lambda _, __: exit_program(),
        },
    }

    # Initial greeting and help menu
    print(Style.BRIGHT + f"\n{WELCOME_MESSAGE_TITLE}".upper())
    print(f"\n{WELCOME_MESSAGE_SUBTITLE}:")
    print(show_help())

    while True:
        # Read user input
        user_input = input(f"\nEnter a command (or {HELP_AWARE_TIP}): ")
        if not user_input:
            print(f"{INVALID_EMPTY_COMMAND_MESSAGE}.")
            continue

        # Get command and arguments from input string
        command, args = parse_input(user_input)

        # Match input command with one from the menu
        metadata = menu.get(command)
        if not metadata:
            print(f"{INVALID_COMMAND_MESSAGE}. {HELP_AWARE_TIP.capitalize()}.")
            continue

        # Run validation checks
        if metadata["validators"]:
            try:
                # Run all available validators
                for validator in metadata["validators"]:
                    # Execute each validator
                    validator(args, contacts)
            except ValueError as exc:
                print(f"{exc}")
                continue

        # Call handling function
        result = metadata["handler"](args, contacts)
        if result:
            print(result)


if __name__ == "__main__":
    try:
        # Choose solution approach
        if "--alternative" in sys.argv:
            main_alternative()
        else:
            main()
    except KeyboardInterrupt:
        print(f"\n{EXIT_MESSAGE} (Interrupted by user)")
        sys.exit(0)
