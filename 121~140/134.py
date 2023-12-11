T = int(input())
for _ in range(T):
    word1, word2 = input().split()
    distances_array = []
    for ch1, ch2 in zip(word1, word2):
        distance = ord(ch2) - ord(ch1)
        if distance < 0:
            distance += 26
        distances_array.append(distance)
    print(f"Distances: {' '.join(map(str, distances))}")
