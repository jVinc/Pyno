""" Examples of dynamically updated interactive controls"""

from pyno import HTML as H, browser_preview


"""
The basic idea is that all properties on dynamic.a have a setter that triggers callbacks. So elements that need to be 
updated on changes to dynamic.a can register a callback which triggers when other pieces of code call dynamic.a=23 or similar
"""


class slider(H):
    def construct(self):
        return H.div(H.input(type="range", min=1, max=100, value=50, Class="slider"), Class="slidercontainer")

page = H.html(H.head(H.Import('range-slider.css')),
              H.slider(),
              H.slider(),
              H.div(id="demo"),
              H.div(id="demo2"),
              H.input(id='inputfield', type="text"),
              H.Import('resources/node_modules/Dynamic-Interactivity/dynamic_interactivity.js'))

browser_preview(page)

""" Aim is to make it work similar to
a = Dynamic(4)      // Makes a proxy object with value 4 and assigns a a reference to it
inputfield(value=Dynamic(a)) // Creates a listener on the proxyobject a that updates input field.
a = 5;              // updates inputfield
# change value of input field to 23
console.log(a);     // returns 23
"""

""" Currently 

a = Dynamic.a // gets value not referene
attachDynamic(Inputfield, Dynamic, 'a')
Dynamic.a = 5;              // updates inputfield
# change value of input field to 23
console.log(Dynamic.a);     // returns 23
"""
