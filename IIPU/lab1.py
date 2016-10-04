#!/usr/bin/python

import libpci
import texttable as tt

devices_file = open('/proc/bus/pci/devices')

lines = devices_file.readlines()

raw_id = [x.split('\t')[1] for x in lines]

vendor_and_device = [(x[:4], x[4:]) for x in raw_id]

vendor_and_device = [(int(x[0], 16), int(x[1], 16)) for x in vendor_and_device]

pcitor = libpci.LibPCI()

tab = tt.Texttable()

x = [[]]  # The empty row will have the header

for kek, i in enumerate(vendor_and_device):
    x.append([kek, pcitor.lookup_device_name(i[0], i[1]), pcitor.lookup_vendor_name(i[0])])

tab.add_rows(x)
tab.set_cols_align(['l', 'l', 'l'])

tab.header(['id', 'Vendor name', 'Device name'])
print(tab.draw())