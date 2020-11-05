# Find the maximum product of two distinct numbers in a sequence of non-negative integers.

def max_pair_product_naive(pair):
    max_product = 0
    for i in range(len(pair)):
        for j in range(i + 1, len(pair)):
            max_product = max(max_product, pair[i] * pair[j])
    return max_product


m = input().split()
pair = []
for i in range(len(m)):
    pair.append(int(m[i]))
print(max_pair_product_naive(pair))

