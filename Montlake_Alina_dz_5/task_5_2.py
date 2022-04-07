"""2.Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield."""
max_num = 11
odd_to_n = (num for num in range(1,max_num+1,2))
print (odd_to_n)
