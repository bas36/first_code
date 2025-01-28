from pioneer_sdk import Pioneer
pioneer_mini = Pioneer(logger=False)
while True:
    number = int(input("Введите число: "))
    if number % 2 == 0:
        print("Четное")
        pioneer_mini.led_control(r=0, g=255, b=0)
    else:
        print("Нечетное")
        pioneer_mini.led_control(r=255, g=0, b=0)