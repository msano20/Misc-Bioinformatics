# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:35:20 2021
Essentially this script reads and parses multiple fasta files 
before calculating GC percentage and assigning those values and
associated fasta IDs into a new dictionary. It will return the 
ID with the highest GC content.
"""

file = "string.fasta"


def GCcount():
    #parsing the fasta
    with open(file,'r') as string:
        headers = {} #header & sequence inserted into dict
        key = ''
        line_seq = ''
        #this line-by-line loop sets the header name as the key
        #sequences are then appended to a list before added as a dict value
        for line in string.readlines():
            if line.startswith('>'):
                key = line.strip('>\n')
                line_seq = ''
            elif line == '\n':
                pass
            else:
                line_seq+=str(line.strip())
            headers[key] = line_seq

    gc_list= {}
    
    for item, value in headers.items():
       gc_dict = {} #overwritten with every loop
       total = len(value)
       gc_count = ((value.count("G")) + value.count("C")) / float(total)
       gc_percent = float(gc_count * 100)
       rounded = (round(gc_percent, 6))
       gc_dict[item] = rounded
       gc_list.update(gc_dict)
       
    desc_list = (dict(sorted(gc_list.items(), key = lambda item: item[1], reverse = True)))
    return desc_list
    #print(max(gc_list, key = gc_list.get)) #if you want the highest gc% only
    headers.clear()
    gc_list.clear()

        
                
def main():
    desc_list = GCcount()
    print(desc_list)

   
if __name__ == "__main__":
    main()

