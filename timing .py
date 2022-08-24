T=input("enter the timings start:")
T1=input("enter the timings ending:")
if T>="6:15" and T1<="6:59":
	print("exersise")
elif T>="7:00" and T1<="7:59":
    print("freshup")
elif T>="8:00" and T1<="8:29":
	print("breakfast")
elif T>="8:30" and T1<="12:29":
	print("1st coding")
elif T>="12:30" and "T1"<="14:00":
    print("lunch bell")
elif T>="14:00" and T1<="16:59":
	print("2nd coding")
elif T>="17:00" and T1<="17:59":
	print("snacks")
elif T>="18:00" and T1<="18:59":
    print("english activity")
elif T>="19:00" and T1<="19:59":
    print("recreation activity")
elif T>="20:00" and T1<="20:59":
    print("dinner time")
else:
	print("no timings")