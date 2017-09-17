sample = ['GTA','GGG','CAC']

def read_dna(dna_file):
  dna_data = ""
  with open(dna_file,"r") as f:
    for line in f:
      dna_data += line
  return dna_data

def dna_codons(dna):
  codons = []
  for pair in range(0,len(dna),3):
    codons.append(dna[pair:pair+3])
  return codons

def match_dna(dna):
  matches = 0
  for codon in dna:
    if codon in sample:
      matches += 1
  return matches

def is_criminal(dna_sample):
  dna_data = read_dna(dna_sample)
  num_matches = match_dna(dna_codons(dna_data))
  if(num_matches >= 3):
    print "Matches: %d\nThe investigation will continue." % (num_matches)
  else:
      print "Matches: %d\nThe suspect is not guilty." % (num_matches)
      
      
is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
    