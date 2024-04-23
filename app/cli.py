import click
import uvicorn


@click.group()
def mh_cli():
    """MangoHabanero CLI."""
    pass


@mh_cli.group("server")
def mh_server():
    """Commands for managing the server."""
    pass


@mh_server.command("develop")
@click.option(
    "--log-level",
    type=click.Choice(["debug", "info", "warning", "error", "critical"]),
    default="debug",
    help="Set the log level.",
)
def run_server(log_level: str):
    """Start the development server."""
    uvicorn.run("app.main:app", reload=True, log_level=log_level)


mh_server.add_command(uvicorn.main, name="start")


def entrypoint():
    from app.exceptions import MangoHabaneroException

    try:
        mh_cli()
    except MangoHabaneroException as e:
        click.secho(f"ERROR: {e}", bold=True, fg="red")


if __name__ == "__main__":
    entrypoint()
