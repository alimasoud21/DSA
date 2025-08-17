class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def counting_sort(arr):
            count = defaultdict(int)
            min_value, max_value = min(arr), max(arr)

            for value in arr:
                count[value] += 1
    
            index = 0
    
            for value in range(min_value, max_value + 1):
                while count[value] > 0:
                    arr[index] = value
                    index += 1
                    count[value] -= 1
    
            return arr

        return(counting_sort(nums))