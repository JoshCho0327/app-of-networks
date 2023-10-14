import random

pkt_in_q = 0  # initial pkt number in the queue 隊列中的數據包數量初始化為0
pkt_dropped = 0  # initial dropped pkt number 已丟棄的數據包數量初始化為0

# event times
#模擬的事件數量
num_events_to_simulate = 2000

# set departure rate and buffer size
# 設定到達率和離開率及buffer大小
arrival_rate = 25
departure_rate = 60
buffer_size = 60

count = 0
arr = 0

with open('output2.txt', 'w') as file:
    # Simulate the events
    for i in range(num_events_to_simulate):
        file.write(f"{i + 1} {pkt_in_q} {pkt_dropped}\n")
        count += 1
    
        # calculate the probavility for arrival and departure 
        #計算到達事件和離開事件的機率
        p_arrival = arrival_rate / (arrival_rate + departure_rate) #λ/(λ+μ) 
    
        # give a random number to decide whether arrival or departure 
        #生成隨機數，以確定下一個事件是到達還是離開事件
        random_num = random.random() 
    
        if random_num <= p_arrival: 
            #arr += 1
            #print("arr", arr)
            if pkt_in_q < buffer_size:
                # 到達事件，如果隊列未滿，增加隊列中的數據包數量
                pkt_in_q += 1
            else:
                pkt_dropped += 1
        else:
            # 離開事件，減少隊列中的數據包數量（如果隊列不為空)
            if pkt_in_q > 0:
                pkt_in_q -= 1

# 輸出最終的隊列狀態
print("最終隊列中的數據包數量:", pkt_in_q)
print("已丟棄的數據包數量:", pkt_dropped)
print("執行了：", count, "次")

# 打开一个文本文件以写入数据
#with open('output.txt', 'w') as file:
#    # 写入事件次数、队列中数据包数量和已丢弃的数据包数量
#    for i in range(num_events_to_simulate):
#        # 在每次模拟后将数据写入文件
#        file.write(f"{i + 1} {pkt_in_q} {pkt_dropped}\n")

print("数据已写入到 output2.txt 文件中。")

