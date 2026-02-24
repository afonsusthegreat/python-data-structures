# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# Simulação da API do LeetCode (Mock)
BAD_VERSION = 4  # Você muda esse número para testar diferentes cenários


def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        esquerda = 1
        direita = n
        resposta = 0
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if isBadVersion(meio):
                resposta = meio
                direita = meio - 1
            else:
                esquerda = meio + 1
        return resposta
