def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    nuc_count = 0
    for char in dna:
        if char == nucleotide:
            nuc_count = nuc_count + 1
            
    return nuc_count

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    
    return dna1.find(dna2) != -1

def is_valid_sequence(dna):
    '''(str) -> bool
    
    Return True if and only if DNA sequence in 
    dna is a valid sequence, containing only A,
    T, C, and G.
    
    >>>is_valid_sequence("ATACTGA")
    True
    >>>is_valid_sequence("AcTGAT")
    False
    '''
    
    isValid = True
    valid_val = 'ATCG'
    
    for char in dna:
        if not char in valid_val:
            isValid = False
            
    return isValid


def insert_sequence(dna1, dna2, loc):
    '''(str, str, int) -> str
    
    Returns a str with DNA sequence dna2 inserted 
    at the index loc in DNA sequence dna1.
    
    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>>insert_sequence('CTGA', 'GAT', 0)
    'GATCTGA'
    '''
    
    new_sequence = dna1[:loc] + dna2 + dna1[loc:]
    return new_sequence

def get_complement(nucleotide):
    '''(str) -> str
    
    Return the complementary nucleotide to the
    nucleotide inputted.
    
    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    'G'
    '''
    
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'C'

    
def get_complementary_sequence(dna):
    '''(str) -> str
    
    Return the complementary DNA sequence to
    the DNA sequence inputted.
    
    >>>get_complementary_sequence('AT')
    'TA'
    >>>get_complementary_sequence('TCTAG')
    'AGATC'
    '''
    
    comp_sequence = ''
    for char in dna:
        comp_sequence = comp_sequence + get_complement(char)
    
    return comp_sequence
