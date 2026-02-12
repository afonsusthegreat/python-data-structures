class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        count = min(len(word) for word in strs)
        """count = menor comprimento de palavra dentro da lista 'strs'"""
        for i in range(count):
            """para cada número i de 0 até count - 1:"""
            letra = strs[0][i]
            """a variável 'letra' vai ser a i-ésima letra da
            primeira palavra de strs"""
            for word in strs:
                """para cada palavra 'word' na lista strs:"""
                if letra != word[i]:
                    """se a variável 'letra' for diferente da i-ésima
                    letra da palavra 'word':"""
                    return prefix
                    """retorna a variável prefix e encerra o código"""
            prefix += letra
            """essa parte só vai executar caso em nenhum momento a variável
            letra seja diferente da variável word"""
        return prefix
