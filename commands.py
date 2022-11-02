import typer

from api.utils.commands.commands import Commands

app = typer.Typer()


@app.command()
def clean():
    Commands.clean_database()


@app.command()
def populate():
    Commands.faker_populate()


if __name__ == "__main__":
    app()
