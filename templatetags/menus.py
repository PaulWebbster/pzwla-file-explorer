# -*- coding: utf-8 -*-
from django import template
from datetime import date
from urlparse import urlparse
from datetime import datetime
from django.contrib.sites.models import Site
from django.utils import timezone
from filer.models import Folder

register = template.Library()


@register.inclusion_tag("pzwla_file_explorer/menu.html")
def show_files_menu(**kwargs):
    context_dict = dict()

    root = Folder.objects.get(name="Inne")

    folders = []
    for fp in Folder.objects.all().filter(parent=root):
        folders.append(Folder.objects.get(id=fp.id))

    context_dict['menu_folders'] = folders

    return context_dict
