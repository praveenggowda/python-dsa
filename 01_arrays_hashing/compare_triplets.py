def compare_triplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1

    return [alice, bob]


print(compare_triplets([5, 6, 7], [3, 6, 10]))   # [1, 1]
print(compare_triplets([17, 28, 30], [99, 16, 8]))  # [2, 1]
