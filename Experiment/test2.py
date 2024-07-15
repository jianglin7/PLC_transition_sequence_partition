import pm4py
import pandas

# log = pm4py.read_xes('C:/Users/Jiang/Desktop/PLC_transition_sequence_partition-master\Experiment\Road_Traffic_Fine_Management_Process.xes')

# log = pm4py.filter_event_attribute_values(log, "concept:name", ["appeal to judge"], level="case", retain=False)

# α算法
# net,im,fm=pm4py.discovery.discover_petri_net_alpha(log)
# pm4py.view_petri_net(net, im, fm)

# 启发式
# map=pm4py.discover_heuristics_net(log)
# pm4py.view_heuristics_net(map)

# α+
# net, im, fm = pm4py.discover_petri_net_alpha_plus(log)
# pm4py.view_petri_net(net, im, fm)

# map=pm4py.discover_heuristics_net(log)
# net, initial_marking, final_marking = pm4py.convert_to_petri_net(map)
# pm4py.view_petri_net(net,initial_marking,final_marking)



# from pm4py.objects.log.importer.xes import importer as xes_importer
#
# # Import the XES file
# log_path = 'C:/Users/Jiang/Desktop/PLC_transition_sequence_partition-master\Experiment\Road_Traffic_Fine_Management_Process.xes'
# log = xes_importer.apply(log_path)
#
# event_log = pm4py.read_xes(log_path)
# event_log = pm4py.convert_to_dataframe(event_log)
# print(event_log)
#
# # 把事件日志输出为csv文件
# event_log.to_csv('C:/Users/Jiang/Desktop/PLC_transition_sequence_partition-master\Experiment\Road_Traffic_Fine_Management_Process.csv',encoding='utf-8')

# def conver_xes(csv_path,xes_path):
#     event_log = pm4py.format_dataframe(pandas.read_csv(csv_path, sep=','),case_id='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
#     pm4py.write_xes(event_log, xes_path)
#
# csv_path = 'C:/Users/Jiang/Desktop/PLC_transition_sequence_partition-master\Experiment\Road_Traffic_Fine_Management_Processnew.csv'
# xes_path = 'C:/Users/Jiang/Desktop/PLC_transition_sequence_partition-master\Experiment\Road_Traffic_Fine_Management_Processnew.xes'
# conver_xes(csv_path, xes_path)

# log = pm4py.read_xes('C:/Users/Jiang/Desktop/PLC_transition_sequence_partition-master\Experiment\Road_Traffic_Fine_Management_Processnew.xes')
# map=pm4py.discover_heuristics_net(log)
# net, initial_marking, final_marking = pm4py.convert_to_petri_net(map)
# pm4py.view_petri_net(net,initial_marking,final_marking)