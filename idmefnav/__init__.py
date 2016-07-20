import pkg_resources

from prewikka import database, env, utils, view, error
from . import templates

import json
import re

import graph_generator

class IDMEFNav(view.View):
    class IDMEFNavParameters(view.Parameters):
        def register(self):
            self.optional("idmef_class", str, default="IDMEF-Message")

    _HTDOCS_DIR = pkg_resources.resource_filename(__name__, 'htdocs')


    plugin_name = "IDMEFNav"
    plugin_author = "Sélim Menouar"
    plugin_license = "GPL"
    plugin_version = "1.0.0"
    plugin_copyright = "CSSI"
    plugin_description = "IDMEF navigator"
    plugin_htdocs = (("idmefnav", _HTDOCS_DIR),)
    view_template = templates.idmefnav
    view_parameters = IDMEFNavParameters
    view_name = N_("IDMEF")
    view_section = N_("Help")

    def __init__(self):
        view.View.__init__(self)
        self.schema = graph_generator.Schema("%s/yaml" % self._HTDOCS_DIR)

    def render(self):
        idmef_class = self.parameters["idmef_class"]

        if idmef_class not in self.schema:
            raise error.PrewikkaUserError("Parameter Error", _("%s is not a valid IDMEF class") % idmef_class)

        self.dataset["schema"] = self.schema[idmef_class]
        self.dataset["full_schema"] = self.schema
        self.dataset["link"] = self.view_path

        with open("%s/graph/%s.svg" % (self._HTDOCS_DIR, idmef_class), 'r') as stream:
            self.dataset["svg"] = re.sub(r"\d+pt", "100%", stream.read())

        with open("%s/graph/%s" % (self._HTDOCS_DIR, idmef_class), 'r') as stream:
            self.dataset["dot"] = stream.read()

        self.dataset["png"] = "idmefnav/graph/%s.png" % idmef_class

