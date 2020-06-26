from nose.tools import assert_equal


def criarMatriz():
    m = [(0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 1),
         (0, 1, 0, 0)]
    return m


def imprimirMatriz(mat):
    for i in range(0, len(mat)):
        print(mat[i])


def moverObj(mat, actX, actY, finX, finY):
    moves = [(actX, actY)]
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if actY != finY and actX != finX:
                if mat[actX + 1][actY] == 1:
                    actY += 1
                else:
                    actX += 1
            else:
                break
            moves.append((actX, actY))
    moves.append((finX, finY))
    return moves


def main():
    expected = [(0, 0), (1, 0), (2, 0),
                (2, 1), (3, 1), (4, 1),
                (5, 1), (5, 2), (6, 2),
                (7, 2), (7, 3)]
    actX = 0
    actY = 0
    finX = 7
    finY = 3
    mat = criarMatriz()
    imprimirMatriz(mat)
    moves = moverObj(mat, actX, actY, finX, finY)
    print(moves)
    assert_equal(expected, moves, None)


if __name__ == "__main__":
    main()
