#!/usr/bin/python

import sys
import typer
import logging
import subprocess

from pathlib import Path
from rich.logging import RichHandler
from rich.console import Console

# Init console
console = Console()

# Init cli
cli = typer.Typer()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(show_time=False)]  # <-- disables timestamps
)

log = logging.getLogger("rich")

# Get the script directory
script_dir = Path(__file__).parent

# Construct the docs path
docs_path = script_dir.parent / "backend/docs"


def install_libs_packages() -> None:
    """Installs the sphinx-build package"""
    command_process = subprocess.run(
        "pip install sphinx-autobuild sphinx-book-theme",
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )


    stderr = command_process.stderr.decode()


    if len(stderr) > 0:
        log.error(
            f"the following error raised when installing packages:\n{stderr}"
        )
        sys.exit(1)


def build_docs(docs_path) -> None:
    """Builds docs"""
    command_process = subprocess.run(
        f"cd {docs_path} && make html",
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    stderr = command_process.stderr.decode()

    if "sphinx-build not found" in stderr:
        log.error(
            "`sphinx-build` is not installed. Installing..."
        )

        install_libs_packages()  # May exit due to errors while installing

        build_docs(docs_path=docs_path)

    return


@cli.command()
def build() -> None:
    """Builds docs"""

    with console.status("Building docs...") as _:
        build_docs(docs_path=docs_path)

    log.info(
        f"Docs built in: '{docs_path}/_static'"
    )


@cli.command()
def serve(
        host: str = typer.Option("0.0.0.0", "--host", help="The host"),
        port: int = typer.Option(9000, "--port", help="The port")
    ) -> None:
    """Serves the docs"""
    command = f"cd {docs_path} && sphinx-autobuild . _build --host {host} --port {port}"

    try:
        subprocess.run(command, shell=True)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    cli()
