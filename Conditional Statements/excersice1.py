import time

# timestamp = time.strftime('%H:%M:%S')
# print("Current timestamp:", timestamp)
# timestamp =time.strftime('%H')
# print("Current hour", timestamp)
# timestamp =time.strftime('%M')
# print("Current minute", timestamp)
# timestamp =time.strftime('%S')
# print("Current second", timestamp)

minute =int(time.strftime('%M'))
hrs = int(time.strftime('%H'))
if hrs < 12:
    print("Good Morning Sir")
elif hrs < 16:
    print("Good Afternoon Sir")
elif hrs < 20:
    print("Good Evening Sir")
else:
    print("Good Night Sir")