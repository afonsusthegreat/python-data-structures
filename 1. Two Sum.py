nums_suja, target_suja = ('nums = [2,7,11,15], target = 9').split(', ')
print(nums_suja, target_suja)
nums_limpo = nums_suja.replace('nums = ', '').replace('[', '').replace(']', '')
lista_strings = nums_limpo.split(',')
nums = [int(i) for i in lista_strings]
target_limpo = target_suja.replace('target = ', '')
target = int(target_limpo)
print(nums, target)
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
