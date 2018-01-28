


def base_count(string):
    possible_bases = 'ACGT'
    cnt = []
    for i in 'ACGT':
        cnt.append(string.count(i))
    
    return cnt


def main():
    seq = 'GCTCAAATTTGCGGTTGCTCGGATTTGAGACCCCGTAGCGCAGTACCTCGCTGAATCTTGCACCGCAGTCTACGTAGCCTCTCTCGTAAAGAGTGAATACCACAATGATAACGAGGAGTCACGAGGAGCCACTGAGGGCAATGTATATCCTCCGCGGAACACAGGAGTACCTAGTAAATCGAGTACTAAGGTGCGCCCACTTGTTCTTTTTCATCGAGTGTTACAAAACCATTCATCCTACTTGGGTCGTGTAATGGAAGCCCCCAAACGGCGGTTTCATAAGCAGCAGAACGGAGTCTTACCGGGCGAACTCTCGACTGATCGCGCACCATCCCACTTGAGAGATGGACAGCCAGAACATAGTGTTCAAACTTCGTATCTAATTGGCATAAACTTACGTAGACAACCCCCCACGTGACCCGAGATCAAAGCTGAAAGTTCTTCGGCTGATACCAGTAGCTCGTATGTTCGATGACCCGGAATCGTAGCATTCTAAGCATAGTATTATAAGTAATGTCGACACCGATGCAGGAGTCGGCTCACACCAGCTGTCTAGTAGGCGCAGGGCGATAAGTTAGGGCAGAGATGGGCTGTCTCGAGAATTCAGTCCCGCAGTGCCATCCTTTTGTATCCCATGGGTAGAAGAATCTGTTCAGCAGGTCGGTAGTTTCATCGGGAAACCATTCGCAAAGATTCGGAATGGGTGGTTAGACGGACAGGTAGGGAATACAGCCGGTAGGCGTATCGTCTCCGTCGCTTCGAATGGGGCTGTGCCTTAGCGGAATTCCTGAATGCTGCTTCCATTCGATGCCGCCCAATAAACTAATTACACACAATGAAACAAGCAACACGCTATCTAAGAACAAATCAGAACCTGTCACGATGAAACCATACCCACAC'
    cnt_arr = base_count(seq)
    
    for i in cnt_arr:
        print(i)
        
if __name__ == '__main__':
    main()