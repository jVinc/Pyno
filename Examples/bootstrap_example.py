""" This example shows how to make costum components to generate the default bootstrap template """
from pyno import HTML as H, browser_preview


class BootstrapBody(H):
    """ Defines the minimal page template for bootstrap themed content"""
    def construct(self, *args,
                  title='Bootstrap 101 Template',
                  node_base_dir="resources/node_modules", **kwargs):

        return H.html(
           H.head(
                H.meta(charset="utf-8"),
                H.meta(http_equiv="X-UA-Compatible", content="IE=edge"),
                H.meta(name="viewport", content="width=device-width, initial-scale=1"),
                H.title(title),
                H.link(rel="stylesheet", href=node_base_dir + "/bootstrap/dist/css/bootstrap.min.css"),
                H.link(rel="stylesheet", href=node_base_dir + "/bootstrap/dist/css/starter-template.css"),
                '<!--[if lt IE 9]>',
                H.script(src=node_base_dir + "/html5shiv/dist/html5shiv.min.js"),
                H.script(src=node_base_dir + "/respond.js/dest/respond.min.js"),
                '<![endif]-->'),
           H.body(*args,
                  H.script(src=node_base_dir + "/jquery/dist/jquery.min.js"),
                  H.script(src=node_base_dir + "/bootstrap/dist/js/bootstrap.min.js")),
           lang="en")


class BootstrapStarterTemplate(H):
    """ Defines the default Bootstrap starter template"""
    def construct(self, *args, **kwargs):
        return BootstrapBody(
            H.nav(
                H.div(
                    H.div(
                        H.button(
                            H.span('Toggle navigation', Class="sr-only"),
                            H.span(Class='icon-bar'),
                            H.span(Class='icon-bar'),
                            H.span(Class='icon-bar'),
                            type="button",
                            Class="navbar-toggle collapsed",
                            data_togle="collapse",
                            data_target="#navbar",
                            aria_expand="false",
                            aria_controls="navbar"),
                        H.a('Project', Class="navbar-brand", href="#"),
                        Class="navbar-header"),
                    H.div(
                        H.ul(
                            H.li(H.a('Home', href="#"), Class="active"),
                            H.li(H.a('About', href="#about")),
                            H.li(H.a('Contact', href="#contact")),
                            Class="nav navbar-nav"), id="navbar-brand", Class="collapse navbar-collapse"),
                    Class="container"),
                Class="navbar navbar-inverse navbar-fixed-top"),
            H.div(H.div(*args, Class="starter-template"), Class="container"),
            title='Bootstrap starter template')


if __name__ == '__main__':
    # Generate the page with whatever content we would like:
    browser_preview(
        H.BootstrapStarterTemplate(
            H.h1('Hello world!')))
