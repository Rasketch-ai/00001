''' Что-то чтобы пайлинт не ругался :) '''
TEXT = "Master of puppets I'm pulling your strings Twisting your mind and smashing your dreams"
PATTERN = "Master"
def rabin_carp(text,pattern):
    ''' Алгоритм Рабина-Карпа '''
    result = ([])
    pattern_sum = 0
    main_sum = 0
    for k in range (0,len(pattern)):
        pattern_sum += ord(pattern[k])
    for k in range (0, len(pattern)):
        main_sum += ord(text[k])
    for k in range (len(text)-len(pattern)):
        if main_sum == pattern_sum:
            if text.startswith(pattern,k):
                result.append(k)
        main_sum += (ord(text[k + len(pattern)]) - ord(text[k]))
    return result
if rabin_carp(TEXT,PATTERN) != []:
    print ("Подстрока",PATTERN,"Найдена на позициях",rabin_carp(TEXT,PATTERN))
