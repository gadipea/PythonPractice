
def permutations(array):
    if len(array) == 1:
        return [array]
    if len(array) == 0:
        return []
    out = []
    for i in range(len(array)):
        for p in permutations(array[:i] + array[i + 1:]):
            out.append([array[i]] + p)
    return out


if __name__ == "__main__":
    print(permutations(list(map(int, input().split()))))
