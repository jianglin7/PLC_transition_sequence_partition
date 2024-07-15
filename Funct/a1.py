import re

import Inputs

S = Inputs.S

# print(f"S: {S}\n")

# Data processing: 't+' as a whole, filtered to remove default values
# e.g. 'list': ['t1', 't2', 't3', 't4', 't5', 't1', 't6', 't7', ...]
def find_t_pattern(sequence):
    pattern = r"t\d+"
    matches = re.findall(pattern, sequence)
    return matches

S = find_t_pattern(S)
print(S)

# Sequential Relation, the set of transition pairs where two transitions can be observed consecutively
# e.g. 'list': [('t1', 't6'), ('t1', 't2'), ('t2', 't3'), ('t3', 't9')....]
def Find_Seq(sequence):
    pairs = [(sequence[i], sequence[i+1]) for i in range(len(sequence) - 1)]
    unique_pairs = list(set(pairs))
    def custom_sort(item):
        return (len(item[0]), item[0])
    seq_pairs = sorted(unique_pairs, key=custom_sort)
    return seq_pairs

Seq = Find_Seq(S)
# print(seq_pairs)
# print(type(seq_pairs))

# Finding all the different transitions
# e.g. 'list': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15']
def Unique_elements(sequence):
    # Get different elements
    unique_elements = set(sequence)
    # list, sorting the elements
    Uni = sorted(unique_elements, key=lambda s: (len(s), s))
    return Uni

Uni = Unique_elements(S)
# print(Uni)
# print(type(Uni))

# Systematic Precedence, the set of transitions which must be fired to re-enable the firing of ti
# e.g. 'dict':{'t1': ['t4', 't5', 't1'], 't3': ['t3', 't7', 't4', 't5', 't6', 't11', 't1'],...}
def Find_PS(sequence):
    subsequences = []
    n = len(sequence)
    for start in range(n):
        for end in range(start + 1, n):
            if sequence[start] == sequence[end]:
                subsequence = sequence[start:end + 1]
                if subsequence not in subsequences:
                    subsequences.append(subsequence)
                break
    grouped_subsequences = {}
    for subsequence in subsequences:
        start_item = subsequence[0]
        if start_item in grouped_subsequences:
            grouped_subsequences[start_item].append(subsequence)
        else:
            grouped_subsequences[start_item] = [subsequence]
    PS = {}
    for key, sequences in grouped_subsequences.items():
        common_elements = set(grouped_subsequences[key][0])
        for lst in grouped_subsequences[key][1:]:
            common_elements = common_elements.intersection(set(lst))
        common_elements_list = list(common_elements)
        PS[key] = common_elements_list
    return PS


PS = Find_PS(S)
# print(type(PS))

# Reverse Systematic Precedence, the set of transitions that depend on ti to re-enable firing
# e.g. 'dict': {'t4': ['t1', 't3', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't15'], 't5': ['t1', 't3', 't4', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15']...}
def Find_InPS(PS):
    InPS = {}
    for key, values in PS.items():
        for value in values:
            if (value != key):
                if value in InPS:
                    InPS[value].append(key)
                else:
                    InPS[value] = [key]
    return InPS

InPS = Find_InPS(PS)
# print(type(InPS))

# Alternating Pattern, the set of transition pairs where two transitions alternate consecutively
# e.g. 'list': [('t1', 't2'), ('t2', 't1')...]
def Find_AP(sequence):
    AP = []  # 用于存储双循环变迁的集合
    for i in range(len(sequence) - 2):
        if sequence[i] == sequence[i + 2]:
            AP.append((sequence[i], sequence[i + 1]))
    return AP

AP= Find_AP(S)
# print(type(AP))

# Find  dual_direction in seq_pairs
# e.g. 'list': [('t4', 't14'), ('t4', 't10'), ('t10', 't4'), ('t14', 't4')]
def Find_dual_direction(Seq):
    dual_direction = []
    for a, b in Seq:
        if (b, a) in Seq:
            dual_direction.append((a, b))
    return dual_direction

