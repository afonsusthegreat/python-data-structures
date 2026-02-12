class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}
        sorted_strs = []
        lista_final = []
        for i in strs:
            temp = sorted(i)
            temp = tuple(temp)
            sorted_strs.append(temp)
        for i in sorted_strs:
            if i not in group:
                group[i] = []
        for index, item in enumerate(sorted_strs):
            if item in group:
                group[item].append(strs[index])
        for key in group:
            lista_final.append(group[key])
        return lista_final
