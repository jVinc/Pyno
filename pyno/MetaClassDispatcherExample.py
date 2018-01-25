

class NodeDispatcher(type):
  def __getattr__(self, name):
    return 'Dispatched: %s-Node' % name

class HTML(metaclass=NodeDispatcher):
    pass



if __name__ == '__main__':
    H = HTML

    H.test = 'k'
    print(H.test)

    print(H.a, H.b)