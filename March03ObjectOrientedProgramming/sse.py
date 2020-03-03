def sse(word, phrase):
    count = 0
    for i in range(len(word)):
        if word[i:i+len(phrase)] == phrase:
            count += 1   
    return count

word = "hi"
phrase = "hi, hi hello hello hi"
print(sse(word,phrase))