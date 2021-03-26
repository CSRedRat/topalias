#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Console script topalias."""

import sys

import click

import aliascore as core

from __init__ import __version__


class AliasedGroup(click.Group):
    """Add alias for command by function name"""

    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass  # noqa: WPS420
        return super().get_command(ctx, cmd_name)


def print_version(ctx, ver):
    """Print current program version and check available online"""
    if not ver or ctx.resilient_parsing:
        return
    click.echo("topalias utility version: {}".format(__version__))
    click.echo("Update command:\npip3 install -U --user topalias")
    ctx.exit()


@click.group(
    cls=AliasedGroup,
    context_settings=dict(help_option_names=["-h", "--help"]),  # noqa: C408
    invoke_without_command=True,
)
@click.option(
    "--min",
    "-l",
    "acr",
    default=1,
    type=int,
    help="Print alias acronym not less that value. Default: 1",
)
@click.option(
    "--count",
    "-c",
    default=20,  # noqa: WPS432
    type=int,
    help="Print specified number acronym suggestions. Default: 20",
)
@click.option(
    "--filter",
    "filtering",
    default=False,
    is_flag=True,
    type=bool,
    help="Filter used aliases in history. Default: False",
)
@click.option(
    "--zsh",
    "-z",
    default=False,
    is_flag=True,
    type=bool,
    help="Use zsh shell history file .zsh_history. Default: False",
)
@click.option(
    "--path",
    "-f",
    type=str,
    help="Change custom directory for files: .bash_aliases, .bash_history, .zsh_history",
)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Print current program version and check latest on pypi.org.",  # pylint: disable=too-many-arguments
)
@click.option(
    "--debug/--no-debug",
    default=False,
    help="Enable debug strings in output.",
)
@click.pass_context
def cli(ctx, debug, acr, path, count, filtering, zsh) -> int:  # noqa: WPS211,WPS216
    """See documentation and usage examples: https://csredrat.github.io/topalias"""

    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = core.DEBUG = debug
    ctx.obj["acronym_minimal_length"] = acr
    ctx.obj["suggestion_count"] = count
    core.SUGGESTION_COUNT = ctx.obj["suggestion_count"]

    if path is not None:
        core.path.insert(0, path)

    if filtering:
        core.ALIASES_FILTER = filtering

    if zsh:
        core.HISTORY_FILE = ".zsh_history"

    if debug:
        click.echo("Debug mode is ON")
    if ctx.invoked_subcommand is None:
        return ctx.invoke(main)
    return 0


@cli.command(
    context_settings=dict(help_option_names=["-h", "--help"]),  # noqa: C408
)
@click.pass_context
def main(ctx) -> int:
    """Main function for group command call."""
    click.echo(
        "topalias - linux bash/zsh alias generator & history analytics https://github.com/CSRedRat/topalias",
    )
    if ctx.obj["DEBUG"]:
        click.echo(ctx.obj)

    if core.find_aliases():
        core.collect_alias()
        ctx.forward(top_history)  # pylint: disable=no-value-for-parameter
    else:
        ctx.forward(top_history)  # pylint: disable=no-value-for-parameter
    return 0


@cli.command()
@click.pass_context
def version(ctx) -> None:
    """Get program current and available version."""
    print_version(ctx, ver=True)


@cli.command()
def hint() -> None:
    """Print all hints."""
    core.print_all_hint()


@cli.command(name="history")
@click.pass_context
def top_history(ctx) -> None:
    """Print bash history file."""
    acronym_minimal_length = ctx.obj["acronym_minimal_length"]

    if acronym_minimal_length is None:
        acronym_minimal_length = 1

    click.echo(
        core.print_history(acronym_minimal_length),
    )


ALIASES = {  # noqa: WPS407, need frozendict
    "h": top_history,
}

if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover # pylint: disable=no-value-for-parameter
