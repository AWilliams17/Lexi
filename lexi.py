import click


@click.group()
def cli():
    pass


@cli.command(help="Returns information about this script.")
def about():
    click.echo(F"About:")


@cli.command(help="Usage: 'lexi define {word}' ~ Looks up the definition for the passed word.")
@click.argument(F"word")
def define(word):
    click.echo(F"definition of {word}: ")


@cli.command(help="Usage: 'lexi anto {word}' ~ List antonyms for the passed word.")
@click.argument(F"word")
def anto(word):
    click.echo("antonym of {word}: ")


@cli.command(help="Usage: 'lexi syn {word}' ~ List synonyms for the passed word.")
@click.argument(F"word")
def syn(word):
    click.echo(F"synonym of {word}: ")


@cli.command(help="Usage: 'lexi tense {word}' ~ List present, future, and past tenses for the passed word.")
@click.argument("word")
def tense(word):
    click.echo(F"tense of {word}: ")


@cli.command(help="Usage: 'lexi lexicon {word}' ~ Outputs all information on the word.")
@click.argument("word")
def lex(word):
    click.echo(F"lexicon of {word}: ")


if __name__ == '__main__':
    cli()
