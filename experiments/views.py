import csv
import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from models import *
from .forms import *

def validate_file(file, exp):
    """
    First pass on file - if header is wrong, parsing halts and only an error list is returned. If header is ok, a
    complete parsing is executed, and a all info/errors are returned, together with parsed sample information.

    :param request: the original http request
    :param exp: experiment associated with the samples contained in the parsed file
    :return: errors: a list of general errors
             serrs: a list of errors per sample
             info: a list of info strings
             sinfo: a list of info strings per sample
             samples: a list of parsed samples (dicts)
             gtypes: a list of genotypes to be added automatically
    """
    rdr = csv.DictReader(file, dialect='excel-tab')
    errors, info, serrs, samples, gtypes = [], [], [], [], []
    if 'genotype' not in rdr.fieldnames:
        errors.append("header doesn't have a 'genotype' field")
    if 'protocol' not in rdr.fieldnames:
        errors.append("header doesn't have a 'protocol' field")
    if 'fastq-path' not in rdr.fieldnames:
        errors.append("header doesn't have a 'fastq-path' field")
    for v in exp.variables.all():
        v_fn = str(v)
        if v_fn not in rdr.fieldnames:
            errors.append("header doesn't have a '%s' field" % v_fn)
    if errors:
        return errors, info, serrs, samples

    # header is ok
    uvals = {v: set([]) for v in exp.variables.all()}
    for si, sline in enumerate(rdr):
        serr = []
        samples.append(sline)
        try:
            g = Genotype.objects.get(string=sline['genotype'])
        except ObjectDoesNotExist:
            try:
                gtypes.append(sline['genotype'], sline['genotype-string'])
                info(
                    'Added a new genotyope "%s". Please add any additional metadata directly to it.' % g.short_name)
            except KeyError:
                serr.append('A new genotype, "%s", was detected. If you want to add it automatically, '
                            'please add a column "genotype-string" and enter a string that describes the genotype '
                            'in the sample where it appears first.' % sline['genotype'])
        try:
            p = Protocol.objects.get(short_name=sline['protocol'])
        except ObjectDoesNotExist:
            serr.append('A new protocol, "%s", was detected. Please add the new protocol to the system '
                        ' and retry.' % sline['protocol'])
        if not os.access(sline['fastq-path'], os.R_OK):
            serr.append('Could not access fastq file in path: %s, verify that the file has group read permissions '
                        'chmod g+r <filepath>, or chmod -R g+r <directory>.' % sline['fastq-path'])
        for v in exp.variables.all():
            uvals[v].add(sline[str(v)])
            try:
                if v.type == v.INT:
                    int(sline[str(v)])
                elif v.type == v.FLT:
                    float(sline[str(v)])
            except ValueError:
                k = (v, v.type, sline[str(v)])
                serr.append(
                    'type mismatch for variable %s. Type is %s, but given value, %s, could not be cast. ' % k)
        serrs.append(serr)

    info.append('File had a total of %i samples.' % len(samples))
    for var, vals in uvals.iteritems():
        k = (var, len(vals), ','.join(vals))
        info.append('variable %s has %i unique values: (%s)' % k)

    return errors, info, serrs, samples, gtypes

def add_all(samples, genotypes):
    pass

def parse_samples_and_report(request, expid):
    exp = Experiment.objects.get(pk=expid)
    errs, info, serrs, samples, gtypes = validate_file(request.FILES['samples_file'], exp)
    zippeds = zip(samples, serrs)
    context = dict(errs=errs, info=info, samples=zippeds)
    if errs or any(serrs):
        print
        zippeds
        print
        'XXXX'
        print
        serrs
        return render(request, 'genomics/upload_samples_errors.html', context)
    else:
        add_all(samples, gtypes)
        return render(request, 'genomics/upload_samples_report.html', context)

def upload_samples(request, expid):
    exp = Experiment.objects.get(pk=expid)
    form = UploadSamplesForm(request.POST, request.FILES)
    return render(request, 'genomics/upload_samples.html', {'form': form, 'exp': exp})

def resp(request):
    return HttpResponse('this is a response')