from pyno import HTML as H, TreeNode, serve_example

H.defaults['h1'] = {'style': 'background-color:Blue;'}

if __name__ == '__main__':

    serve_example(H.html(
        H.h1('Hello World'),
        H.div(H.h2('And so it continues')),
        H.ul(H.li(n) for n in range(1, 10)),
        H.svg(H.circle(cx=50, cy=50, r=20, fill='red'), width=100, height=100),
        H.p('this is some text in a paragra'),
        H.p('and this is some more text'),
        H.p('Just for the sake of it I´ll add som´ore')
    ))