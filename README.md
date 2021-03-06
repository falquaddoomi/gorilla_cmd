# Simple GOrilla command-line interface

Query the GOrilla service from the command line and receive results in Excel format.

Usage: ./gorilla_cmd.py [-s SPECIES] [-o OUTFILE] genefile

**genefile**: a file containing newline-delimited genes. Consult the sample.txt file for an example.

*-b*: an optional background set to use with the query; by default no background set is used.

*-s*: the species over which to perform the query, from the following options:

* ARABIDOPSIS_THALIANA
* SACCHAROMYCES_CEREVISIAE
* CAENORHABDITIS_ELEGANS
* DROSOPHILA_MELANOGASTER
* DANIO_RERIO
* HOMO_SAPIENS
* MUS_MUSCULUS
* RATTUS_NORVEGICUS

Defaults to 'HOMO_SAPIENS' if unspecified.

*-o*: the filename to which to write the Excel data. The target filename should be specified with the extension, e.g. "myfile.xls".

Dumps the excel data to stdout if no filename is specified.

*-v*: runs the script in verbose mode, which outputs some debugging information to stderr.

*-u*: emits the results URL.

If -o is not specified, the URL is appended to stdout. If -o is specified, the URL is written to a new file with the same path and name as the outfile, but with a .url extension.

*(NOTE: this script relies on the argparse module introduced in Python 2.7. If you're running a previous version of Python, you can install the argparse module via pip/wheel.)*
