# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic import DetailView
from ..models import ExplorerFile
from ..models import ExplorerFolder
from filer.models import Folder


class RootFolderView(ListView):
    template_name = 'pzwla_file_explorer/root.html'
    view_type = 'stats'
    model = Folder

    def get_context_data(self, **kwargs):
        context = super(RootFolderView, self).get_context_data(**kwargs)

        root = Folder.objects.get(name="Inne")

        context['folders'] = self.get_sub_folders(root)
        context['files'] = self.get_files(root)

        print "Folders are: "
        print context['folders']

        return context

    @staticmethod
    def get_files(folder):
        files = []
        for fp in folder.files:
            files.append(ExplorerFile.objects.get(id=fp.id))

        return files

    @staticmethod
    def get_sub_folders(folder):
        folders = []
        for fp in Folder.objects.all().filter(parent=folder):
            folders.append(ExplorerFolder.objects.get(id=fp.id))

        return folders
