# Your tests here
def long_sub_str(keyword):
    l_seq= ''
    for i in range(len(keyword)):
        for j in range(i+1, len(keyword)):
            common= "".join(c for c in keyword[i] if c in keyword[j])
            if len(common) > len(l_seq):
                l_seq=common
    return l_seq

keyword = ['milk', 'catalog', 'c++', 'python','cat', 'dog']
result = long_sub_str(keyword)
print(result)
