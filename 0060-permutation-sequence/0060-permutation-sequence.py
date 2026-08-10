class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        numbers = list(range(1, n + 1))

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1

        ans = ""

        while numbers:

            index = k // fact

            ans += str(numbers[index])

            numbers.pop(index)

            if not numbers:
                break

            k %= fact

            fact //= len(numbers)

        return ans