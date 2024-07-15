def split_sequence(seq):
    """
    将序列在指定模式后划分为子序列。
    :param seq: 原始序列列表
    :param split_pattern: 划分模式
    :return: 分割后的子序列列表
    """
    if len(seq) < 2:
        return [seq]  # 序列太短无法形成分割模式

        # 构建分割模式
    split_pattern = [seq[-1], seq[0]]

    sub_sequences = []
    last_index = 0

    # 遍历序列，查找划分模式
    i = 0
    while i < len(seq) - len(split_pattern) + 1:
        # 如果找到分割模式
        if seq[i:i + len(split_pattern)] == split_pattern:
            # 添加从上一个分割点到当前分割点的子序列，并包括分割模式的第一个元素
            sub_sequences.append(seq[last_index:i + 1])
            last_index = i + 1
            i += len(split_pattern) - 1  # 跳过分割模式长度减1
        i += 1

    # 添加最后一个分割点到序列结束的部分
    if last_index < len(seq):
        sub_sequences.append(seq[last_index:])

    return sub_sequences


# 示例序列
seq = ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C']
sub_seqs = split_sequence(seq)
for sub_seq in sub_seqs:
    print("子序列:", sub_seq)


# 给定的序列列表
sequences_list = [['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'F', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'B', 'D', 'E', 'C', 'A', 'B', 'D', 'E', 'F', 'D', 'E', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'B', 'D', 'E', 'C'], ['H', 'D', 'E', 'G'], ['A', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'F', 'D', 'E', 'G'], ['A', 'D', 'E', 'F', 'D', 'B', 'E', 'C', 'A', 'D', 'E', 'F', 'D', 'E', 'B', 'C'], ['H', 'D', 'E', 'G']]
print(sequences_list)

# 用于存储所有分割后的子序列
all_sub_sequences = []

# 应用函数
for seq in sequences_list:
    sub_seqs = split_sequence(seq)
    for sub_seq in sub_seqs:
        print("子序列:", sub_seq)
        all_sub_sequences.extend(sub_seqs)

print(all_sub_sequences)