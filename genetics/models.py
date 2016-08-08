from django.db import models
from labdb.settings import fss
from django.contrib.auth.models import User
from django.contrib import admin

# @admin.register
class Genotype(models.Model):
    """
    A concise and complete description of the genetic background of biological samples. Note that it can also contain a
    multiplexed genotype (e.g. identical genotype but for a specific locus, that has a combinatorial insertion).
    """
    short_name = models.CharField(max_length=60)
    string = models.TextField(help_text='string describing the complete genotype unambiguously')
    created_by = models.ForeignKey(User, related_name='genotypes_added')

    def __str__(self):
        return self.short_name


# @admin.register
class GenotypeMetaFile(models.Model):
    """
    A file attached to a genotype.
    """
    attached_to = models.ForeignKey(Genotype, on_delete=models.CASCADE, related_name='meta_files')
    upload_time = models.DateField(auto_now=True)
    file = models.FileField(storage=fss, upload_to='meta/genotype/')
    desc = models.TextField(verbose_name='description', max_length=2000, blank=True)