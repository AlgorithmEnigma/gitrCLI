import os
from turtle import dot
import dotenv
import typer 

def verifyAuth():
    '''
    Verify that the user has provided a GitHub username and token

    If not ask for user to provide them
    '''

    dotenv.load_dotenv()

    if os.getenv("GITHUB_USERNAME") is None or os.getenv("GITHUB_USERNAME") == "":
            username = typer.prompt("You need to set GITHUB_USERNAME environment variable")
            dotenv.set_key(".env", "GITHUB_USERNAME", username)

    if os.getenv("GITHUB_TOKEN") is None or os.getenv("GITHUB_TOKEN") == "":
            token = typer.prompt("You need to provide a GitHub token: ")
            dotenv.set_key(".env", "GITHUB_TOKEN", token)

    basicAuth = (os.getenv("GITHUB_USERNAME"), os.getenv("GITHUB_TOKEN"))
    return basicAuth