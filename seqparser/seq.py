# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    trans_seq = []
    for nuc in seq:
        if nuc in ALLOWED_NUC:
            trans_seq.append(TRANSCRIPTION_MAPPING[nuc])
        else:
            trans_seq.append(nuc)
    
    trans_seq_str = "".join(trans_seq)
    
    return trans_seq_str

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    trans_seq = []
    for nuc in seq:
        if nuc in ALLOWED_NUC:
            trans_seq.append(TRANSCRIPTION_MAPPING[nuc])
        else:
            trans_seq.append(nuc)
    
    trans_seq_str = "".join(trans_seq)
    rev_trans_seq_str = trans_seq_str[::-1] #reverse the string by slicing start to end in negative steps
    
    return rev_trans_seq_str