import typer
import requests
from rich import print  
from rich.console import Console
from rich.table import Table
from utils.auth import verifyAuth


console = Console()
app = typer.Typer()


@app.command(name="fd", short_help="Find a repository by name")
def find(reponame: str = typer.Argument(..., help="The name of the repository to find")):
    '''Find a repository on GitHub by name'''
    # print(reponame)

    basicAuth = verifyAuth()
    res = requests.get("https://api.github.com/user/repos", auth=basicAuth).json()

    table = Table("Name", "Visibility", "Stars", "Lang")
    table.add_column("Git Clone")
    table.add_column("URL", width=10)
    
    # print(f"Searching for {repo}")
    for repo in res:
        if repo["name"] == reponame:
            name = repo["name"]
            visibility = repo["private"]
            stars = repo["stargazers_count"]
            lang = repo["language"]
            gitLink = repo["git_url"]
            link = repo["url"]

            # table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}",   f'[blue]{link}[/blue]')
            
            if visibility:
                table.add_row(name, ":lock: [red]Private[/red]", f':star: {stars}',  f"{lang}", f'{gitLink}', f'[blue]{link}[/blue]')

            else:
                table.add_row(name, ":unlock: [green]Public[/green]", f':star: {stars}', f"{lang}", f'{gitLink}', f'[blue]{link}[/blue]')
            
            console.print(table)
            return
        
    

    print(f"Repository {name} not found")
            
            
    
