text = "End of passion play, crumbling away I'm your source of self-destruction Veins that pump with fear,sucking darkest clear Leading on your deaths' construction Taste me you will see More is all you need Dedicated to How I'm killing you Obey your master Master Master of puppets I'm pulling your strings Twisting your mind and smashing your dreams Blinded by me, you can't see a thing Just call my name, 'cause I'll hear you scream Master Master Just call my name, 'cause I'll hear you scream Master Master, yeah Needlework the way, never you betray Life of death becoming clearer Pain monopoly, ritual misery Chop your breakfast on a mirror Taste me you will see More is all you need You're dedicated to How I'm fucking you Obey your master Master Master of puppets I'm pulling your strings Twisting your mind and smashing your fucking dreams Blinded by me, you can't see a thing Just call my name, 'cause I'll hear you scream Master Master Just call my name, 'cause I'll hear you scream Master Master"
pattern = "Master"
def rabin_carp(text,pattern):
    result = ([])
    pattern_sum = 0
    main_sum = 0
    for k in range (0,len(pattern)):
        pattern_sum += ord(pattern[k])
    for k in range (0, len(pattern)):
        main_sum += ord(text[k])
    for k in range (len(text)-len(pattern)):
        if main_sum == pattern_sum :
            if text.startswith(pattern,k) : result.append(k) 
        main_sum += (ord(text[k + len(pattern)]) - ord(text[k]))
    return (result)
result = rabin_carp(text,pattern)
if (result != []): print ("Подстрока",pattern,"Найдена на позициях",result)


         

