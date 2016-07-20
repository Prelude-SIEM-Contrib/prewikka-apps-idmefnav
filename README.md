## IDMEF nav plugins

This plugin add pretty UML graph of the IDMEF schema. (see [RFC 4765](https://www.ietf.org/rfc/rfc4765.txt))

It use graphviz to generate the graphs

## How to use Prewikka apps

### Requirements

You need Prewikka 3.0.0 or higher.

### Source

The git repo for Prewikka apps is available on [GitHub](https://github.com/Prelude-SIEM-Contrib/prewikka-apps-idmefnav) and can be cloned like this:

    git clone https://github.com/Prelude-SIEM-Contrib/prewikka-apps-idmefnav.git

### Install

Once the source code downloaded:

    cd prewikka-apps-helloworld
    cheetah-compile */templates/*.tmpl
    python setup.py install

Then restart Prewikka.

Depending on the app, you may need to activate it by visiting the Settings > Plugins page.

### License

The code is released under the GPLv2 license. See the COPYING file.

### Development

Please feel free to propose your own Prewikka plugins by submitting a pull request.

## Specific

If you want to regenerate the graph with graphviz :

    python idmefnav/graph_generator.py