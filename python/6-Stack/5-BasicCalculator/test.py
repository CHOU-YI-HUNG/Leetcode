def split_with_symbols(text):
    split_result = []
    i = 0
    while i < len(text):
        if text[i] in "+-":
            split_result.append(text[i])
            i += 1
        else:
            start_index = i
            while i < len(text) and text[i] not in "+-":
                i += 1
            split_result.append(text[start_index:i])
    return split_result

text = "10+20-30"
split_result = split_with_symbols(text)
print(split_result)  # Output: ['10', '+', '20', '-', '30']
