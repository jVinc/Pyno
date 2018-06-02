""" This examples highlights a case using some of the void elements.

Pyno outputs void elements in the fully valid HTML5 form, <br /> which does however employ unessesary syntax.
This is a personal preference to distinguish void elements from opening tags. If desired, settings can be set to employ
the more minimal <br> syntax.

An element is set to be considered a void element through the setting _void_element as such:
TreeNode.defaults['br'] = {'_void_element': True}

There are 16 html tags that are set to be void elements per default such as br and meta. If desired the void element
option can simply be removed from these by setting TreeNode.defaults['meta'] = {'_void_element': False}

"""

from pyno import HTML as H

H.defaults['div'] = {'style': 'background-color:Green;'}
H.defaults['br'] = {'_void_element': False}
H.defaults['div'] = {'_void_element': True}

print(str(
    H.html(H.br(),
        H.head(H.meta('content of void tags gets dropped', name='description', content='Samples with void elements'),
               H.style('div {font-weight:bold;font-size:22;}')
               ),
        H.body(H.div('Hello there! :)'), H.div('It`s a meee!', H.ul(H.li(n) for n in range(1, 10))))
    )
))
