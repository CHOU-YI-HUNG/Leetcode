# 原始列表
original_list = [7, 2, 5, 1, 9]

# 通过enumerate函数创建原始列表的索引和值的映射
indexed_list = list(enumerate(original_list))


# 对列表进行排序，根据元素的第二个值（即列表中的值）
sorted_list = sorted(indexed_list, key=lambda x: x[1])
print(sorted_list[0][1])

# # 输出排序后的列表和原始列表的索引之间的映射
# for new_index, (original_index, value) in enumerate(sorted_list):
#     print(f"原始列表索引 {original_index} 对应于排序后的索引 {new_index}")
