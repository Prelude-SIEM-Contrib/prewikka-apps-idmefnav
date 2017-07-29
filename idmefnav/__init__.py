from __future__ import absolute_import, division, print_function, unicode_literals


from prewikka import version, database, utils, view, error, template, mainmenu

import re

from .graph_generator import Schema 
import pkg_resources

class IDMEFNavParameters(mainmenu.MainMenuParameters):
    allow_extra_parameters = True

class IDMEFNav(view.View):
    _HTDOCS_DIR = pkg_resources.resource_filename(__name__, 'htdocs')

    plugin_name = "IDMEFNav"
    plugin_author = "Sélim Ménouar, Thomas Andrejak"
    plugin_license = version.__license__
    plugin_version = version.__version__
    plugin_copyright = version.__copyright__
    plugin_description = N_("IDMEF navigator")
    plugin_htdocs = (("idmefnav", _HTDOCS_DIR),)

    view_parameters = IDMEFNavParameters

    def __init__(self):
        view.View.__init__(self)
        self.schema = Schema("%s/yaml" % self._HTDOCS_DIR)

    @view.route("/help/idmefnav", menu=(N_("Help"), N_("IDMEF")))
    def render(self):
        idmef_class = env.request.parameters.get("idmef_class", "IDMEF-Message")
        dataset = {}

        if idmef_class not in self.schema:
            raise error.PrewikkaUserError(N_("Parameter Error"), N_("%(idmefclass)s is not a valid IDMEF class", {'idmefclass':idmef_class}))

        dataset["schema"] = self.schema[idmef_class]
        dataset["full_schema"] = self.schema
        dataset["link"] = self.view_path

        with open("%s/graph/%s.svg" % (self._HTDOCS_DIR, idmef_class), 'r') as stream:
            dataset["svg"] = re.sub(r"\d+pt", "100%", stream.read())

        with open("%s/graph/%s" % (self._HTDOCS_DIR, idmef_class), 'r') as stream:
            dataset["dot"] = stream.read()

        dataset["png"] = "idmefnav/graph/%s.png" % idmef_class

        return template.PrewikkaTemplate(__name__, "templates/idmefnav.mak").render(**dataset)
