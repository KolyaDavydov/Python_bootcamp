import itertools


def fix_wiring(cabels, sockets, plugs):
    return itertools.starmap(
        lambda x, y: 'weld '+x[0]+' to '+x[1]+' without plug'
        if not y else 'plug '+x[0]+' into '+x[1]+' using '+y,
        filter(
            lambda x: not x[0] is None,
            itertools.zip_longest(
                zip(
                    filter(lambda x: isinstance(x, str), cabels),
                    filter(lambda x: isinstance(x, str), sockets),
                ),
                filter(lambda x: isinstance(x, str), plugs)
            )
        )
    )


if __name__ == '__main__':
    print("\033[0m\033[32m____Первый тест____\033[0m")
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
    print()
    print("\033[0m\033[32m____Второй тест____\033[0m")
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]
    for c in fix_wiring(cables, sockets, plugs):
        print(c)
