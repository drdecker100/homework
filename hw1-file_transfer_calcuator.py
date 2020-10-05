#----------------------------------------------------
# PROJECT TITLE: SIMPLE FILE TRANSFER TIME CALCULATOR 
#----------------------------------------------------


while True:

    print("\nWelcome Back!!\n")

    #prompt user for a file size in MegaBytes
    size = input("Enter file size in MB: ").strip()

    #check if input is a digit
    if size.isdigit():
        size = float(size)
    else:
        print(">>>Wrong input, key in the right file size")
        continue
    
    #convert size to Megabits( 1 MB = 8 Mbit)
    size_Mbit = 8 * size

    #prompt user for a file transfer speed in Mb/s
    speed = input("Enter file transfer speed in Mb/s: ").strip()

    #check if input is a digit
    if speed.isdigit():
        speed = float(speed)
    else:
        print(">>>Wrong input, key in the right file transfer speed")
        continue

    #Display file transfer time in sec(round to a max 2 decimal places)
    time = size_Mbit / speed

    if time < 60 :
        print("="*45)
        print( "The time recorded is",round(time,2),"second(s)" )
        print("="*45,"\n")

    else:    
        time_mins = time //60
        time_secs = time % 60
        print("="*45)
        print( "The time recorded is",int(time_mins), "minute(s)", round(time_secs),"second(s)") 
        print("="*45,"\n")



