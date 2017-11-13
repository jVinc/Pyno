from pyno import TreeSub, html as H, browser_preview





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