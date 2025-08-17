class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def marge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i , j , k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i +=1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while j < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
                
                
        
        def margeSort(arr, l, r):
            if l == r:
                return arr

            m = (r+l) // 2
            margeSort(arr, l, m)
            margeSort(arr, m+1, r)
            marge(arr, l, m, r)
            return arr
        
        return margeSort(nums, 0, len(nums) - 1)