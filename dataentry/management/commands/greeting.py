from django.core.management.base import BaseCommand


# Define a custom command class that inherits from BaseCommand.
class Command(BaseCommand):
    """
    This class defines a custom Django management command named `greeting`.
    The command takes a single argument (name) and prints a greeting message.
    """

    # The 'help' attribute provides a short description of the command.
    # This description is shown when running `python manage.py help greeting`.
    help = "Greets the user"

    def add_arguments(self, parser):
        """
        This method allows the command to accept arguments from the command line.

        - `parser.add_argument('name', type=str, help='Specifies user name')`:
          - Adds a required positional argument `name` (string).
          - This argument represents the user's name.
          - The help text describes its purpose.

        Example:
        Running `python manage.py greeting femi` will pass "femi" as the `name` argument.
        """
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        """
        This method executes when the command is run via the terminal.

        - Retrieves the `name` argument from `kwargs`.
        - Constructs a greeting message using an f-string.
        - Uses `self.stdout.write(self.style.SUCCESS(message))` to display the message in green.

        Example:
        Running `python manage.py greeting Alice` will output:
        `Hi femi, Good Morning!` (formatted as a success message).
        """

        # Extracting the user's name from the command-line arguments
        name = kwargs['name']

        # Creating the greeting message using an f-string
        greeting = f'Hi {name}, Good Morning!'

        # Printing the greeting message in a success format (green text)
        self.stdout.write(self.style.SUCCESS(greeting))