import random

pkt_in_q = 0  # initial pkt number in the queue 隊列中的數據包數量初始化為0
pkt_dropped = 0  # initial dropped pkt number 已丟棄的數據包數量初始化為0

# event times
#模擬的事件數量
num_events_to_simulate = 1000000

# set departure rate and buffer size
departure_rate = 125
buffer_size = 100

#set arrival rate base on events times
arrival_rate = [70] * (num_events_to_simulate // 10) + \
               [200] * (num_events_to_simulate * 6 // 10) + \
               [130] * (num_events_to_simulate // 10) + \
               [120] * (num_events_to_simulate // 10) + \
               [70] * (num_events_to_simulate // 10)
#print(arrival_rate)
count = 0

with open('input_data.txt', 'w') as file:

    # Simulate the events
    for i in range(num_events_to_simulate):
        file.write(f"{i + 1} {pkt_in_q} {pkt_dropped}\n")
        count += 1
    
        # calculate the probavility for arrival and departure 
        #計算到達事件和離開事件的機率
        p_arrival = arrival_rate[i] / (arrival_rate[i] + departure_rate) #λ/(λ+μ) 
        
        # give a random number to decide whether arrival or departure 
        #生成隨機數，以確定下一個事件是到達還是離開事件
        random_num = random.random() 
    
        if random_num <= p_arrival: 
            #arr += 1
            #print("arr", arr)
            if pkt_in_q < buffer_size:
                # 達事件，如果隊列未滿，增加隊列中的數據包數量
                pkt_in_q += 1
            else:
                pkt_dropped += 1
        else:
            # 離開事件，減少隊列中的數據包數量（如果隊列不為空)
            if pkt_in_q > 0:
                pkt_in_q -= 1

#Final queue status
print("Final packet number in the queue:", pkt_in_q)
print("Packets Dropped:", pkt_dropped)
print("Executed：",count, "times")