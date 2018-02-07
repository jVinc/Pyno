""" Examples of dynamically updated interactive controls"""

from pyno import HTML as H, browser_preview

css = """
.slider {
    -webkit-appearance: none;
    width: 100%;
    height: 15px;
    border-radius: 5px;   
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
}

.slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%; 
    background: #4CAF50;
    cursor: pointer;
}

.slider::-moz-range-thumb {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #4CAF50;
    cursor: pointer;
}
"""

"""
The basic idea is that all properties on dynamic.a have a setter that triggers callbacks. So elements that need to be 
updated on changes to dynamic.a can register a callback which triggers when other pieces of code call dynamic.a=23 or similar
"""

javascript = """


var Dynamic = new Proxy({listeners:{}},{
get(target, name) {
    if (name == 'listen'){
        return function(name, callback) { 
                if (name in target['listeners']) {
                    target['listeners'][name].push(callback)
                } else {
                    target['listeners'][name] = [callback]
                }
            }
    } else if (name in target) {
        return target[name];
    } else {
        return undefined
    }
},
set(target, name, value) {
    target[name] = value;
    // Run listeners on the variable name
    if (name in target.listeners) {
        for (i=0,m=target.listeners[name].length; i<m; i++){
            target.listeners[name][i](value);
        }
    }
}
// Todo apply could also be overwritten to extend functionality
})

function attachDynamic(element, dyn, name) {
    element.oninput = function() { dyn[name] = this.value; }
    dyn.listen(name, function(val) { this.value = val; }.bind(element));
}

sliders = document.getElementsByClassName("slider")

var output = document.getElementById("demo");
Dynamic.listen('a', function(val) {this.innerHTML = val;}.bind(output));

for (var n = 0, m = sliders.length; n < m; n++) {
    attachDynamic(sliders[n], Dynamic, 'a');
}

attachDynamic(document.getElementById('inputfield'), Dynamic, 'a');

Dynamic.a = 50;
"""

class slider(H):
    def construct(self):
        return H.div(H.input(type="range", min=1, max=100, value=50, Class="slider"), Class="slidercontainer")

page = H.html(H.head(H.style(css)),
              H.slider(),
              H.slider(),
              H.div(id="demo"),
              H.input(id='inputfield', type="text"),
              H.script(javascript))

browser_preview(page)

""" Aim is to make it work similar to
a = Dynamic(4)      // Makes a proxy object with value 4 and assigns a a reference to it
inputfield(value=a) // Creates a listener on the proxyobject a that updates input field.
a = 5;              // updates inputfield
# change value of input field to 23
console.log(a);     // returns 23
"""

""" Currently 

a = Dynamic.a
attachDynamic(Inputfield, Dynamic, 'a')
Dynamic.a = 5;              // updates inputfield
# change value of input field to 23
console.log(Dynamic.a);     // returns 23
"""
