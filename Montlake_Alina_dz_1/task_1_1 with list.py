seconds = int(input(''))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
duration = [str(days) + " дн", str(hours) + " час", str(minutes) + " мин", str(seconds) + " сек"]
if seconds > 0:
    print (duration)
else:
    print("Невременное значение. Пожалуйста, введите положительное число")
