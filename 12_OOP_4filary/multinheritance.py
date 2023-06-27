class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')


class Watch(UsefulStuff):
    def __init__(self, watch_name):
        print(f"{watch_name} is elegant & small")
        super().__init__(watch_name)


class Phone(UsefulStuff):
    def __init__(self, phone_name):
        print(phone_name, "can make a call & write sms")
        super().__init__(phone_name)


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('Smartwatch is great, small, smart, and conviniet!')
        super().__init__("smart watch")

sw = SmartWatch()


