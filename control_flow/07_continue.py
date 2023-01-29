num = 100
while num > 0:
    print(num)
    # 死循环 永远也到不了 49
    if num == 50:
        print("break here because num == %s" % num)
        continue
    num -= 1

# Path: control_flow\07_continue.py
