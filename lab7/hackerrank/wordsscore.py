def score_words(words):
    vowels = 'aeiouy'
    total_score = 0
    
    for word in words:
        vowel_count = 0
        
        for char in word:
            if char in vowels:
                vowel_count += 1
        
        if vowel_count % 2 == 0:
            total_score += 2
        else:
            total_score += 1
    
    return total_score

if __name__ == "__main__":
    n = int(input())
    words = input().split()
    result = score_words(words)
    print(result)
