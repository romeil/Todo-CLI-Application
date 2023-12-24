# Groups all the created commands into mycommands()
import click
from commands import add_todo, edit_todo, delete_todo, list_todos


@click.group
def mycommands():
    pass

mycommands.add_command(add_todo)
mycommands.add_command(edit_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)