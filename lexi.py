import click
from words.word import Word


@click.group()
def cli():
    pass


@cli.command(help="Returns information about this script.")
def about():
    click.echo(F"About:")


@cli.command(help="Usage: 'words define {word}' ~ Looks up the definition for the passed word.")
@click.argument(F"word")
def define(word):
    word_inst = Word(word)
    click.echo(F"Definition of {word}:")
    click.echo("-Noun-")
    for i in word_inst.definitions['noun']:
        click.echo(F"{word_inst.definitions['noun'].index(i)}: {i}")
    click.echo("-Verb-")
    for i in word_inst.definitions['verb']:
        click.echo(F"{word_inst.definitions['verb'].index(i)}: {i}")


@cli.command(help="Usage: 'words anto {word}' ~ List antonyms for the passed word.")
@click.argument(F"word")
def anto(word):
    click.echo("antonym of {word}: ")


@cli.command(help="Usage: 'words syn {word}' ~ List synonyms for the passed word.")
@click.argument(F"word")
def syn(word):
    click.echo(F"synonym of {word}: ")


@cli.command(help="Usage: 'words tense {word}' ~ List present, future, and past tenses for the passed word.")
@click.argument("word")
def tense(word):
    click.echo(F"tense of {word}: ")


@cli.command(help="Usage: 'words lexicon {word}' ~ Outputs all information on the word.")
@click.argument("word")
def lex(word):
    click.echo(F"lexicon of {word}: ")


if __name__ == '__main__':
    cli()
