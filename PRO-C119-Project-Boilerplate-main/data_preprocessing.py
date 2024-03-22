# create an instance of class PorterStemmer
ps = PorterStemmer()

# creating function to stem words
def get_stem_words(words, ignore_words):
    stem_words = []
    for word in words:
        # write stemming algorithm:
        '''
        Check if word is not a part of stop word:
        1) lowercase it 
        2) stem it
        3) append it to stem_words list
        4) return the list
        '''
        # Add code here
        word_lower = word.lower()
        if word_lower not in ignore_words:
            stemmed_word = ps.stem(word_lower)
            stem_words.append(stemmed_word)
    return stem_words

# creating a function to make corpus
def create_bot_corpus(words, classes, pattern_word_tags_list, ignore_words):
    for intent in data['intents']:
        # Add all patterns and tags to a list
        for pattern in intent['patterns']:
            # tokenize the pattern
            pattern_words = nltk.word_tokenize(pattern.lower())  # lowercase the pattern
            # add the tokenized words to the words list
            words.extend(pattern_words)
            # add the 'tokenized word list' along with the 'tag' to pattern_word_tags_list
            pattern_word_tags_list.append((pattern_words, intent['tag']))

        # Add all tags to the classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

    stem_words = get_stem_words(words, ignore_words)

    # Remove duplicate words from stem_words
    stem_words = list(set(stem_words))

    # sort the stem_words list and classes list
    stem_words.sort()
    classes.sort()

    # print stem_words
    print('stem_words list : ', stem_words)

    return stem_words, classes, pattern_word_tags_list

# ... (rest of the code remains unchanged)
