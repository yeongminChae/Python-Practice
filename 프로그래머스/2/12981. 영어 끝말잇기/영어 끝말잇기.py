def solution(n, words):
    used_words = set()
    last_char = words[0][0]
    
    for i, j in enumerate(words) :
        if j[0] != last_char or j in used_words :
            return [(i % n) + 1, (i // n) + 1]
        
        used_words.add(j)
        last_char = j[-1]
    
    return [0, 0]