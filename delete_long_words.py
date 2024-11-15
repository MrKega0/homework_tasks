def delete_long_words():
    words = [[i,len(i)] for i in input().split()]
    for word in range(len(words)):
        for i in range(len(words[word][0])):
            if words[word][0][i] in [',','.']:
                words.insert(word+1,[words[word][0][i],1])
                words[word][0] = words[word][0][:-1]
                words[word][1] -= 1


    max_len = 0
    for _, len_word in words:
        if len_word > max_len:
            max_len = len_word

    while True:
        try:
            words.remove(['',0])
        except ValueError:
            break

    out_st = ''
    for word in range(len(words)):
        if words[word][1] != max_len:
            out_st += words[word][0]
            if word == len(words)-1:
                break
            if words[word+1][0] not in [',','.',' ']:
                out_st += ' '
    return out_st

print(delete_long_words())