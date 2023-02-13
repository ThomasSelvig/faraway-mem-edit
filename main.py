from pymem import Pymem

"""
offsets:

health:
	faraway.exe + 0x5a0cc8
	+ 0x30
	+ 0x1c
leaf inv slot:
	faraway.exe + 0x5a0ccc
	+ 0x2b8
	+ 0x4
	+ 0x8
	+ 0x14
food:
	faraway.exe + 0x5a0cc8
	+ 0x30
	+ 0x18

"""


faraway = Pymem("faraway.exe")


def addr_of_pointer(offset):
	# return faraway.read_ulonglong(offset)
	return faraway.read_int(offset)
	# return faraway.read_ulong(offset)


health_addr = addr_of_pointer(addr_of_pointer(faraway.base_address + 0x5a0cc8) + 0x30) + 0x1c
print("health", faraway.read_float(health_addr))

food_addr = addr_of_pointer(addr_of_pointer(faraway.base_address + 0x5a0cc8) + 0x30) + 0x18
print("food", faraway.read_float(health_addr))

leaf_addr = addr_of_pointer( addr_of_pointer( addr_of_pointer( addr_of_pointer( faraway.base_address + 0x5a0ccc) + 0x2b8) + 0x4) + 0x8) + 0x14
print("leaves", faraway.read_int(leaf_addr))

# faraway.write_int(leaf_addr, 45)
while True:
	faraway.write_float(health_addr, 100.)
