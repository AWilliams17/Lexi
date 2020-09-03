# Lexi
I made this because I wanted to fool around with [NLTK](https://github.com/nltk/nltk) and [click](https://github.com/pallets/click). I also made it because it sounded like it would be an entertaining way to pass the time.  

That being said, don't look at the source expecting to see gold. I haven't even finished up adding all the stuff I want to add to it yet, or even begun refactoring.

It's basically just a little commandline dictionary thing. Looks up the definitions, synonyms, antonyms, and rhymes of words.

There are a bunch of alternatives to this 'tool'(read: toy) that do the same things way better.

### How to use it
Don't.

If for some reason you want to though, just go [install NLTK](https://www.nltk.org/install.html)
and run `pip install requirements.txt` to grab all the dependencies.

Then you just do `python3.8 lexi.py --(options) (command) (word)`.

Available commands/options:
```
Options:
  --help  Show this message and exit.

Commands:
  about     Returns information about this script.
  anto      Usage: 'anto {word}' ~ Lists antonyms for the word.
  define    Usage: 'define {word}' ~ Looks up definitions for the word.
  examples  Usage: 'examples {word}' ~ Lists examples of the word in a
            sentence.
  rhyme     Usage: 'rhyme {word}' ~ Outputs all words which rhyme with the
            word
  syn       Usage: 'syn {word}' ~ Lists synonyms for the word.
```  
EG: 
```
python3.8 lexi.py rhyme door 
rhymes of door: 
1: abhor
2: abor
3: ador
4: adore
...
```  
Also as of writing this there is no way to truncate how many results you get from the commands, so you could get back hundreds of results... Some of them not even valid. I dunno, NLTK is weird.