class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        res = 0

        for i in range(len(operations)):
            if operations[i] == "C":
                score.pop(-1)
            elif operations[i] == "D":
                score.append(score[-1] * 2)

            elif operations[i] == "+":
                score.append(score[-2] + score[-1])
            else:
                score.append(int(operations[i]))

        print(score)
        for i in range(len(score)):
            res = res + int(score[i])
        return res