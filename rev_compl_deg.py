

def rev_compl(seq):
    BASES ='NACRWMBDHVKSYGT'
    return ''.join([BASES[-j] for j in [BASES.find(i) for i in seq.replace('-','')][::-1]])

if __name__ == '__main__':
    inseq = input('sequence: ')
    print(rev_compl(inseq.upper()))
