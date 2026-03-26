class SmartDevice:
    # SL part, Base class has device state and some power logic
    def __init__(self, device_id, base_power_draw, is_on=False):
        self.__device_id = device_id
        self.__is_on = is_on
        self.__base_power_draw = 0
        self.set_base_power_draw(base_power_draw)

    def get_device_id(self):
        return self.__device_id

    def get_is_on(self):
        return self.__is_on

    def get_base_power_draw(self):
        return self.__base_power_draw

    def set_device_id(self, device_id):
        self.__device_id = device_id

    def set_is_on(self, is_on):
        self.__is_on = is_on

    def set_base_power_draw(self, base_power_draw):
        if base_power_draw < 0:
            self.__base_power_draw = 0
        else:
            self.__base_power_draw = base_power_draw

    def toggle_power(self):
        self.__is_on = not self.__is_on

    def get_current_usage(self):
        if self.__is_on:
            return self.__base_power_draw
        return 0


class SmartLight(SmartDevice):
    # HL part, SmartLight inherits from SmartDevice
    # power usage depends on brightness level
    # and this adds brightness and uses it to scale the power usage later
    def __init__(self, device_id, base_power_draw, brightness, is_on=False):
        super().__init__(device_id, base_power_draw, is_on)
        self.__brightness = 0
        self.set_brightness(brightness)

    def get_brightness(self):
        return self.__brightness

    def set_brightness(self, brightness):
        if brightness < 0:
            self.__brightness = 0
        elif brightness > 100:
            self.__brightness = 100
        else:
            self.__brightness = brightness

    def get_current_usage(self):
        if self.get_is_on():
            return (self.__brightness / 100) * self.get_base_power_draw()
        return 0

class SmartThermostat(SmartDevice):
    # HL part, SmartThermostat inherits from SmartDevice
    # SmartThermostat tracks "goal" temp and based on that enable
    # heating or cooling or something
    def __init__(self, device_id, base_power_draw, goal_temp, is_on=False, is_active=False):
        super().__init__(device_id, base_power_draw, is_on)
        self.__goal_temp = goal_temp
        self.__is_active = is_active

    def get_goal_temp(self):
        return self.__goal_temp

    def get_is_active(self):
        return self.__is_active

    def set_goal_temp(self, goal_temp):
        self.__goal_temp = goal_temp

    def set_is_active(self, is_active):
        self.__is_active = is_active

    def get_current_usage(self):
        if self.get_is_on():
            usage = self.get_base_power_draw()
            if self.__is_active:
                usage += 500
            return usage
        return 0

class Room:
    # HL part, Room aggregates smart devices
    # Total room usage is found basically summing the device usage
    # Room aggregates devices and sums power using the polymorphism
    def __init__(self, room_name):
        self.__room_name = room_name
        self.__device_list = []

    def get_room_name(self):
        return self.__room_name

    def get_device_list(self):
        return self.__device_list

    def set_room_name(self, room_name):
        self.__room_name = room_name

    def set_device_list(self, device_list):
        self.__device_list = device_list

    def add_device(self, device):
        self.__device_list.append(device)

    def get_room_power_usage(self):
        total_usage = 0
        for device in self.__device_list:
            total_usage += device.get_current_usage()
        return total_usage

# Basic test for SL with uhhh three devices
tv = SmartDevice("TV1", 120)
fan = SmartDevice("FAN1", 60)
speaker = SmartDevice("SPKR1", 30)

tv.toggle_power()
speaker.toggle_power()

total_usage = tv.get_current_usage() + fan.get_current_usage() + speaker.get_current_usage()
print("Our total usage is uhhhh", total_usage, "W")

# HL stuff with rooms and some mixed types of devices
living_room = Room("Living Room")
kitchen = Room("Kitchen")

lamp = SmartLight("LIGHT1", 20, 75, True)
thermostat = SmartThermostat("THERMO1", 100, 22.5, True, True)
coffee_machine = SmartDevice("COFFEE1", 900, True)
desk_fan = SmartDevice("FAN2", 50, False)
kitchen_light = SmartLight("LIGHT2", 15, 40, True)
hall_thermostat = SmartThermostat("THERMO2", 90, 20.0, True, False)

# Living room
living_room.add_device(lamp)
living_room.add_device(thermostat)
living_room.add_device(desk_fan)

# Kitchen
kitchen.add_device(coffee_machine)
kitchen.add_device(kitchen_light)
kitchen.add_device(hall_thermostat)

print(living_room.get_room_name(), living_room.get_room_power_usage(), "W")
print(kitchen.get_room_name(), kitchen.get_room_power_usage(), "W")

