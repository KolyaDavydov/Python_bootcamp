from itertools import tee 


def mul(a, b):
    b_iter = tee(zip(*b), len(a))
    return [
        [
            sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
            for col_b in b_iter[i]
        ] for i, row_a in enumerate(a)
    ]


if __name__ == '__main__':
    x = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    y = [
        [1, 2],
        [3, 4],
        [5, 6],
    ]

    print(mul(x, y))
