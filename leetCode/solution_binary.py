
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_a = 0
        sum_b = 0
        for counter in range(0, len(a)):
            sum_a += int(a[counter]) * (2 ** counter)

        for counter in range(0, len(b)):
            sum_b += int(b[counter]) * (2 ** counter)

        addition = sum_a + sum_b

        print(f"The first add = {sum_a}\n"
              f"The second add = {sum_b}\n"
              f"The addition = {addition}")

        answer = ""
        while addition != 1:
            number = addition % 2
            answer += str(number)

            addition = addition // 2
        answer += str(addition)

        answer = answer[::-1]
        return answer
