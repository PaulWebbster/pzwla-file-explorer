#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from filer.models import Folder


class MainExplorerFolder(models.Model):

    class Meta:
        verbose_name = "Folder glowny przegladarki"
        verbose_name_plural = "Folder glowny przegladarki"

    name = models.CharField("Folder główny przeglądarki", max_length=26, default='Folder główny przeglądarki')
    folder = models.ForeignKey(Folder)
