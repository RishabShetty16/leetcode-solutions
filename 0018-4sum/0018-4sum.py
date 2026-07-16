class Solution:
    def fourSum(self, arr, target):
        n = len(arr)
        arr.sort()
        ans = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])

                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return ans


