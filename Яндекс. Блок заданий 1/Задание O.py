n = int(input())
m = int(input())
t = int(input())

total_minutes = n * 60 + m  
arrival_time = (total_minutes + t) % (24 * 60)  

arrival_hours = arrival_time // 60
arrival_minutes = arrival_time % 60

print(f"{arrival_hours:02}:{arrival_minutes:02}")
