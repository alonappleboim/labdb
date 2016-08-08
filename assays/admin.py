
from django.contrib import admin
from assays.models import *

admin.site.register(Assay)
admin.site.register(ProtocolModifier)
admin.site.register(Protocol)
admin.site.register(ProtocolModifierValue)
admin.site.register(ProtocolMetaFile)
