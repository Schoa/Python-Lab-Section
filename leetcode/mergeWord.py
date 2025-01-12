def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    i = 0

    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return "".join(result)

a = list(map(str, input().split()))
b = list(map(str, input().split()))

print(mergeAlternately(a, b))