from pyno.tree_model import html, TreeSub, TreeNode
from pyno.browser_preview import browser_preview


# Set default settings for void elements
void_elements = 'br hr img input link meta area base col command embed keygen param source track wbr'.split(' ')
for tag in void_elements:
    TreeNode.defaults[tag] = {'_void_element': True}


from pyno.costum_tags import CDATA, Include


# todo consider adding some magic to add default parameters from construct as parameters on the object during initialization. (*It's funky but nice in practice*)

__version__ = "0.0.4-dev1"
