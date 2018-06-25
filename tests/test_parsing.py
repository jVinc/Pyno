from pyno import HTML as H

def test_iterator_unwrapping():
    page = H.ul(H.li(n) for n in range(1, 10))

    assert str(page) == '<ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li><li>7</li><li>8</li><li>9</li></ul>', 'Default behavior is broken'
    assert str(page) == '<ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li><li>7</li><li>8</li><li>9</li></ul>', 'Iterators might not be unrwapped correctly'

def test_default_arguments():
    H.defaults['div'] = {'color': 'Green'}

    str(H.div('test')) == '<div color="Green">test</div>', 'default arguments is broken'
