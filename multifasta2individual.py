import argparse
import re
import tqdm
import sys
import subprocess
from Bio import SeqIO
import textwrap

parser = argparse.ArgumentParser(prog='python multifasta2individual.py',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent('''\

# multifasta2individual

Author: Murat Buyukyoruk

        multifasta2individual help:

This script is developed to generate individual fasta files for the sequences in a multifasta file.

SeqIO package from Bio is required to fetch flank sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.
        
Syntax:

        python multifasta2individual.py -i demo.fasta

multifasta2individual dependencies:

Bio module and SeqIO available in this package          refer to https://biopython.org/wiki/Download

tqdm                                                    refer to https://pypi.org/project/tqdm/
	
Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.
	
      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename', help='Specify a fastafile.\n')

results = parser.parse_args()
filename = results.filename

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Splitting...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        acc = record.id

        out = filename.split(".fasta")[0] + "_" + acc + ".fasta"
        f = open(out, 'a')
        sys.stdout = f

        x = record.seq
        chunks, chunk_size = len(x), 1000000
        x_chunks = [x[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for i in range(len(x_chunks)):
            print(">" + record.id + "_" + str(i) + " | " + record.description)
            print(re.sub("(.{60})", "\\1\n", str(x_chunks[i]), 0, re.DOTALL))

