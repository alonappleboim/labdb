from __future__ import unicode_literals

from django.db import models
from experiments.models import Sample
from labdb.settings import fss
from django.contrib.auth.models import User


class ProtocolModifier(models.Model):
    """
    A modifiable attribure of a protocol, e.g. concentration of an enzyme.
    """
    STR = 'STR'
    INT = 'INT'
    FLT = 'FLT'
    TYPES = ((STR, 'string'), (INT, 'integer'), (FLT, 'float'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=TYPES, default=STR)
    units = models.CharField(max_length=100)

    def __str__(self):
        return '%s [%s]' % (self.name, self.units)


class Protocol(models.Model):
    """
    A modifiable procedure used to extract data from a biological sample.
    """
    title = models.CharField(max_length=60)
    desc = models.TextField(max_length=2000, verbose_name='description')
    pub_url = models.URLField(help_text='if published, link to protocol', blank=True, verbose_name='publication url')
    prot_mods = models.ManyToManyField(ProtocolModifier, blank=True, verbose_name='protocol_modifiers')
    samples = models.ManyToManyField(Sample, blank=True, verbose_name='protocol assays', through='Assay')
    data_type = models.ForeignKey('data.DataType', related_name='generating_protocols',
                                  limit_choices_to={'is_raw': True})

    def __str__(self):
        return self.short_name


class Assay(models.Model):
    """
    An application of a protocol to a biological sample.
    """
    performed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='assays')
    performed_on = models.DateField(help_text='the date on which assay was perfomed', verbose_name='on')
    protocol = models.ForeignKey(Protocol, blank=True, related_name='assays')
    sample = models.ForeignKey(Sample, blank=True, related_name='assays')


class ProtocolModifierValue(models.Model):
    """
    A specific protocol modifier value, related to a specific assay.
    """
    assay = models.ForeignKey(Assay, on_delete=models.CASCADE, related_name='protocol_modifier_values')
    modifier = models.ForeignKey(ProtocolModifier, on_delete=models.CASCADE, related_name='values')
    string_value = models.CharField(max_length=100)

    def __str__(self):
        return self.string_value

    def _value(self):
        if self.var.type == ProtocolModifier.INT:
            return int(self._value)
        elif self.var.type == ProtocolModifier.FLT:
            return float(self._value)
        elif self.var.type == ProtocolModifier.STR:
            return self._value
        else:
            raise TypeError('Unknown dimension type')


class ProtocolMetaFile(models.Model):
    """
    A file attached to a protocol.
    """
    attached_to = models.ForeignKey(Protocol, on_delete=models.CASCADE, related_name='meta_files')
    upload_time = models.DateField(auto_now=True)
    file = models.FileField(storage=fss, upload_to='meta/protocol/')
    desc = models.TextField(verbose_name='description', max_length=2000, blank=True)
