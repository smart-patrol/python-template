"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """{{cookiecutter.package_name}}."""


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
