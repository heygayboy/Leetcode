class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        answer = []
        result = []
        self.compute(candidates, target, 0, answer, result)
        return result

    def compute(self, candidates, target, start, answer, result):
        if target == 0:
            temp = answer[:]
            result.append(temp)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if target > 0:
                answer.append(candidates[i])
                self.compute(candidates, target - candidates[i], i + 1, answer, result)
                answer.pop()
            else:
                return


can = [10,1,2,7,6,1,5]
tar = 8
Solution().combinationSum2(candidates= can, target= tar)