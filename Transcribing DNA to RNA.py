# -*- coding: utf-8 -*-
"""
Identifies and strips FASTA DNA file for conversion into RNA.
RNA output is a text file (no heading)so it can be easily
passed on to the translation script.
"""    
file = 'rosalind_rna.txt' 

def main():
    with open(file, 'r') as f:
        
        DNA = []
        for line in f:
            fasta_condition = line.startswith(">")
            if fasta_condition == False:
                try:
                    DNA.append(line.strip('\n'))
                except StopIteration:
                    break
 
    DNA_combined = ''.join(DNA)
    RNA = DNA_combined.replace('T', 'U')
    with open("RNA.txt", 'w') as output:
       output.write(RNA)
       

if __name__ == "__main__":
    main()
