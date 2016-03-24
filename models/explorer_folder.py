#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from filer.models import Folder
from ..settings import *
from django.contrib.staticfiles.templatetags.staticfiles import static


class ExplorerFolder(Folder):
    class Meta:
        proxy = True

    objects = models.Manager()

    @property
    def get_folder_icon(self):
        r = {}

        for size in ICON_SIZES:
            r[size] = static('pzwla_events/icons/folder_%sx%s.png' % (size, size))
        return r['32']

    @property
    def get_mb_size(self):
        return "%.2f MB" % (float(self.size)/1024/1024)
