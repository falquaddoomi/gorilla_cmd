# Simple GOrilla command-line interface

Query the GOrilla service from the command line and receive results in Excel format.

Usage: ./gorilla_cmd.py [-s SPECIES] [-o OUTFILE] genefile

**genefile**: a file containing newline-delimited genes. Consult the sample.txt file for an example.

*-s*: the species over which to perform the query, from the following options:

* ARABIDOPSIS_THALIANA
* SACCHAROMYCES_CEREVISIAE
* CAENORHABDITIS_ELEGANS
* DROSOPHILA_MELANOGASTER
* DANIO_RERIO
* HOMO_SAPIENS
* MUS_MUSCULUS
* RATTUS_NORVEGICUS

defaults to 'HOMO_SAPIENS' if unspecified.

*-o*: the filename to which to write the Excel data. The target filename should be specified with the extension, e.g. "myfile.xls".

Dumps the excel data to stdout if no filename is specified.
