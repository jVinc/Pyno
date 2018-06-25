dynamic = {
  aInternal: 10,
  aListener_list: [],
  set a(val) {
    this.aInternal = val;
    console.log('set called');
    for (var i=0, n = this.aListener_list.length; i < n; i++) {
        console.log('callback called');
        this.aListener_list[i](val);
    }
  },
  get a() {
    console.log('get called');
    return this.aInternal;
  },
  registerListener: function(listener) {
    this.aListener_list.push(listener);
  },
}


sliders = document.getElementsByClassName("slider")

var output = document.getElementById("demo");
dynamic.registerListener(function(val) { this.innerHTML = val; }.bind(output));

for (var n = 0, m = sliders.length; n < m; n++) {
    var slider = sliders[n];

    output.innerHTML = slider.value; // Display the default slider value

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
        dynamic.a = this.value;
    }

    dynamic.registerListener(function(val) { this.value = val; }.bind(slider));
}

document.getElementById('inputfield').onchange = function(val) {newDynamic.a = this.value};
dynamic.registerListener(function(val) { this.value = val; }.bind(document.getElementById('inputfield')));
