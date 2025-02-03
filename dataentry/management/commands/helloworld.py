# Importing BaseCommand from Django's core management module.
# BaseCommand is a class provided by Django that allows us to define custom management commands.
from django.core.management.base import BaseCommand


# Define a custom command class that inherits from BaseCommand.
class Command(BaseCommand):
    """
    This class defines a custom Django management command.
    The command simply prints "Hello World" to the console when executed.
    """

    # The 'help' attribute provides a description of what this command does.
    # It is displayed when running `python manage.py help <command_name>`.
    help = "Prints Hello World"

    # The handle() method is where the main logic of the command is implemented.
    # It is executed when the command is run.
    def handle(self, *args, **kwargs):
        """
        This method executes when the command is run via the terminal.
        It prints "Hello World" using Django's stdout.write() method.

        - `self.stdout.write()` is preferred over `print()` in Django management commands
          because it ensures that the output is correctly formatted and handled by Django.
        """

        # Printing "Hello World" to the console.
        self.stdout.write('Hello World')