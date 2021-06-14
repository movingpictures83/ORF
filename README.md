# ORF
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: FASTA
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that returns nucleotides corresponding to open-reading frames (ORFs), given an assumed full genome and starting and ending indices of each gene.

The plugin accepts as input a TXT file of keyword-value pairs.  Keywords:
threshold: minimum length to count as an ORF
complete: (Assumed) complete genome, FASTA format
csvfile: Comma-separated value, assumed to contain a set of genes (rows), with three columns: start, end, and readingFrame

The plugin outputs nucleotides corresponding to ORFs in FASTA format 
