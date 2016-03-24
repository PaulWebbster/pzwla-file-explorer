#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PzwlaFileExplorerApp(CMSApp):
    name = _("Przegladarka plikow")  # give your app a name, this is required
    urls = ["pzwla_file_explorer.urls"]  # link your app to url configuration(s)
    app_name = "pzwla_file_explorer"

apphook_pool.register(PzwlaFileExplorerApp)  # register your app