# Start a new game, specifying the word to be guessed and the number of guesses allowed
# Show some instructions on how to proceed

# Keep asking for guesses until game won or lost

#   Get next letter to guess
#   Check if it's a valid guess - ie a single letter

#   If it's not a valid guess show an error message
#   Otherwise

#       Try this guess out and gets its status - there are 3 possibilities:
#       - the guess is correct
#       - the guess is wrong
#       - you've already guessed this letter previously

#       If it's not already been guessed ...
#           See if you've won, and if so display a suitable congratulatory message and break out of the loop
#           See if you've lost, and if so display a suitable commiserations message and break out of the loop

#       Display a status message showing:
#       - the status of this last guess
#       - the current word (with blanks for missing letters)
#       - a list of the correct letters you've already guessed
#       - a list of the incorrect letters you've already guessed
#       - how many guesses remain to you

# If you get here, have jumped out of the loop either because you won or list; display a final message