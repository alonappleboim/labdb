This project is a web-based application to manage all lab data.

The primary entities are:
 - Experiment - A single experiment performed by a someone at some date. It is easiest for us to refer to these units
                of work, and hence they are the basic data context in the system. An experiment is further elaborated
                by its experiment dimesnions, that are under evaluation in the experimental context. For example,
                a single experiment might compare different genotypes in otherwise the same conditions, so the
                experimental dimension would by "genotype". A different experiment might compare different genotypes
                in different optical density levels, so the experiment dimensions would be both "genotype" and "OD".

 - Genotype - A single well-defined and complete genotype. Note that a genotype can be a combinatorial mixture of
              genotypes, e.g. gRNA(X):His3+gRNA(Y):Leu2

 - Sample - Within an experiment, a sample is defined as a single instantiation of all the controlled variables. e.g. in
            an experiment with two repeats, five time points, and two initial conditions, there will be 2x5x2 samples,
            each with a specific value combination of the controlled variables of the experiment. A sample is a
            biological entity.

 - Assay - An assay is a process that takes a sample, and produces data from it, possibly with modifiable
           steps. For example, a single example can undergo a MNase-ChIP-seq protocol, but the protocol can
           include an incubation with X amount of MNase, or a 10X amount of MNase, similarly, the IP can be
           performed with Ab X or Ab Y, or with twice as much Ab X. The same sample can also undergo other assays, e.g.
           OD measurement, or 3'-RNA-seq. Each assay is associated with its respective data type. The most common data
           type is a fastq output, but growth curves, FACS distributions, microscope images, colony images, etc.
           are other types of possible outputs.

 - RawData - When an assay is applied to a sample, the result is a raw data entry. Thus, wrapping the actual data, it
             also contains all the metadata assoicated with the data, derived from the assoicated sample and the
             associated assay.

 - User - Someone in the lab.


%% next versions will include
 - External data, that will be assoicated with external experiments, etc.

 - Genotype parsing - a precise formal language to write a genotype, used to parse it into meaningful fields in the DB.

 - Datatypes - Each data (raw or processed) will be associated with a specific format; well-known ones like fastq, bam,
               tiff, etc. and new ones, like centers-lengths (for v-plots), and others. Each datatype is associated with
               relevant metadata (e.g. bam includes genome used for mapping).

 - Transformer - A batch of code that converts one type of data raw or analyzed data to produce another kind (or several kinds) of
                 analyzed data. e.g. a pipeline that maps reads to transcripts and reports

 - Exporter - Given a collection of data entries with similar characterisitics, exports them in a pre-spcified format.
              e.g. given a collection of BAM files, and annotations, outputs a CSV of how many reads were mapped within
              a +/- 200 bp of annotations in each of the BAM files.

 - Annotations - genes, TSSs, nucleosome positions,



 %% appendix - what kinds of assays/data do we expect to see in the db?
 - mnase
 - chip
 - co-chip
 - 3' rna
 - 5' rna
 - nascent rna (4sU/netseq)
 - ribosome profiling
 - genome sequencing (mutation analysis)
 - FACS
 - OD / growth curves
 - microscopy images
 - colony images
 - massively parallel reporter assays with (m)any of the above as readout