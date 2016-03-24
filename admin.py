# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html
from models import MainExplorerFolder


class MainExplorerFolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_files_folder',)

    def add_files_folder(self, obj):
        return format_html('<a href="/admin/filer/folder/%s/list/">Dodaj/modyfikuj pliki do pobrania</a>' % obj.folder.id)
        show_firm_url.allow_tags = True

    add_files_folder.short_description = "Pliki do pobrania"

    def has_add_permission(self, request):
        if MainExplorerFolder.objects.all().count() == 0:
            return True

        return False

admin.site.register(MainExplorerFolder, MainExplorerFolderAdmin)
