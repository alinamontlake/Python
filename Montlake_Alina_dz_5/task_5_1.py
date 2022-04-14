"""1.Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield"""

def odd_to_n(max_num):
     for num in range(1,max_num+1,2):
         yield num

new_odd_to_n = odd_to_n(9)
print(new_odd_to_n)
