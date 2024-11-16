import json
import os
import argparse


def arg_parser() -> argparse.Namespace:
    """Парсит аргументы командной строки и возвращает

    Returns:
        argparse.Namespace: аргументы
    """
    parser = argparse.ArgumentParser(description='Parser')
    parser.add_argument("-v", action='store_true', default=False, help="Output all path between graphs", dest="v_")
    parser.add_argument("--from", type=str, required=True, help="From which graph need find route", dest="from_")
    parser.add_argument("--to", type=str, required=True, help="To which graph need find route", dest="to_")
    parser.add_argument("--non-directed", action='store_true', default=False,
                        help="Removes the direction from the edges of the graph", dest="non_directed_")

    return parser.parse_args()


def get_graph() -> dict:
    """конфертирует файл .json (путь к файлу хранится в переменной WIKI_FILE)
    паралеьно проверяет есть ли такой файл

    Returns:
        dict: граф в виде словаря
    """
    path = os.environ.get('WIKI_FILE')
    if not path:
        print('\033[31mWIKI_FILE enviroment veriable not found\033[0m')
        exit(-1)
    if not os.path.exists(path):
        print('\033[31mDatabase not found\033[0m')
        exit(-1)
    with open(path, 'r') as f:
        graph = json.load(f)

    return graph


def get_non_derected_graph(graph: dict) -> dict:
    """конвертирует направленный граф в ненаправленый

    Args:
        graph (dict): направленный граф

    Returns:
        dict: ненаправленный граф
    """
    new_graph: dict = graph.copy()
    for vertex in graph:
        for mention in graph[vertex]:
            if mention not in graph:
                new_graph[mention] = [vertex]
            elif vertex not in graph[mention]:
                new_graph[mention].append(vertex)
    return new_graph


def get_route(graph, from_, to_) -> list:
    """Строит маршрут между двумя вершинами графа

    Args:
        graph (dict): граф
        from_ (str): начальная точка маршрута
        to_ (str): конечная точка маршрута

    Returns:
        list: маршрут между вершинами графа
        если вершин нет в графе или маршрута не существует
        возвращает пустой список
    """
    if from_ not in graph or to_ not in graph:
        return []
    if from_ == to_:
        return [from_]
    route = {page: [from_] for page in graph[from_]}
    while to_ not in route:
        new_route = {}
        for page in route:
            if page in graph:
                for next in graph[page]:
                    if next not in route[page]:
                        new_route[next] = route[page] + [page]
        route.update(new_route)
        if all(page not in graph for page in route):
            break
    # print(route)
    return route[to_] + [to_] if to_ in route else []


def print_route(route: list) -> str:
    """выводит маршрут в консоль

    Args:
        route (list): маршрут - список вершин

    Returns:
        str: строковое представление маршрута
    """
    temp_route_str = ""
    for i in range(len(route) - 1):
        temp_route_str += route[i] + ' -> '
    route_str = temp_route_str + route[-1]
    return route_str


def main():
    args = arg_parser()
    os.environ['WIKI_FILE'] = 'graph.json'
    graph = get_graph()
    if args.non_directed_:
        graph = get_non_derected_graph(graph)

    route = get_route(graph, args.from_, args.to_)
    if not len(route):
        print('\033[31mPath not found\033[0m')
    else:
        if args.v_:
            path = print_route(route)
            print('\033[32m', path, '\033[0m')
        print('\033[32m', len(route) - 1, '\033[0m')


if __name__ == '__main__':
    # Тестовый файл нахождится после первого скрипта: 'graph.json'
    # Варианты тестовых скриптов:
    # python3 shortest_path.py -v --from 'Paul Erdős' --to 'Erdős number' --non-directed
    # python3 shortest_path.py -v --from 'Erdős number' --to 'Paul Erdős'
    main()
