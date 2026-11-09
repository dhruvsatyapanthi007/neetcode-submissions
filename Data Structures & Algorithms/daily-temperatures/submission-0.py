class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i in range(0, n):
            temperature = temperatures[i]
            while stack and stack[-1][0] < temperature:
                colderTemperature, colderTemperatureIndex = stack.pop()
                res[colderTemperatureIndex] = i - colderTemperatureIndex
            stack.append((temperature, i))
        
        return res
        