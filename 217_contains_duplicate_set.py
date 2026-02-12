class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # lista de números já vistos
        for i in nums:  # para cada elemento de nums:
            if i in seen:  # se o elemento estiver em 'seen':
                return True  # retorna verdadeiro
            seen.add(i)  # adiciona o elemento a seen
        return False  # penis
