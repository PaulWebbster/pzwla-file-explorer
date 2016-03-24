# -*- coding: utf-8 -*-
from django.views.generic.list import ListView
from django.views.generic import DetailView
from ..models import ExplorerFile
from ..models import ExplorerFolder
from filer.models import Folder


class SubFolderView(DetailView):
    template_name = 'pzwla_file_explorer/sub_folder.html'
    view_type = 'stats'
    model = Folder
    context_object_name = 'parent'

    def get_context_data(self, **kwargs):
        context = super(SubFolderView, self).get_context_data(**kwargs)

        root = Folder.objects.get(id=context['parent'].id)

        context['folders'] = self.get_sub_folders(root)
        context['files'] = self.get_files(root)

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
