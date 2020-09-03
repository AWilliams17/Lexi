import click
from words.word import Word


@click.group()
def cli():
    pass


@cli.command(short_help="Returns information about this script.")
def about():
    click.echo(F"About:")
    click.echo("Github: github.com/awilliams17/Lexi")
    click.echo("To report a problem, file an issue in the repo.")


@cli.command(short_help="Usage: 'define {word}' ~ Looks up definitions for the word.")
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


@cli.command(short_help="Usage: 'anto {word}' ~ Lists antonyms for the word.")
@click.argument(F"word")
def anto(word):
    word_inst = Word(word)
    click.echo(F"Antonyms of {word}:")
    for i in word_inst.meanings['antonyms']:
        click.echo(F"{word_inst.meanings['antonyms'].index(i)+1}: {i}")


@cli.command(short_help="Usage: 'syn {word}' ~ Lists synonyms for the word.")
@click.argument(F"word")
def syn(word):
    word_inst = Word(word)
    click.echo(F"Synonyms of {word}:")
    for i in word_inst.meanings['synonyms']:
        click.echo(F"{word_inst.meanings['synonyms'].index(i)+1}: {i}")


@cli.command(short_help="Usage: 'examples {word}' ~ Lists examples of the word in a sentence.")
@click.argument("word")
def examples(word):
    word_inst = Word(word)
    click.echo(F"examples of {word} in a sentence: ")
    for i in word_inst.examples:
        click.echo(F"{word_inst.examples.index(i)+1}: {i}")


@cli.command(short_help="Usage: 'rhyme {word}' ~ Outputs all words which rhyme with the word")
@click.argument("word")
def rhyme(word):
    word_inst = Word(word)
    click.echo(F"rhymes of {word}: ")
    for i in word_inst.rhymes:
        click.echo(F"{word_inst.rhymes.index(i)+1}: {i}")


if __name__ == '__main__':
    cli()
