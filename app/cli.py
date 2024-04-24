import multiprocessing
import subprocess

import click


@click.group()
def mh_cli():
    """MangoHabanero CLI."""
    pass


@mh_cli.group("server")
def mh_server():
    """Commands for managing the server."""
    pass


@mh_server.command("development")
@click.argument("app", required=True)
@click.option(
    "--log-level",
    type=click.Choice(["debug", "info", "warning", "error", "critical"]),
    default="debug",
    help="Set the log level.",
)
@click.option(
    "--interface",
    type=click.Choice(["asgi", "rsgi", "wsgi"]),
    default="asgi",
    help="Set the interface.",
)
def run_dev_server(app, interface: str, log_level: str):
    """Start the development server."""
    threads = multiprocessing.cpu_count()
    subprocess.run(
        [
            "granian",
            "--interface",
            interface,
            app,
            "--log-level",
            log_level,
            "--threads",
            str(threads),
        ]
    )


@mh_server.command(
    "start",
    context_settings={
        "ignore_unknown_options": True,
        "allow_extra_args": True,
    },
)
@click.pass_context
def start(context: click.Context):
    """Start the server."""
    subprocess.run(["granian"] + context.args)


def entrypoint():
    from app.exceptions import MangoHabaneroException

    try:
        mh_cli()
    except MangoHabaneroException as e:
        click.secho(f"ERROR: {e}", bold=True, fg="red")


if __name__ == "__main__":
    entrypoint()
