class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev = 0
        total = 0
        for i in s:
            curr = roman_to_int[i]
            if curr > prev:
                total -= prev
            else:
                total += prev
            prev = curr
        total += prev
        return total