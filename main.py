from pymem import Pymem


faraway = Pymem("faraway.exe")

def addr_of_pointer(offset):
	return faraway.read_int(offset)

def follow_pointers(base_offset, *pointer_offsets):
	addr = addr_of_pointer(faraway.base_address + base_offset)
	for offset in pointer_offsets[:-1]:
		addr = addr_of_pointer(addr + offset)
	return addr + pointer_offsets[-1]

health_addr = follow_pointers(0x5a0cc8, 0x30, 0x1c)
print("health", faraway.read_float(health_addr))

food_addr = follow_pointers(0x5a0cc8, 0x30, 0x18)
print("food", faraway.read_float(health_addr))

while True:
	faraway.write_float(health_addr, 100.)
	faraway.write_float(food_addr, 100.)
