import typer
import requests
import os
import dotenv
from rich import print  
from rich.console import Console
from rich.table import Table

console = Console()
dotenv.load_dotenv()

app = typer.Typer()




@app.command(name="fd", short_help="Find a repository by name")
def find(name: str):
    '''Find a repository on GitHub by name'''

    print(f"Searching for {name}")
