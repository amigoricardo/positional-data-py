import typer
import os
import subprocess


app = typer.Typer()

@app.command()
def main(
        datafile: str = typer.Argument(
            ..., 
            help="Path to the data file"
        ),
        columns: str = typer.Option(
            ..., "--columns", "-c", 
            help="Path to the columns definition file"
        )
    ):

    for file in [datafile, columns]:
        if not os.path.isfile(file):
            raise FileNotFoundError(f"{file} not found")
        
    dirname = os.path.dirname(os.path.abspath(__file__))
    awkfile = os.path.join(dirname, 'convert.awk')

    subprocess.run(["awk", "-f", awkfile, "-v", f"dict={columns}", datafile])