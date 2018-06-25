from flask import Flask
from pyno import HTML as H

app = Flask(__name__)


@H.construct
def cellShade(n):
    return H.td(H.strong(n), style=f'background-color:rgb({n}, {40*n}, {n});')


@app.route('/<lang>/')
# @H.construct    # No strictly needed unless the construct is needed elsewhere, however it illustrates that construct an be directly served on routes
def mainpage(lang):
    return H.html(H.body(H.table(H.tr(H.cellShade(i) for i in range(n)) for n in range(12))))

if __name__ == '__main__':

    print(H.mainpage())

    app.run(debug=True)

