from datetime import datetime


class Clock:

    def current_time(self) -> None:
        print(datetime.now().strftime("%H:%M:%S"))


class Alarm:

    def on(self) -> None:
        print('Будильник включен')


    def off(self) -> None:
        print('Будильник выключен')


class AlarmClock(Clock, Alarm):

    def alarm_on(self) -> None:
        self.on()


clock = AlarmClock()

clock.current_time() 
clock.alarm_on()
