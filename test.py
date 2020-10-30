import time

localtime = time.localtime(time.time())
print("Local current time :", localtime)

from datetime import datetime

dt1 = datetime(year=2020, month=3, day=31)
print(dt1)

dt1 = datetime(year=2020, month=3, day=31, hour=21, minute=21, second=21)
print(dt1)

dt1 = datetime(2020, 3, 31)
print(dt1)

dt1 = datetime(2020, 3, 31, 21, 21, 20)
print(dt1)

print(dt1.year);  print(dt1.month);  print(dt1.day)
print(dt1.hour);  print(dt1.minute); print(dt1.second)

print("=====================================================")
print(datetime.now())
print(datetime.today())

print("=====================================================")
print("=====================================================")

ct = datetime.now()

ct_y = ct.year
ct_m = ct.month
ct_d = ct.day
ct_h = ct.hour
ct_m = ct.minute
ct_s = ct.second
ct_ms = ct.microsecond

ct_m_y = ct_y, ct_m, ct_d, ct_h, ct_m, ct_s, ct_ms

print(ct_m_y)

print("=====================================================san")
ct = datetime.now()
print(ct.microsecond)
