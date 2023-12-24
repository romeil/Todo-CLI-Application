# A series of all the created commands
import click
from priorities import PRIORITIES

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("file", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the to-do name", help="The name of the to-do item")
@click.option("-d", "--desc", prompt="Describe the todo", help="The description of the to-do item")
def add_todo(name, desc, priority, file):
    filename = file if file is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]\n")


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.option("-f", "--file", type=click.Path(exists=True), prompt="Enter the name of the file", help="The name of the file")
@click.option("-i", "--idx", type=int, prompt="Enter index of the to-do item", help="The index of the to-do item")
@click.option("-n", "--name", prompt="Enter the to-do name", help="The name of the to-do item")
@click.option("-d", "--desc", prompt="Describe the todo", help="The description of the to-do item")
def edit_todo(file, idx, name, desc, priority):
    with open(file, "r") as f:
        todo_list = f.read().splitlines()
        todo_list[idx] = f"{name}: {desc} [Priority: {PRIORITIES[priority]}]"
    with open(file, "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


@click.command()
@click.argument("idx", type=int, required=1)
@click.option("-p", "--path", type=click.Path(exists=True))
def delete_todo(path, idx):
    with open(path, "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open(path, "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), required=0)
@click.option("-f", "--file", type=click.Path(exists=True), prompt="Enter the name of the file", help="The name of the file")
def list_todos(priority, file):
    filename = file
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            click.echo(f"({idx}) - {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                    click.echo(f"({idx}) - {todo}") 
