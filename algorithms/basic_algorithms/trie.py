basic_trie = {
    # a and add word
    'a': {
        'd': {
            'd': {'word_end': True},
            'word_end': False},
        'word_end': True},
    # hi word
    'h': {
        'i': {'word_end': True},
        'word_end': False}}


def is_word(word):
    """
    Look for the word in `basic_trie`
    """
    current_node = basic_trie

    for char in word:
        if char not in current_node:
            return False

        current_node = current_node[char]

    return current_node['word_end']


# Test words

def test(test_words):
    for word in test_words:
        if is_word(word):
            print(f'"{word}" is a word.')
        else:
            print(f'"{word}" is not a word.')


if __name__ == '__main__':
    test(['ap', 'add'])
