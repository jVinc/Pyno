from pyno import HTML as H, browser_preview, TreeNode

TreeNode.defaults['div'] = {'style': 'background-color:Green;'}

browser_preview(
    H.html(
        H.head(H.style('div {font-weight:bold;font-size:22;}')),
        H.body(H.div('Hello there! :)'), H.div('It`s a meee!', H.ul(H.li(n) for n in range(1, 10))))
    )
)
