from time import sleep as slp

class TrafficLight:
    __TrafficLight_color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        f = 0
        while f < 3:
            print(f'Светофор загорелся {TrafficLight.__TrafficLight_color[f]} цветом.')
            slp(7)
            if f == 1:
                slp(2)
            f += 1


TrafficLight1 = TrafficLight()
TrafficLight.running(TrafficLight1)