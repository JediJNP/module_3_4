print('Однокоренные')
print('------------')

def single_root_words(root_word, *other_words ):
    same_words = []
    root_word_lower = root_word.lower()
    for i in other_words:
        i_original = i
        i_lower = i.lower()
        if i_lower in root_word_lower or root_word_lower in i_lower:
            same_words.append(i_original)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

