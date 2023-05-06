class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 10:
                # break if no remainder
                break

            digits[i] = 0
            # if it is the first digit, insert 1 at the beginning
            if i == 0:
                digits.insert(0, 1)
                continue

            # else
            digits[i - 1] += 1

        return digits


if __name__ == "__main__":
    sol = Solution()

    digits = [1, 2, 3]
    print(sol.plusOne(digits))

    digits = [4, 3, 2, 1]
    print(sol.plusOne(digits))

    digits = [9]
    print(sol.plusOne(digits))
