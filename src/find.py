import typer
import requests
import os

from rich import print  
from rich.console import Console
from rich.table import Table
from utils.auth import verifyAuth


console = Console()
app = typer.Typer()


@app.command(name="fd", short_help="Find a repository by name")
def find(
    reponame: str = typer.Argument(..., help="The name of the repository to find"),
    clone: bool = typer.Option(False, "--clone", "-c", help="Clone the repository")
):
    '''Find a repository on GitHub by name'''
    
    print(clone)

    basicAuth = verifyAuth()
    res = requests.get("https://api.github.com/user/repos", auth=basicAuth).json()

    table = Table("Name", "Visibility", "Stars", "Lang", "URL")
    
    
    for repo in res:
        if repo["name"] == reponame:
            name = repo["name"]
            visibility = repo["private"]
            stars = repo["stargazers_count"]
            lang = repo["language"]
            link = repo["html_url"]
            cloneUrl = repo["clone_url"]

            # table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}",   f'[blue]{link}[/blue]')
            
            if visibility:
                table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}", f'[blue]{link}[/blue]')

            else:
                table.add_row(name, ":unlock: [green]Public[/green]", f':star: {stars}', f"{lang}", f'[blue]{link}[/blue]')
            
            console.print(table)
            if clone:
                confirm = typer.confirm(f"Clone {name} to {clone}?")
                if confirm:
                    print(clone)
                    os.system(f"git clone {cloneUrl} ./{reponame}")
                    print(f"Cloned {name}")
            return
        
    

    print(f"Repository {reponame} not found")
            
