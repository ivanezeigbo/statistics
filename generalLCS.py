#Recursive Solution Top-Down with Dynamic Programming
def main(string):
    DNA = {}
    def Long_CS(string, length):
        content = tuple(length[:])       
        if content in DNA:
            value = DNA[content]
            return value
        if 0 in content:
            #import pdb; pdb.set_trace()
            value = 0
            DNA[content] = value
            return value
        Same = True
        j = 0
        while j < (len(string) - 1):
            if Same == False:
                break
            k = 1
            while k < len(string):
                if Same == True:
                    if string[j][length[j]-1] != string[k][length[k]-1]:
                        Same = False
                        break
                else:
                    break
                k += 1
            j += 1
                    
        if Same == True:
            copy = length[:]
            for l in range(len(copy)):
                copy[l] -= 1
            value = 1 + Long_CS(string, copy)
            DNA[content] = value
            return value
        
        else:
            all_recurse = []
            for i in range(len(string)):
                other_copy = length[:]
                other_copy[i] -= 1
                recurse = Long_CS(string, other_copy)
                all_recurse.append(recurse)
            value = max(all_recurse)
            DNA[content] = value
            return value
        return value

    if len(string) < 2:
        print("Number of DNA sequences provided is less than two! \n")
        raise KeyError
    else:
        length = []
        for h in range(len(string)):
            length.append(len(string[h]))
        
        return Long_CS(string, length)
        
     

strings = {0: 'TTCTACGGGGGGAGACCTTTACGAATCACACCGGTCTTCTTTGTTCTAGCCGCTCTTTTTCATCAGTTGCAGCTAGTGCATAATTGCTCACAAACGTATC', \
           1: 'TCTACGGGGGGCGTCATTACGGAATCCACACAGGTCGTTATGTTCATCTGTCTCTTTTCACAGTTGCGGCTTGTGCATAATGCTCACGAACGTATC', \
           2: 'TCTACGGGGGGCGTCTATTACGTCGCCAACAGGTCGTATGTTCATTGTCATCATTTTCATAGTTGCGGCCTGTGCGTGCTTACGAACGTATTCC', \
           3: 'TCCTAACGGGTAGTGTCATACGGAATCGACACGAGGTCGTATCTTCAATTGTCTCTTCACAGTTGCGGCTGTCCATAAACGCGTCCCGAACGTTATG', \
           4: 'TATCAGTAGGGCATACTTGTACGACATTCCCCGGATAGCCACTTTTTTCCTACCCGTCTCTTTTTCTGACCCGTTCCAGCTGATAAGTCTGATGACTC', \
           5: 'TAATCTATAGCATACTTTACGAACTACCCCGGTCCACGTTTTTCCTCGTCTTCTTTCGCTCGATAGCCATGGTAACTTCTACAAAGTTC', \
           6: 'TATCATAGGGCATACTTTTACGAACTCCCCGGTGCACTTTTTTCCTACCGCTCTTTTTCGACTCGTTGCAGCCATGATAACTGCTACAAACTTC'}

print("The longest common sequence for all sequences is", main(strings))  
