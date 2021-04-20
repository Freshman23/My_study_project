from time import sleep
from itertools import cycle


class TrafficLight:
    __color_list = ('Red', 'Yellow', 'Green')

    def __init__(self, red_dur=7, yel_dur=2, grn_dur=7):
        """При инициализации экземпляра задаем продолжительность действия каждого света
        или оставляем значения по умолчанию.
        Создаем поле экземпляра в виде словаря, где ключи - свет, значения - продолжительность его действия."""
        self.color_dict = {light: dur for light, dur in zip(TrafficLight.__color_list, (red_dur, yel_dur, grn_dur))}

    def running(self, amount_cycles):
        """При вызове метода передаем дополнительно количество циклов действия светофора.
        PS. Думаю, нет смысла обозначать amount_cycles, count_cycles в качестве полей экземпляра."""
        print('Traffic light switched on.')
        count_cycles = 0
        for light in cycle(self.color_dict):
            if count_cycles >= amount_cycles * 3:
                break
            print(f'{light} light is on')
            sleep(self.color_dict[light])
            count_cycles += 1
        print('Traffic light switched off.')


trf_lgt = TrafficLight(5, 1, 5)
print(trf_lgt.color_dict)
trf_lgt.running(3)
