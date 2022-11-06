#!/usr/bin/python3
#Program written by s2268606 on 21/10/22. DNA manipulation.

##Q1
#Finding AT count
short_seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_count= short_seq.count('A')
T_count= short_seq.count('T')
AT_content=((A_count + T_count)/len(short_seq))*100
print(f"1.The number of As is {A_count}, the number of Ts is {T_count}, the A/T content of the seqeunce is {round(AT_content,2)}%")

##Q2
#Finding complementary sequence
seq_for_comp="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
seq_for_comp=seq_for_comp.replace('A','t')
seq_for_comp=seq_for_comp.replace('T','a')
seq_for_comp=seq_for_comp.replace('C','g')
seq_for_comp=seq_for_comp.replace('G','c')
comp_DNA=seq_for_comp.upper()
print(f"2.The complementary seqquence is {comp_DNA}")

##Q3
restr_frag="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
#Find position of motif
cut_pos=restr_frag.find("GAATTC")
print(f"3.1. The position of the motif is {cut_pos}-{(cut_pos)+5} (python index, 'real' position is {cut_pos+1}-{cut_pos+6})")

#Use position to find cut position
print(f"3.2. The positon of the cut site is after G at position { cut_pos}")

#Find length of second fragement
second_frag=restr_frag[22:]
length_sec_frag=len(second_frag)
print(f"3.3. The length of the second fragement '({second_frag})' is {length_sec_frag} bases")

##Q4
genomic_DNA="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1_coord=":63"
exon_2_coord="90:"
#Extract exons
exon_1=genomic_DNA[:63]
exon_2=genomic_DNA[90:]
#Join exons for coding sequence
coding_seq=exon_1+exon_2
print(f"4.1.1 The first exon is {exon_1}\nThe second exon is {exon_2}")
print(f"4.1.2 The coding sequence is {coding_seq}")

#% of DNA sequence that is coding

