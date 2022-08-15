class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return f'{eval("*".join([num1,num2]))}'

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(f'{num1} * {num2}'))