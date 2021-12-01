# Foreign Language Flash Cards - Working EXE

A foreign language frequently used words application using tkinter. 
Day 31 Python Bootcamp

## NOTICE
If you download the .exe, Windows Defender or Avast will flag it as malware. This
is because the executable is unsigned. This program is for display purposes only
and really isn't being designed for mass distribution.

It is for anyone who wants to have a working example of the code found in the repo.


## Usage
This is a reformatted version [original](https://github.com/megler/Day31-Foreign_Language-Flashcards)
using OOP and compiled into a working EXE file.

Unlike the non-executable file, this one does not have the ability to remove
known words and update the CSV. However, you can hit the button and go from one
card to the next.

The program defaults to Spanish words, but you can also use a French dictionary.
The foreign word will be shown for 3 seconds, then it's English translation will
be shown. If you know the word, click the green checkmark button and the word
will be removed from the dictionary. Click the red X and the deck will be 
reshuffled and you'll be shown a new card.

If you want to use a new dictionary, change Line 28:

    words = pd.read_csv("data/spanish_words.csv") 
    
to correct csv and find/replace "Spanish" to new column head in csv
(eg. "French", "German", etc)

## License
[MIT](https://choosealicense.com/licenses/mit/)