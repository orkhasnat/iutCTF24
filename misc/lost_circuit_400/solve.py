'''
We import the VCD file and read the waveform, VCD files can be tricky. I needed
a lot of time to get familiar with this myself. Anyway after that, We realize
this is actually waveforms sent to a LCD screen. We know, there are commands
and stuff we send to LCD, but we should just need data. So it is enough just to
look at the following conditions
    - When is the RS high, so we are sending data to LCD
    - When RS is high, there should be two nibbles sent, ie, two pulses in E
    - If that is done, we will check the value of D47 line when that pulse
      happened

There are myriads of way to solve this including, handsolving like a CHAD. But
here is my python implementation.
'''


import vcdvcd
from vcdvcd import VCDVCD
from bisect import bisect_left

def parseToNibble(entry):
    t, data = entry
    try:
        return (t, int(data, 2))
    except:
        return (t, 0)

def generate_unique(it):
    prev = -1
    for t, x in it:
        if x != prev:
            prev = x
            yield (t, x)

vcd = VCDVCD('lost_circuit.vcd')

signals = list(vcd.data.keys())

print(vcd.data[signals[0]].references)
print(vcd.data[signals[1]].references)
print(vcd.data[signals[2]].references)
print(vcd.data[signals[3]].references)

d47 = list(generate_unique(map(parseToNibble, vcd.data[signals[0]].tv)))
rs = list(generate_unique(map(parseToNibble, vcd.data[signals[1]].tv)))
en = list(generate_unique(map(parseToNibble, vcd.data[signals[2]].tv)))

print(d47)

d47t, d47s = zip(*d47)
ent, ens = zip(*en)

data = ''

for t_rs, s_rs in rs:
    if s_rs == 1:
        ip = bisect_left(ent, t_rs)
        if ip == len(ent):
            break
        print(f'RS at {t_rs}, closest EN at {ent[ip]}')

        bb = 0
        for _ in range(4):
            if ens[ip] == 1:
                dip = bisect_left(d47t, ent[ip]) - 1
                print(f'Just before {ent[ip]}, we have {d47t[dip]}')
                bb = (bb << 4) | d47s[dip]
            ip += 1
        print(hex(bb))
        data += chr(bb)

print(data)
