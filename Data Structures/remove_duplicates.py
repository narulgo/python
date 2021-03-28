def word_count(text):
    text = text.lower().split()
    result = {}
    for word in text:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result
def remove_duplicates(text):
    text = word_count(text)
    str = ''
    for word in text:
        if text[word.lower()] == 1:
            str += word + ' '
    return str[:-1]

# text = 'The quick brown fox jumps over the lazy dog'
# text = 'The quick brown fox jumps over brown the lazy dog'
# text = 'The quick brown fox fox fox fox fox The jumps brown over the lazy dog'
# quick jumps over lazy dog
text = 'The quick brown fox jumps over the lazy dog'

print(remove_duplicates(text))

assert remove_duplicates(text) == 'quick brown fox jumps over lazy dog'
# assert remove_duplicates(text) == 'quick jumps over lazy dog'
