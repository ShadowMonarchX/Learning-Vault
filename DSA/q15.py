class Solution:
    # Bubble Sort: Time - O(n^2), Space - O(1)
    def bubbleSort(self, nums):
        n = len(nums) - 1
        for i in range(0, n):
            swapped = False
            for j in range(0, n - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums

    # Selection Sort: Time - O(n^2), Space - O(1)
    def selectionSort(self, nums1):
        n = len(nums1)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if nums1[j] < nums1[min_idx]:
                    min_idx = j
            nums1[i], nums1[min_idx] = nums1[min_idx], nums1[i]
        return nums1

    # Insertion Sort: Time - O(n^2), Space - O(1)
    def insertionSort(self, nums2):
        n = len(nums2)
        for i in range(1, n):
            key = nums2[i]
            j = i - 1
            while j >= 0 and nums2[j] > key:
                nums2[j + 1] = nums2[j]
                j -= 1
            nums2[j + 1] = key
        return nums2

    # Heap Sort: Time - O(n log n), Space - O(1)
    def heapSort(self, nums):
        def heapify(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums

    # Counting Sort: Time - O(n + k), Space - O(k) where k is the range of input
    def countingSort(self, nums):
        if not nums:
            return []

        max_val = max(nums)
        min_val = min(nums)
        range_of_elements = max_val - min_val + 1

        count = [0] * range_of_elements
        output = [0] * len(nums)

        for num in nums:
            count[num - min_val] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for num in reversed(nums):
            output[count[num - min_val] - 1] = num
            count[num - min_val] -= 1

        return output

# Input arrays
nums = [1, 3, 2, 5, 4, 7, 6]
nums1 = [1, 3, 2, 5, 4, 7, 6, 9, 10, 12, 11]
nums2 = [1, 3, 2, 5, 4, 7, 6, 9, 10, 12, 11, 17, 14, 15, 13]
nums3 = [4, 2, 2, 8, 3, 3, 1]
nums4 = [4, 2, 2, 8, 3, 3, 1]

solution = Solution()
sorted_nums = solution.bubbleSort(nums[:])
sorted_nums1 = solution.selectionSort(nums1[:])
sorted_nums2 = solution.insertionSort(nums2[:])
sorted_nums3 = solution.heapSort(nums3[:])
sorted_nums4 = solution.countingSort(nums4[:])

print("Bubble Sort:", sorted_nums)
print("Selection Sort:", sorted_nums1)
print("Insertion Sort:", sorted_nums2)
print("Heap Sort:", sorted_nums3)
print("Counting Sort:", sorted_nums4)
