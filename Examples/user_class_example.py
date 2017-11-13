from pyno import html as H, browser_preview, TreeNode, TreeSub

TreeNode.defaults['div'] = {'style': 'background-color:Purple;'}
TreeNode.defaults['my_page'] = {'style': 'background-color:Yellow;'}

class my_page(TreeSub):
    def construct(self, *args, **kwargs):
        an_element = H.div('Pope')

        value = H.html(
            H.head(H.style('div {font-weight:bold;font-size:22;}')),
            H.body(*self.args, style=kwargs['style']),
            an_element
        )

        an_element.style = "background-color:green;"

        return value


if __name__ == '__main__':

    browser_preview(
        H.my_page(H.div('Hello there! :)'), H.div('It`s a meee! Mario!', H.ul(H.li(n) for n in range(1, 10))))
    )
