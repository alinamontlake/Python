"""1.Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод."""

import time


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 10))

    def running(self):
        for color, time_traffic_light in self.__color:
            print(f'{color}! wait ... {time_traffic_light} seconds')
            time.sleep(int(time_traffic_light))


traffic_light = TrafficLight()
while True:
    traffic_light.running()
