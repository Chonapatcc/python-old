# module date / time
import datetime 

date=datetime.datetime.now() # yyyy,m,d,h,m,s
print(date)
print(date.year)
print(date.month)

#กำหนด เวลา
newdate=datetime.datetime(2020,11,1)
print(newdate)

# รูปแบบการแสดงผล
print(date.strftime("%x")) #m/d/y
print(date.strftime("%X")) # เวลา time
print(date.strftime("%c"))
#%H M S
print(date.strftime("%H:%M:%S"))
#1-365
print(date.strftime("%j"))
#day
print(date.strftime("%a")) #shorts
print(date.strftime("%A")) #full
print(date.strftime("%w")) # 0=sunday
print(date.strftime("%d")) #วันที่
print(date.strftime("%b")) #เดือนแบบสั้น
print(date.strftime("%B")) # เดือนfull

#d/m/y
print(date.strftime("%d/%M/%Y"))