def speed_check(speed):
    if speed <= 60:
        return "OK"

    else:
        speed1 = (speed-60)//5

        if speed1 <= 12:
            return print(f"Point: {speed1}")

        else:
            return print("Time to go to jail!")


enter = speed_check(int(input("Enter speed: ")))
print(enter)