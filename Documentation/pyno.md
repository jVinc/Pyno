# Pyno a nano-framework for generating structured text

The basic gist of pyno is to use python function calls to guide the strugure of text tags. For instance this is a hello world example:

```
from pyno import html as H, browser_preview, TreeSub

browser_preview(
    H.html(
        H.head(H.style('div {font-weight:bold;font-size:22;')),
        H.body(H.div('Hello there! :)'))
    )
)
```

## User added extensions

A central feature of the syntax is the ease of adding custom elements. For instance you might want to add a special button component:
This is done by defining a class inheriting from Treenode and redefining the string output it creates when parsed.
```
class SpecialButton(TreeSub):
    def construct(self, *args, **kwargs):
        return '<button class="SpecialButtonClass" onclick="SpecialButtonJs()">Press me</button>'

browser_preview(
    H.html(
        H.body(
        H.div('Hello World'),
        H.SpecialButton()
        )
    ))
```

The above shows writing custom html, but you could also use pyno elements to define the custom element eg:

```python
class SpecialButton(TreeSub):
    def construct(self):
        return H.button('Press Me', Class='SpecialButtonClass', onclick="SpecialButtonJs()")

```

To define a costum element that takes input, extend the class to store and use the parameters:

```
class SpecialButton(TreeSub):
    def __init__(self, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = label

    def construct(self, *args, **kwargs):
        return H.button(self.label, Class='SpecialButtonClass', onclick="SpecialButtonJs()")

browser_preview(
    H.html(
        H.body(
        H.div('Hello World'),
        H.SpecialButton('hop in da lake')
        )
    ))
```

