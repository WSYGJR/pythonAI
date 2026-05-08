elec = float(input("用电度数为"))
total_count = 0
if elec < 2880:
    total_count = elec * 0.4883
elif elec >= 2880 and elec <=4800:
    total_count = 2880*0.4883 + (elec - 2880) * 0.5383
elif elec > 4800:
    total_count = 2880*0.4883 + (4800 - 2880) * 0.5383 + (elec - 4800) * 0.7883
print("总计电费为：", total_count)