import PyPluMA

COMPLEMENT = dict()
COMPLEMENT['A'] = 'T'
COMPLEMENT['T'] = 'A'
COMPLEMENT['C'] = 'G'
COMPLEMENT['G'] = 'C'


class ORFPlugin:
   def input(self, filename):
      paramfile = open(filename, 'r')
      self.parameters = dict()
      for line in paramfile:
          contents = line.strip().split('\t')
          self.parameters[contents[0]] = contents[1]
      completegenome = open(PyPluMA.prefix()+"/"+self.parameters["complete"], 'r')
      csvfile = open(PyPluMA.prefix() + "/" + self.parameters["csvfile"])
      threshold = int(self.parameters["threshold"])
      completegenome.readline() # header
      self.DNA = ''
      for line in completegenome:
          self.DNA += line.strip()
      header = csvfile.readline().strip()
      headercontents = header.split(',')
      start_idx = headercontents.index("start")
      readingFrame_idx = headercontents.index("readingFrame")
      plusMinus_idx = headercontents.index("+/-")
      self.regions = []
      for line in csvfile:
          contents = line.strip().split(',')
          readingFrame = int(contents[readingFrame_idx])
          if (readingFrame >= threshold):
             start = int(contents[start_idx])
             startspot = start - readingFrame + 1
             endspot = start-1
             plusMinus = contents[plusMinus_idx]
             self.regions.append((plusMinus, startspot-1, endspot-1))

   def run(self):
       self.sequences = []
       for indices in self.regions:
           sequence = self.DNA[indices[1]:indices[2]]
           if (indices[0] == "+"):
              self.sequences.append(sequence)
           else:
               # Reverse comp
               revcomp_seq = ''
               for i in range(len(sequence)):
                   revcomp_seq += COMPLEMENT[sequence[i]]
               revcomp_seq = revcomp_seq[::-1]
               self.sequences.append(revcomp_seq)

   def output(self, filename):
       outfile = open(filename, 'w')
       for i in range(len(self.sequences)):
          outfile.write(">openReadingFrame "+str(i)+"\n")
          outfile.write(self.sequences[i]+"\n")
