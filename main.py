import ch1text


def count_syllables(words):
    """This function takes a list of words and returns a total
       count of syllables across all words in the list.
    """
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count

    return count


def count_syllables_in_word(word):
    """This function takes a word in the form of a string
       and returns the number of syllables. Note this function is
       a heuristicand may not be 100% accurate.
    """
    count = 0
    # print(word, "words")

    # Fighting with endings
    endings = '.,;!?:'
    last_char = word[-1]    # the last character

    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    # Words with 3 letters
    if len(processed_word) <= 3:
        return 1

    # Remove silent "e" or "E"
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]

    # Find vowels in words and ignore consecutive vowels
    vowels = 'aeiouAEIOU'
    prev_char_was_vowel = False

    for char in processed_word:
        if char in vowels:
            # if the current character is a vowel, and previous character wasn't
            if not prev_char_was_vowel:
                count = count + 1
                # print(count)
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
        # print('prev', prev_char_was_vowel)

    if processed_word[-1] in 'yY':
        count = count + 1

    return count


def output_results(score):
    """This function takes a Flesch-Kincaid score and prints the
       corresponding reading level.
    """
    if score >= 90:
        print('Reading level of 5th Grade')
    elif score >= 80:
        print('Reading level of 6th Grade')
    elif score >= 70:
        print('Reading level of 7th Grade')
    elif score >= 60:
        print('Reading level of 8-9th Grade')
    elif score >= 50:
        print('Reading level of 10-12th Grade')
    elif score >= 30:
        print('Reading level of College Student')
    else:
        print('Reading level of College Graduate')


def compute_readability(text):
    """This function takes a text string of any length and prints out a
       grade-based readability score.
    """
    # total_words = 0
    # total_sentences = 0
    # total_syllables = 0
    # score = 0

    words = text.split()
    total_words = len(words)
    total_sentences = compute_sentences(text)
    total_syllables = count_syllables(words)

    score = (206.835 - 1.015 * (total_words/total_sentences)
             - 84.6 * (total_syllables/total_words))

    print(total_words, 'words')
    print(total_sentences, 'sentences')
    print(total_syllables, "syllables")
    print(round(score, 2), 'reading ease score index')

    output_results(score)


def compute_sentences(text):
    """This function counts the number of sentences in a string of text
       using period, semicolon, question mark and exclamation mark as
       terminals.
    """
    count = 0
    terminals = '.;?!'

    for char in text:
        if char in terminals:  # if char == '.' or char == ';' or char == '?' or char == '!':
            count = count + 1
            # print('test:', char, count)
    return count    # return command MUST be under FOR!


# call func, pass it the string from file, access the variable "text" in the file
compute_readability(ch1text.text)
# count sentences
compute_sentences(ch1text.text)
# count syllables
count_syllables(ch1text.text)
