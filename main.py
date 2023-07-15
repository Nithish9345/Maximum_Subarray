
class Maximum:
    def Maximum_Subarray(self, array, B):
        result = 0
        present_sum = 0
        j = 0

        for i in range(len(array)):
            present_sum += array[i]
            while present_sum > B:
                present_sum -= array[j]
                j += 1
            result = max(present_sum, result)
        return result



A, B = map(int, input().split())
array = list(map(int, input().split()))
print(Maximum().Maximum_Subarray(array, B))
