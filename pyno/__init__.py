from pyno.tree_model import html, TreeSub, TreeNode
from pyno.browser_preview import browser_preview


# Set default settings for void elements
void_elements = 'br hr img input link meta area base col command embed keygen param source track wbr'.split(' ')
for tag in void_elements:
    TreeNode.defaults[tag] = {'_void_element': True}


# Create a special element for CDATA insertion
class CDATA(TreeSub):
    def construct(self, content):
        return f"<![CDATA[{content}]]>"


# todo consider adding some magic to add default parameters from construct as parameters on the object during initialization. (*It's funky but nice in practice*)

__version__ = "0.0.3-dev5"
