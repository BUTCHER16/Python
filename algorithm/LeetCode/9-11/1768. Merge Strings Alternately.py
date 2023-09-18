word1 = "abcd"
word2 = "pq"
i = 0
j = 0
result = []
while i < len(word1) or j < len(word2):
    if i < len(word1):
        result +=word1[i]
        i += 1 
    if j < len(word2):
        result +=word2[j]
        j += 1
print("".join(result))