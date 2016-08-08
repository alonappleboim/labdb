from __future__ import unicode_literals

from django.db import models
from experiments.models import Sample
from labdb.settings import fss
from django.contrib.auth.models import User


"""
this file will contain scripts that convert between data types
and pipelines and pipegrids that execute multiple consecutive and parallel such conversions.

"""