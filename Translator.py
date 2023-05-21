class Translator:
    def __init__(self):

        self.transcript = []
        self.width = None
        self.height = None
        #self.dictionary use if not just 0's 1's and 2

    def translate(self, MazeFile):
        file = open(MazeFile)
        script = file.readlines()
        for line in script:
            cut = []
            if line != "":
                for number in line.split(","):
                    cut.append(int(number))
                self.transcript.append(cut)
        self.width = len(self.transcript[0])
        self.height = len(self.transcript)
        return self

    
if __name__ == "__main__":
    translator = Translator()
    print(translator.transcript)