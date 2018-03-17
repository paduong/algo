# Spanning Forest visualization
# Requires graphviz

from graphviz import Digraph

spanning_colors = {'discovery': 'black', 'forward': 'blue', 'backward': 'red', 'cross': 'orange' }

class SpanningForest:

    def __init__(self, colors=spanning_colors):
        self.__iner_tree = Digraph()
        self.__colors = colors

    def discovery(self, src, dst):
        self.__iner_tree.edge(str(src), str(dst), color=self.__colors['discovery'])

    def forward(self, src, dst):
        self.__iner_tree.edge(str(src), str(dst), constraint='false', color=self.__colors['forward'])

    def backward(self, src, dst):
        self.__iner_tree.edge(str(src), str(dst), constraint='false', color=self.__colors['backward'])

    def cross(self, src, dst):
        self.__iner_tree.edge(str(src), str(dst), constraint='false', color=self.__colors['cross'])

    def _repr_svg_(self):
        return self.__iner_tree._repr_svg_()

    def _display(self):
        '''Displays SVG representation directly in IPython notebook.

        Requires IPython and (through method _repr_svg_) graphviz modules.
        '''
        try:
            from IPython.display import display_svg
        except:
            raise Exception('Missing moduke: IPtyhon')
        display_svg(self)


    @property
    def source(self):
        return self.__iner_tree.source
