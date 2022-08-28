import typer
import requests
from rich import print  
from rich.console import Console
from rich.table import Table

from utils.auth import verifyAuth


console = Console()
app = typer.Typer()


@app.command(name="ls", short_help="List all your repositories")
def list(
    private: bool = typer.Option(False, "--private", "-p", help="List private repositories"),
    public: bool = typer.Option(False, "--public", "-P", help="List public repositories"),
):
    """List the signed in user's GitHub repositories"""
    

    basicAuth = verifyAuth()
    res = requests.get("https://api.github.com/user/repos", auth=basicAuth).json()

    table = Table("Name", "Visibility", "Stars", "Lang",  "URL")
    
    for repo in res:
        name = repo["name"]
        visibility = repo["private"]
        stars = repo["stargazers_count"]
        lang = repo["language"]
        link = repo["url"]

        if private:
            if visibility:
                table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}",   f'[blue]{link}[/blue]')

        elif public:
            if not visibility:
                table.add_row(name, ":lock: [green]Public[/green]", f':star: {stars}',  f"{lang}",   f'[blue]{link}[/blue]')       
        else:   
            if visibility:
                table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}",   f'[blue]{link}[/blue]')

            else:
                table.add_row(name, ":unlock: [green]Public[/green]", f':star: {stars}', f"{lang}", f'[blue]{link}[/blue]')


    console.print(table)
    
