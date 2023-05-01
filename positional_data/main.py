import typer
import os
import shutil
import subprocess


app = typer.Typer(pretty_exceptions_show_locals=False)

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

    awk_which = shutil.which("awk")
    if awk_which is None:
        raise RuntimeError("Could not find awk command. Make sure it is installed and on your PATH.")

    for file in [datafile, columns]:
        if not os.path.isfile(file):
            raise FileNotFoundError(f"{file} not found.")
        
    dirname = os.path.dirname(os.path.abspath(__file__))
    awkfile = os.path.join(dirname, 'convert.awk')

    subprocess.run(["awk", "-f", awkfile, "-v", f"dict={columns}", datafile])