from itertools import count


class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence

    def __len__(self):
        words = self.sentence.split()
        return len(words)


v1 = Sentence("Waldek i    kamil")
print(len(v1))

