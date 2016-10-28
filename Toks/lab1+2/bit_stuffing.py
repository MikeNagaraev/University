import bitarray
from bitstring import BitArray

searched_combination = bitarray.bitarray() 
searched_combination.extend([0,1,1,1,1,1])

def to_bits(x):
	bit_array = bitarray.bitarray() 
	bit_array.fromstring(x) 
	return bit_array

def append_stop(x):
	x.insert(x.__len__(), 1)
	return x

def append_start(x):
	x.insert(0, 0)
	return x

def transform_to_bits_push_to_list(_list):
	list2 = list(map(to_bits,_list))
	list2 = list(map(append_stop,list2))
	list2 = list(map(append_start,list2))
	print(list2)
	return list2

def copy_to_bitarray(list):
	bit_array = bitarray.bitarray() 
	for i in list:
		bit_array.extend(i)
	return bit_array

def insert_zero(positions,bit_array):
	j = 0
	for i in positions:
		bit_array.insert(i+6+j,0)
		j+=1

def bit_stuffing(bytes):
	formed_list = list(bytes)
	formed_list = transform_to_bits_push_to_list(formed_list)
	bit_array = copy_to_bitarray(formed_list)
	positions = bit_array.search(searched_combination)
	insert_zero(positions,bit_array)
	bit_array.fill()
	print('After BITSTUFFING: ')
	print(bit_array)
	return bit_array.tobytes()

def delete_stop_start(x):
	return x[1:x.__len__()-1]


def to_bytes(x):
	bit_array = bitarray.bitarray()
	bit_array = x
	return bit_array.tobytes().decode()

def to_list(array,num_elem):
	_list = list()
	for i in  range(int(array.__len__()/num_elem)):
		_list.append(array[i*num_elem:(i+1)*num_elem])
	return _list

def back_convert(bits_array):
	bits = bits_array #with stop/start/zero 
	normalbits = []

	#find first '0111110'


	# deleting EXTRA zeroes
	begin = 0
	end = bits.__len__()
	print('START BACK_CONVERT')
	print('RECIEVED MESSAGE IN BITS')
	print(bits)
	while begin < end:
		shift_begin = bits[begin:end].find('011111') 
		if(shift_begin != -1 and begin + shift_begin+len('011111') < end):		
			normalbits.append(bits[begin:begin + shift_begin+len('011111')])
			begin = begin + shift_begin +len('011111') + 1;
		else: 
			normalbits.append(bits[begin:end])
			break

	#deleting stop/start

	bit_array = copy_to_bitarray(normalbits)
	bit_array = bit_array[0:int(bit_array.__len__()/10 )*10]
	message_list=to_list(bit_array,10)
	message_list = list(map(delete_stop_start,message_list))
	print('AFTER DELETING STOP/START BITS')
	print('IN BITS: ')
	print(message_list)
	message_list = list(map(to_bytes,message_list))
	print('DECODE: ')
	print(message_list)
	message = ''.join(message_list)
	message = message[1:] #without '01111110'
	print('MESSAGE: ')
	print(message)
	
	return message

