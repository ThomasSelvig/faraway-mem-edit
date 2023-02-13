from pymem import Pymem


faraway = Pymem("faraway.exe")

def addr_of_pointer(offset):
	return faraway.read_int(offset)


health_addr = addr_of_pointer(addr_of_pointer(faraway.base_address + 0x5a0cc8) + 0x30) + 0x1c
print("health", faraway.read_float(health_addr))

food_addr = addr_of_pointer(addr_of_pointer(faraway.base_address + 0x5a0cc8) + 0x30) + 0x18
print("food", faraway.read_float(health_addr))

while True:
	faraway.write_float(health_addr, 100.)
	faraway.write_float(food_addr, 100.)
