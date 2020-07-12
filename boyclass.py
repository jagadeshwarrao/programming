class Boy:
    def say_hello(self):
        print("Hi! Welcome to the game!")
    def say_time(self,hour,minute):
        print("It has been",hour,"hours and",minute,"minutes")








boy1 = Boy()

boy1.say_hello()

hour = int(input())
minute = int(input())

boy1.say_time(hour, minute)