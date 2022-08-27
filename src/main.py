import typer
import requests
import os
import dotenv
from rich import print  
from rich.console import Console
from rich.table import Table



app = typer.Typer()
console = Console()
dotenv.load_dotenv()


@app.command()
def list():
    """List users GitHub repositories"""
    
    if os.getenv("GITHUB_USERNAME") is None or os.getenv("GITHUB_USERNAME") == "":
        username = typer.prompt("You need to set GITHUB_USERNAME environment variable")
        dotenv.set_key(".env", "GITHUB_USERNAME", username)

    if os.getenv("GITHUB_TOKEN") is None or os.getenv("GITHUB_TOKEN") == "":
        token = typer.prompt("You need to provide a GitHub token: ")
        dotenv.set_key(".env", "GITHUB_TOKEN", token)

    
    basicAuth = (os.getenv("GITHUB_USERNAME"), os.getenv("GITHUB_TOKEN"))
    res = requests.get("https://api.github.com/user/repos", auth=basicAuth).json()

    table = Table("Name", "Visibility", "Stars", "Lang",  "URL")
    
    for repo in res:
        name = repo["name"]
        private = repo["private"]
        stars = repo["stargazers_count"]
        lang = repo["language"]
        link = repo["url"]

        if private:
            table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}",   f'[blue]{link}[/blue]')

        else:
            table.add_row(name, ":unlock: [green]Public[/green]", f':star: {stars}', f"{lang}", f'[blue]{link}[/blue]')


    console.print(table)




@app.command()
def find(name: str):
    print(f"Searching for {name}")



if __name__ == "__main__":
    app()
