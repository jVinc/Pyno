from pyno import HTML as H, serve_example

serve_example(H.html(
    H.h1('Hello World'),
    H.div(H.h2('And so it continues')),
    H.svg(H.circle(cx=50, cy=50, r=20, fill='red'), width=100, height=100)
))