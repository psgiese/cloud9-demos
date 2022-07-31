def bit_swap(x):
    """this is a function that helps you swap bit positions"""
    start = list(str(x))
    end = []
    for idx in range(len(start)):
        if idx % 2 == 0:
            end.append(start[idx + 1])
        else:
            end.append(start[idx - 1])
    return int("".join(map(str, end)))


print((bit_swap(1234)))
