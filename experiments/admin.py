
from django.contrib import admin
from django import forms
from nested_admin import *
from experiments.models import *

admin.site.site_header = 'LabDB'


class TabularAspectValue(NestedTabularInline):
    model = AspectValue
    extra = 0


class TabularExpFile(NestedTabularInline):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'rows': 1, 'cols': 40})}}
    model = ExperimentMetaFile
    extra = 0


class TabularSample(NestedTabularInline):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'rows': 1, 'cols': 40})}}
    model = Sample
    extra = 0
    inlines = [TabularAspectValue]


class ExperimentAdmin(NestedModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',
                       'desc',
                       'pub_url',
                       'data_url',
                       ('performed_by',
                        'performed_on'),
                       'aspects'),
            'description': ""
        }),
    )

    list_display = ('title', 'performed_by', 'performed_on', 'n_samples')
    inlines = [TabularExpFile, TabularSample]
    readonly_fields = ['samples',]
    filter_horizontal = ('aspects',)
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'rows': 6, 'cols': 100})}}
    list_filter = ('performed_by', 'performed_on', 'aspects')

admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Sample)
admin.site.register(Aspect)
admin.site.register(ExperimentMetaFile)
admin.site.register(AspectValue)