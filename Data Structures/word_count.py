def word_count(text):
    text = text.lower().split()
    result = {}
    for word in text:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


text = 'I really really like apples apples I'
print(word_count(text))
assert word_count(text) == {'i': 2, 'really': 2, 'like': 1, 'apples': 2}
