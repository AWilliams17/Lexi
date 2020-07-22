import click
from words.word import Word


@click.group()
def cli():
    pass


@cli.command(help="Returns information about this script.")
def about():
    click.echo(F"About:")
    click.echo("Github: github.com/awilliams17/Lexi")
    click.echo("To report a problem, file an issue in the repo.")
    click.echo("Contact: awilliams17412@gmail.com")


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
    for i in word_inst.examples:
        click.echo(F"{word_inst.examples.index(i)+1}: {i}")


@cli.command(help="Usage: 'lexicon {word}' ~ Outputs all information on the word.")
@click.argument("word")
def lexicon(word):
    word_inst = Word(word)
    click.echo(F"lexicon of {word}: ")
    click.echo(word_inst)


@cli.command(help="Usage: 'rhyme {word}' ~ Outputs all words which rhyme with the passed word")
@click.argument("word")
def rhyme(word):
    word_inst = Word(word)
    click.echo(F"rhymes of {word}: ")
    for i in word_inst.rhymes:
        click.echo(F"{word_inst.rhymes.index(i)+1}: {i}")


if __name__ == '__main__':
    cli()
