from __future__ import unicode_literals

import os

from django.db import models
from labdb.settings import fss
from assays.models import Assay


def get_storage_path(instance, fname):
    """
    store by year, experiment, and data type.
    """
    y = instance.assay.experiment.performed_on.year
    e = ''.join(x for x in instance.assay.experiment.title.replace(' ','_') if x.isalnum())
    t = instance.type.name
    return os.path.sep.join([str(y), e, t])


class DataType(models.Model):
    """
    A dimension alteredand the experiment, e.g. time since some event, concnentration of some molecule in medium, etc.
    """
    name = models.CharField(max_length=100)
    s_desc = models.CharField(max_length=200, verbose_name='short_description',
                              help_text='A concise description of the file format, for quick orientation')
    desc = models.CharField(max_length=2000, verbose_name='description',
                            help_text='A complete and accurate description of the file format.')
    file_extension = models.CharField(max_length=10)
    is_raw = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Data(models.Model):
    """
    A data entry. Can be any file.
    """
    assay = models.OneToOneField(Assay, on_delete=models.PROTECT, related_name='data')
    file = models.FileField(storage=fss, upload_to=get_storage_path)
    type = models.ForeignKey(DataType, on_delete=models.PROTECT, related_name='data_set')

"""
This file will also contain various annotation data
"""