import json
import os
import time
import networkx as nx
import pylab as plt

from bokeh.models import Circle, MultiLine
from bokeh.plotting import figure, from_networkx, show

def get_graph() -> dict:
    """конфертирует файл .json (путь к файлу хранится в переменной WIKI_FILE)
    паралеьно проверяет есть ли такой файл

    Returns:
        dict: граф в виде словаря
    """    
    # os.environ['WIKI_FILE'] = 'test_graph.json'
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

def render(data):
    G = nx.DiGraph()
    for key in data.keys():
        G.add_node(key, title=key, links=0)
        for val in data[key]:
            G.add_node(val, title=val,links=1)
            G.nodes[key]['links'] += 1
            G.add_edge(key, val)
    # for node in G.nodes:
    #     print(node['links'])
        # node['links'] = round(math.log(int(node['links'])))
    nx.draw(G, with_labels = True)
    plt.savefig('wiki_graph.png')

    edge_attrs = {}
    for start_node, end_node, _ in G.edges(data=True):
        edge_color = "darkgrey" 
        edge_attrs[(start_node, end_node)] = edge_color

    nx.set_edge_attributes(G, edge_attrs, "edge_color")

    plot = figure(width=800, height=800, x_range=(-1.2, 1.2), y_range=(-1.2, 1.2),
                x_axis_location=None, y_axis_location=None, toolbar_location=None,
                title="Interaction Graph", background_fill_color="#efefef",
                tooltips="title: @title links: @links")
    plot.grid.grid_line_color = None
    mapping = dict((n, i) for i, n in enumerate(G.nodes))
    H = nx.relabel_nodes(G, mapping)
    graph_renderer = from_networkx(H, nx.spring_layout, scale=1, center=(0, 0))
    graph_renderer.node_renderer.glyph = Circle(size='links', fill_color="lightblue")
    graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color",
                                                line_alpha=1, line_width=2)
    plot.renderers.append(graph_renderer)

    show(plot)
    
graph = get_graph()
render(graph)
time.sleep(10)
if os.path.exists("render_graph.html"):
        os.rename('render_graph.html','wiki_graph.html')