d_direction_pairs = Find_dual_direction(Seq)
# print(type(d_direction_pairs))

# Combinations is used to find permutations of two distinct transitions assigned to the set T−combs
# 'list': e.g. [('t1', 't2'), ('t1', 't3'), ('t1', 't4'), ('t1', 't5'), ('t1', 't6'),...]
def Combinations(unique_elements, num):
    T_combs = []
    if num == 2:
        for i in range(len(unique_elements)):
            for j in range(len(unique_elements)):
                if unique_elements[i] != unique_elements[j]:
                    T_combs.append((unique_elements[i], unique_elements[j]))
    return T_combs

T_combs = Combinations(Uni, 2)
# print(type(T_combs))


# Order Independent, the set of transition pairs where two transitions are independent.
# e.g. 'list': [('t1', 't2'), ('t2', 't1'), ('t2', 't3'),...]
def Find_OI(all_combinations, prior_trasitions_dict):
    OI = []
    for a,b in all_combinations:
        if (b not in prior_trasitions_dict.get(a, [])) and (a not in prior_trasitions_dict.get(b, [])):
            OI.append((a,b))
    return OI

OI = Find_OI(T_combs, PS)
# print(OI)

# The set of transition pairs with causal relationship.
# e.g. 'list': CausalR = [('t1', 't6'), ('t3', 't4'), ('t4', 't5')]
def Find_CausalR(Seq, PS, AP):
    PS_list = []
    for key, values in PS.items():
        for value in values:
            PS_list.append((key, value))
    CausalR = []
    for a, b in Seq:
        if (a, b) in PS_list or (b, a) in PS_list or (a,b) in AP:
            CausalR.append((a, b))
    return CausalR

CausalR = Find_CausalR(Seq, PS, AP)
# print(CausalR)

# The set of transition pairs with concurrent relationship.
# e.g. 'list': ConcR = [('t4', 't14'), ('t14', 't4')]
def Find_ConcR(d_direction_pairs, CausalR, PS, OI, Seq, InPS):
    ConcR = []
    # 1
    for a, b in d_direction_pairs:
        if ((a, b) not in CausalR) and ((b, a) not in CausalR):
            if (len(PS[a]) > 1) and (len(PS[b]) > 1):
                ConcR.append((a, b))
    # 2
    for a, b in d_direction_pairs:
        if (a, b) in OI:
            for key, values in PS.items():
                if (a!=key) and (b!=key) and (a in PS[key]) and (b in PS[key]) and ((a,b) not in ConcR):
                    ConcR.append((a,b))
    # 3
    for a, b in d_direction_pairs:
        if (a, b) in OI:
            for key, values in PS.items():
                if b==key:
                   for value in values:
                       if (value not in PS[a]) and ((a, value) in Seq) and ((a,b) not in ConcR):
                           ConcR.append((a,b))
    # 4
    for a, b in d_direction_pairs:
        if (a, b) in OI:
            if a in InPS:
                for value in InPS[a]:
                    if ((value, b) in ConcR) and ((a,b) not in ConcR):
                        ConcR.append((a, b))
    return ConcR

ConcR = Find_ConcR(d_direction_pairs, CausalR, PS, OI, Seq, InPS)
# print(ConcR)

# The set of transition pairs with irrelevant relationship.
# e.g. 'list': IrrelR = [('t1', 't2'), ('t2', 't3'), ('t3', 't13'), ('t3', 't9'), ('t8', 't13'), ('t8', 't9')]
def Find_IrrelR(CausalR, ConcR, Seq):
    IrrelR = []
    excluded_elements = set(CausalR + ConcR)
    for pair in Seq:
        if pair not in excluded_elements:
            IrrelR.append(pair)
    return IrrelR

IrrelR = Find_IrrelR(CausalR, ConcR, Seq)
# print(IrrelR)