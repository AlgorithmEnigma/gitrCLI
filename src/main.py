import typer

# Import commands
import list
import find



# Create a typer application
app = typer.Typer()

# Register commands to the application
app.registered_commands += list.app.registered_commands + find.app.registered_commands


@app.callback()
def callback():
    """
    A fancy CLI to manage GitHub repositories.
    """




if __name__ == "__main__":
    app()
