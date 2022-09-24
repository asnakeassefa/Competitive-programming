class Solution:
    def sortSentence(self, s: str) -> str:
        word = s.split(' ')

        for i in range(len(word)):
            for j in range(len(word)):
                if(word[i][-1:] > word[j][-1:]):
                    temp = word[i]
                    word[i] = word[j]
                    word[j] = temp
            word[i] = word[i][:-1]
        a = ""
        for x in range(len(word)):
            if a == "":
                a = word[x]
            else:
                a = a + " " + word[x]

        return a
        