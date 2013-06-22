def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''

    return len(dna)

def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''

    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    
    return dna2 in dna1

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence dna is valid
    (that is, it contains only nucleotide characters: 'A', 'T', 'C' and 'G')

    >>> is_valid_sequence('ATCGA')
    True
    >>> is_valid_sequence('atcga')
    False
    >>> is_valid_sequence('DNA')
    False

    '''

    valid_sequence = True

    for char in dna:
        if char not in 'ATCG':
            valid_sequence = False

    return valid_sequence

def insert_sequence(dna1,dna2,index):
    '''(str, str, int) -> str

    Returns a string where dna2 is inserted in dna1 at the point specified in
    index.

    >>> insert_sequence('CCGG','AT',2)
    CCATGG
    >>> insert_sequence('CCAA','TAC',0)
    TACCCAA
    >>> insert_sequence('ATCG','GTCA',4)
    ATCGGTCA
    '''

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    ''' (str) -> str

    Returns the complement of the entered nucleotide.
    nucleotide must be a valid nucleotide ('A','T','C' or 'G')

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
    '''

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return 'Invalid nucleotide'

def get_complementary_sequence(dna):
    '''(str) -> str

    Returns the complementary sequence of dna.
    dna must be a valid sequence

    >>> get_complementary_sequence('TA')
    AT
    >>> get_complementary_sequence('GGATCC')
    CCTAGG
    '''

    complementary_dna = ''
    for char in dna:
        complementary_dna = complementary_dna + get_complement(char)

    return complementary_dna
