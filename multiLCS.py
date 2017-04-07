#Recursive Solution Top-Down with Dynamic Programming
def main(string):
    DNA = {}
    B = ''
    def Long_CS(first_string, second_string, n, m, b):
        #import pdb; pdb.set_trace()
        if (n, m) in DNA:
            value, b = DNA[(n, m)]
            #print('1', b)
            return [value, b]
        if n == 0 or m == 0:
            value = 0
            DNA[(n, m)] = value, ''
            #print('2', b)
            return [value, '']
        elif first_string[n-1] == second_string[m-1]:
            #c = b
            c = first_string[n-1]
            b = c
            #print('3.5', c)
            value = 1 + Long_CS (first_string, second_string, n-1, m-1, c)[0]
            b += Long_CS (first_string, second_string, n-1, m-1, c)[1]
            #print('3.8', b)
   
            #print('3',b)
            DNA[(n, m)] = value, b
            return [value, b]
        elif first_string[n-1] != second_string[m-1]:
            ad = b
            recursive1, st1 = Long_CS(first_string, second_string, n-1, m, ad)
            da = b
            recursive2, st2 = Long_CS(first_string, second_string, n, m-1, da)
            value = max({recursive1, recursive2})
            if recursive1 > recursive2:
                b = st1
            else:
                b = st2
            DNA[(n, m)] = value, b
            return [value, b]
        return [value, b]
    if len(string) < 2:
        print('Number of DNA sequences is less than 2! Please recheck.\n')
        raise KeyError
    else:
        Result = Long_CS(string[0], string[1], len(string[0]), len(string[1]), B)
        Common_seq = Result[1][::-1] #reversing it since sequence is written backwards
        
        for indx in range(2, len(string)):
            DNA = {}
            B = ''
            Result = Long_CS(Common_seq, string[indx], len(Common_seq), len(string[indx]), B)
            Common_seq = Result[1][::-1] #reversing it
        print('The length of the longest common sequence for all DNA sequences is', Result[0], '\n')
        print('The longest common subsequence is:\n', Common_seq)
        return

            
strings = {0: 'TTCTACGGGGGGAGACCTTTACGAATCACACCGGTCTTCTTTGTTCTAGCCGCTCTTTTTCATCAGTTGCAGCTAGTGCATAATTGCTCACAAACGTATC', \
           1: 'TCTACGGGGGGCGTCATTACGGAATCCACACAGGTCGTTATGTTCATCTGTCTCTTTTCACAGTTGCGGCTTGTGCATAATGCTCACGAACGTATC', \
           2: 'TCTACGGGGGGCGTCTATTACGTCGCCAACAGGTCGTATGTTCATTGTCATCATTTTCATAGTTGCGGCCTGTGCGTGCTTACGAACGTATTCC', \
           3: 'TCCTAACGGGTAGTGTCATACGGAATCGACACGAGGTCGTATCTTCAATTGTCTCTTCACAGTTGCGGCTGTCCATAAACGCGTCCCGAACGTTATG', \
           4: 'TATCAGTAGGGCATACTTGTACGACATTCCCCGGATAGCCACTTTTTTCCTACCCGTCTCTTTTTCTGACCCGTTCCAGCTGATAAGTCTGATGACTC', \
           5: 'TAATCTATAGCATACTTTACGAACTACCCCGGTCCACGTTTTTCCTCGTCTTCTTTCGCTCGATAGCCATGGTAACTTCTACAAAGTTC', \
           6: 'TATCATAGGGCATACTTTTACGAACTCCCCGGTGCACTTTTTTCCTACCGCTCTTTTTCGACTCGTTGCAGCCATGATAACTGCTACAAACTTC'}

main(strings)
