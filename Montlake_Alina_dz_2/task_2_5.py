"""5. a. Создать список, содержащий цены на товары (10–20 товаров).
Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
b. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
c. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
d. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?"""

"a"
pricelist = [38.5, 45.62, 97.12, 49, 13.93, 15, 18.76, 67, 90.21, 14.99, 87.54, 14.9, 76.88, 45, 55]
print (id(pricelist))
for i, number in enumerate(pricelist):
    price = str(f"{float(number):.2f}").split(".")
    
    print (f"{price[0]} руб {price[1]} коп", end = ",")

"b"
pricelist.sort()
print(pricelist)
print(id(pricelist))

"Мы видим, что id первоначального списка (строка 10) = id измененного списка (после расставления значений по возрастанию) (строка 18)"

"c"
pricelist.sort(reverse = True)
new_pricelist = pricelist
print (new_pricelist)

"d"
only_expensive = new_pricelist[:5]
only_expensive.sort(reverse = False)
print (only_expensive)
