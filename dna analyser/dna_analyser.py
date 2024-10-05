from Bio import SeqIO
import streamlit as st
from io import StringIO

def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    return (g + c) / len(sequence) * 100 if len(sequence) > 0 else 0

def analyze_sequence(seq):
    length = len(seq)
    gc = gc_content(seq)
    return length, gc

# Streamlit Interface
st.title("DNA Sequence Analyzer")
uploaded_file = st.file_uploader("Choose a FASTA file", type=["fasta", "fa"])

if uploaded_file is not None:
    # Read the content of the uploaded file
    string_data = uploaded_file.getvalue().decode("utf-8")  # Decode bytes to string
    
    # Use StringIO to treat the string data as a file-like object
    sequences = SeqIO.parse(StringIO(string_data), "fasta")

    for record in sequences:
        length, gc = analyze_sequence(str(record.seq))
        st.write(f"**Sequence ID:** {record.id}")
        st.write(f"**Length:** {length} nucleotides")
        st.write(f"**GC Content:** {gc:.2f}%")
        st.write(f"**Sequence:** {record.seq}")

