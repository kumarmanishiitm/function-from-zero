#!/usr/bin/env python3
from mylib.calc import add, sub, mul, div, power
import click
@click.group()
def cli():
    """This is a simple calculator tool."""
@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cmd(a, b):
    "Add two numbers"
    click.echo(add(a, b))
@cli.command("sub")
@click.argument("a", type=float)
@click.argument("b", type=float)
def sub_cmd(a, b):
    "Subtract two numbers"
    click.echo(sub(a, b))
@cli.command("mul")
@click.argument("a", type=float)
@click.argument("b", type=float)
def mul_cmd(a, b):
    "Multiply two numbers"
    click.echo(mul(a, b))
@cli.command("div")
@click.argument("a", type=float)
@click.argument("b", type=float)
def div_cmd(a, b):
    "Divide two numbers"
    click.echo(div(a, b))
@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_cmd(a, b):
    "Raise a to the power of b"
    click.echo(power(a, b))
if __name__ == "__main__":
    cli()