

class PlagiatScanner():

    def __init__(self, code1 = None, code2 = None):
        self.code1 = code1
        self.code2 = code2

    def compute_Levenshtein_distance(self):
        len1, len2 = len(self.code1), len(self.code2)
        if len1 > len2:
            self.code1, self.code2 = self.code2, self.code1
            len1, len2 = len2, len1

        current_row = range(len1 + 1)
        for i in range(1, len2 + 1):
            previous_row, current_row = current_row, [i] + [0] * len1
            for j in range(1, len1 + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if self.code1[j - 1] != self.code2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[len1]
