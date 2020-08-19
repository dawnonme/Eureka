def find_pothole(M, i, j):
    arr = [M[i][j]]
    for nei in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x = i + nei[0]
        y = j + nei[1]
        if x >= 0 and x < len(M) and y >= 0 and y < len(M[0]):
            arr.append(M[x][y])
    min_ele = min(arr)
    if min_ele == M[i][j]:
        return (i, j)

    return find_pothole
