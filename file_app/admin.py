from django.contrib import admin
from file_app.models import File
from mptt.admin import DraggableMPTTAdmin

admin.site.register(File, DraggableMPTTAdmin)