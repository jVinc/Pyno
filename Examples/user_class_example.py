from pyno import html as H, browser_preview, TreeNode

TreeNode.defaults['div'] = {'style': 'background-color:Purple;'}
TreeNode.defaults['my_page'] = {'style': 'background-color:Yellow;'}

class MyPage(H):
    def construct(self, *args, flymetothemoon='sure', **kwargs):
        an_element = H.div('Pope')

        value = H.html(
            H.head(H.style('div {font-weight:bold;font-size:22;}')),
            H.body(*self.args, style=kwargs.get('style', '')),
            an_element
        )

        an_element.style = "background-color:green;"

        return value


if __name__ == '__main__':

    browser_preview(
        H.MyPage(H.div('Hello there! :)'), H.div('It`s a meee! Mario!', H.ul(H.li(n) for n in range(1, 10))))
    )
