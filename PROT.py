# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:24:06 2021
"""

RNA = "RNA.txt"

def RNAtoPROT(RNA): 
    codon_chart = {
        'F': ['UUU', 'UUC'],
        'L' : ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
        'I' : ['AUU','AUC','AUA'],
        'M' : ['AUG'],
        'V' : ['GUU', 'GUC', 'GUA', 'GUG'],
        'S' : ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
        'P' : ['CCU', 'CCC', 'CCA', 'CCG'],
        'T' : ['ACU', 'ACC', 'ACA', 'ACG'],
        'A' : ['GCU', 'GCC', 'GCA', 'GCG'],
        'Y' : ['UAU', 'UAC'],
        'H' : ['CAU', 'CAC'],
        'Q' : ['CAA', 'CAG'],
        'N' : ['AAU', 'AAC'],
        'K' : ['AAA', 'AAG'],
        'D' : ['GAU', 'GAC'],
        'E' : ['GAA', 'GAG'],
        'C' : ['UGU', 'UGC'],
        'W' : ['UGG'],
        'R' : ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
        'G' : ['GGU', 'GGC', 'GGA', 'GGG'],
        'STOP' : ['UAA', 'UAG', 'UGA']
        }
    
    
   
    with open(RNA) as f:
        
        RNA_listed = f.readline().strip()
        stopping_point = len(RNA_listed)
        starting_point = RNA_listed.find('AUG')
        #This function will run in a loop until a stop codon is found or the sequence is depleted
        def loop_from_starting_pnt(starting_point, stopping_point):
            output_array = []
            #indicates all codons have been exhausted
            if starting_point == -1:
                return output_array
            else:
                output_aa = ''
                #n represents the position (as an integer) where the next triplet is
                for n in range(starting_point, len(RNA_listed), 3):
                    for aa in codon_chart:
                        for codon in codon_chart[aa]:
                            if RNA_listed[n:n+3] in codon:
                                if aa == 'STOP':
                                    #Updates starting and stopping points
                                    starting_point = RNA_listed.find('AUG', n)
                                    output_array.append(output_aa)
                                    output_aa = ''
                                    if n > (stopping_point - 3):
                                        loop_from_starting_pnt(starting_point, stopping_point)
                                else:
                                    output_aa += aa

            return output_array
            
    output_array = loop_from_starting_pnt(starting_point, stopping_point)
    return output_array     
    f.close()

############# MAIN FX ###############
def main():
    prot_translation = (RNAtoPROT(RNA))
    i = 1
    print(prot_translation)
    user_input = input("Found %s amino acid sequences. Write output to FASTA file? Type Y or N \n" % (len(prot_translation)))
    #Here the sequences can be written into a file
    if user_input == "Y" or "y":
        with open("Output.fasta", 'w') as fileoutput:
            for aa_sequence in prot_translation:
                fileoutput.write(">Protein%i\n%s\n" % (i, aa_sequence))
                i += 1
               
    elif user_input == "N" or "n":
        return
        
    fileoutput.close()
    
if __name__ == "__main__":
    main()    
   
       