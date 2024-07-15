import a1
import Inputs

# Calculation of causal frequency
# e.g. 'dict': {('t1', 't6'): 29, ('t3', 't4'): 1, ('t4', 't11'): 22, ('t4', 't10'): 3,...}
def Count_frequency(S, CausalR):
    causal_frequencies = {}
    for item in CausalR:
        pattern = list(item)
        count = 0
        for i in range(len(S) - 1):
            if [S[i], S[i + 1]] == pattern:
                count += 1
        causal_frequencies[item] = count
    return causal_frequencies

S = a1.S
CausalR = a1.CausalR
Causal_frequencies = Count_frequency(S, CausalR)
# print(type(Causal_frequencies))

# Finding Pass Relationships
# e.g. 'list': [( , ), ( , ), ...]
def Find_Rpass(ConcR, IrrelR):
    Rpass = []
    for a, b in IrrelR:
        for c, d in ConcR:
            if a == c:
                Rpass.append((d, b))
            elif a == d:
                Rpass.append((c, b))
            elif b == c:
                Rpass.append((a, d))
            elif b == d:
                Rpass.append((a, c))
    return Rpass

ConcR = a1.ConcR
IrrelR = a1.IrrelR
Rpass = Find_Rpass(ConcR, IrrelR)

# Finding Breakpoint
# e.g. 'list': [('t1', 't2'), ('t2', 't3'), ('t3', 't9'), ('t3', 't13'), ('t8', 't9'), ('t8', 't13'), ('t3', 't4'), ('t4', 't5')]
def Find_Bp(IrrelR, Rpass, Causal_frequencies, frequency_threshold):
    Bp = IrrelR
    for item in Rpass:
        if item not in Bp:
            Bp.append(item)
    for item, count in Causal_frequencies.items():
        # if count < 0.005 * (len(S) - 1):
        if count < frequency_threshold:
            Bp.append(item)
    return Bp

frequency_threshold = Inputs.frequency_threshold
Bp = Find_Bp(IrrelR, Rpass, Causal_frequencies, frequency_threshold)
# print(Bp)

# the process of partitioning, results in partitioned traces
# e.g. 'list': [['t1'], ['t2'], ['t3'], ['t4'], ['t5', 't1', 't6', 't7', 't8'], ['t9', 't4', 't10', 't11', 't12', 't5', 't1', 't6', 't7', 't3'], ...]
def Do_partition(S, Bp):
    Partitioned_traces = []
    Current_trace = []
    for item in range(len(S)):
        Current_trace.append(S[item])
        if item != len(S) - 1 and ((S[item], S[item + 1]) in Bp):
            Partitioned_traces.append(Current_trace)
            Current_trace = []
    if Current_trace:
        Partitioned_traces.append(Current_trace)
    return Partitioned_traces

Partitioned_traces = Do_partition(S, Bp)
# print(Partitioned_traces)