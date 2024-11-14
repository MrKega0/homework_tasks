def search_long_words():
    words = [[i,len(i)] for i in input().split()]
    for word in range(len(words)):
        for i in range(len(words[word][0])):
            if words[word][0][i] in [',','.']:
                words[word][0] = words[word][0][:-1]
                words[word][1] -= 1

    max_len = 0
    for _, len_word in words:
        if len_word > max_len:
            max_len = len_word

    out_st = ''
    for word, len_word in words:
        if len_word == max_len:
            out_st += word
            out_st += ', '
    return out_st

print(search_long_words())