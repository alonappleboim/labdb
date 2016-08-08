from __future__ import unicode_literals

from django.db import models
from labdb.settings import fss
from django.contrib.auth.models import User
from genetics.models import *


class Aspect(models.Model):
    """
    A property that is alterable in an experiment, e.g. medium type, time since some event, concnentration of some
    molecule in medium, etc.
    """
    STR = 'STR'
    INT = 'INT'
    FLT = 'FLT'
    TYPES = ((STR, 'string'), (INT, 'integer'), (FLT, 'float'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=3, choices=TYPES, default=STR)
    units = models.CharField(max_length=100)
    samples = models.ManyToManyField('Sample', through='AspectValue')

    def __str__(self):
        return '%s [%s]' % (self.name, self.units)


class Experiment(models.Model):
    """
        A conceptual frame managing related samples that were handled in the same day by the same user.
    """
    performed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='experiments')
    performed_on = models.DateField(help_text='the date on which experiment was perfomed', verbose_name='on')
    title = models.CharField(max_length=120, unique=True)
    desc = models.TextField(max_length=2000, verbose_name='description')
    pub_url = models.URLField(help_text='if published, link to publication', blank=True, verbose_name='publication url')
    data_url = models.URLField(help_text='if data is published, link to data repository entry', blank=True)
    aspects = models.ManyToManyField(Aspect, verbose_name='aspects')

    def n_samples(self):
        return len(self.samples.all())

    def __str__(self):
        return self.title


class ExperimentMetaFile(models.Model):
    """
    Files attached to an experiment.
    """
    attached_to = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='meta_files')
    upload_time = models.DateField(auto_now=True)
    file = models.FileField(storage=fss, upload_to='meta/experiment/')
    desc = models.TextField(max_length=2000, verbose_name='description', blank=True)


class Sample(models.Model):
    """
    A single biological sample, i.e. a collection of cells that underwent exactly the same treatment until harvesting
    for downstream analysis.
    """
    exp = models.ForeignKey(Experiment, on_delete=models.PROTECT, verbose_name='experiment', related_name='samples')
    comment = models.TextField(max_length=2000, blank=True)
    genotype = models.ForeignKey(Genotype, on_delete=models.PROTECT, related_name='samples')

    def __str__(self):
        return '%s: %s' % (str(self.experiment), str(id(self)))


class AspectValue(models.Model):
    """
    A value of a sample in an experimental dimension.
    """
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE, related_name='dim_values')
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name='dim_vals')
    string_value = models.CharField(max_length=100, verbose_name='value')

    def __str__(self):
        return self.string_value

    def _value(self):
        if self.var.type == Aspect.INT:
            return int(self._value)
        elif self.var.type == Aspect.FLT:
            return float(self._value)
        elif self.var.type == Aspect.STR:
            return self._value
        else: raise TypeError('Unknown dimension type')