"""
This example showcases a decorator used in the most typical form of construct definition
for the majority of cases where building a state holding class is not neccesary.
"""
from pyno import HTML as H

class unordered_list(H):
    def construct(self, content_nodes):
        return H.ul(H.li(x) for x in content_nodes)


@H.construct
def ordered_list(content_nodes):
    return H.ol(H.li(x) for x in content_nodes)


if __name__ == '__main__':

    print(H.unordered_list(range(4)))
    print(H.ordered_list(range(4)))