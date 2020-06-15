import click
from words.word import Word


@click.group()
def cli():
    pass


@cli.command(help="Returns information about this script.")
def about():
    click.echo(F"About:")


@cli.command(help="Usage: 'define {word}' ~ Looks up the definition for the passed word.")
@click.argument(F"word")
def define(word):
    word_inst = Word(word)
    click.echo(F"Definition of {word}:")
    click.echo("-Noun-")
    for i in word_inst.definitions['noun']:
        click.echo(F"{word_inst.definitions['noun'].index(i)+1}: {i}")
    click.echo("-Verb-")
    for i in word_inst.definitions['verb']:
        click.echo(F"{word_inst.definitions['verb'].index(i)+1}: {i}")


@cli.command(help="Usage: 'anto {word}' ~ List antonyms for the passed word.")
@click.argument(F"word")
def anto(word):
    word_inst = Word(word)
    click.echo(F"Antonyms of {word}:")
    for i in word_inst.meanings['antonyms']:
        click.echo(F"{word_inst.meanings['antonyms'].index(i)+1}: {i}")


@cli.command(help="Usage: 'syn {word}' ~ List synonyms for the passed word.")
@click.argument(F"word")
def syn(word):
    word_inst = Word(word)
    click.echo(F"Synonyms of {word}:")
    for i in word_inst.meanings['synonyms']:
        click.echo(F"{word_inst.meanings['synonyms'].index(i)+1}: {i}")


@cli.command(help="Usage: 'examples {word}' ~ List examples of the word in a sentence.")
@click.argument("word")
def examples(word):
    word_inst = Word(word)
    click.echo(F"examples of {word} in a sentence: ")


@cli.command(help="Usage: 'lexicon {word}' ~ Outputs all information on the word.")
@click.argument("word")
def lex(word):
    word_inst = Word(word)
    click.echo(F"lexicon of {word}: ")
    click.echo(word_inst)


if __name__ == '__main__':
    cli()
