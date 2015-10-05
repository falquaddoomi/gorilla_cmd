#!/usr/bin/env python

import requests
import argparse, re, shutil, time

FORM_URL = """http://cbl-gorilla.cs.technion.ac.il/servlet/GOrilla"""
EXCEL_URL = """http://cbl-gorilla.cs.technion.ac.il/GOrilla/%s/GO.xls"""

SPECIES = [
	"ARABIDOPSIS_THALIANA",
	"SACCHAROMYCES_CEREVISIAE",
	"CAENORHABDITIS_ELEGANS",
	"DROSOPHILA_MELANOGASTERz",
	"DANIO_RERIO",
	"HOMO_SAPIENS",
	"MUS_MUSCULUS",
	"RATTUS_NORVEGICUS"
]

id_grabber = re.compile("id=([^&]+)")

class RequestFailedException(Exception):
	"""
	Raised when a POSTed job is rejected for some reason by GOrilla (i.e. the service returns a non-200 HTTP code)
	"""
	pass

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Sends a remote command to GOrilla returns results(?)')
	parser.add_argument('genefile', type=argparse.FileType('rb'), help='a file containing newline-delimited genes')
	parser.add_argument('-s', '--species', type=str, help='the species over which to perform the query', choices=SPECIES, default='HOMO_SAPIENS')
	parser.add_argument('-o', '--outfile', type=str, help='filename to which to write excel results, defaults to job_id.xls if not specified')

	args = parser.parse_args()

	data = {
		'application': 'gorilla',
		'species': args.species,
		'run_mode': 'mhg',
		'target_set': args.genefile.read(),
		'background_set': '',
		'db': 'proc',
		'run_gogo_button': 'Search Enriched GO terms',
		'pvalue_thresh': '0.001',
		'analysis_name': '',
		'user_email': '',
		'output_excel': 'on',
		'fast_mode': 'on',
	}

	try:
		print "* Sending request to GOrilla..."

		r = requests.post(FORM_URL, data=data)

		if r.status_code != 200:
			raise RequestFailedException("Request to GOrilla failed with code %s" % r.status_code)

		print "* Got GOrilla response, waiting for results to become available...",
		time.sleep(5)
		print "done, getting results"

		try:
			job_id = id_grabber.findall(r.url)[0]

			# use the job ID to perform a second request for the excel data
			response = requests.get(EXCEL_URL % job_id, stream=True)

			if response.status_code != 200:
				raise RequestFailedException("Request for excel file failed with code %s" % response.status_code)

			result_file = args.outfile if args.outfile else '%s.xls' % job_id

			print "* Saving excel results as '%s'..." % result_file
			with open(result_file, 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response

		except IndexError:
			print "ERROR: job ID not found in response URL"
	except RequestFailedException as ex:
		print "ERROR: %s" % ex.message