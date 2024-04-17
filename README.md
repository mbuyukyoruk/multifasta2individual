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
	
