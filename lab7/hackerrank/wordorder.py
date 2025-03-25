from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())  
    words = [input().strip() for _ in range(n)]  

    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(len(word_count))

    print(" ".join(map(str, word_count.values())))
