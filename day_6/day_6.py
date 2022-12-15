file = open('input_day_6.txt', 'r')                                            
Line = file.readlines()
signal = Line[0].strip()
length = 14
for i in range(length,len(signal)):
    datastream = list(signal[i-length:i])
    datastream_reduced = list(set(datastream))
    datastream_reduced.sort()
    datastream.sort()
    if datastream == datastream_reduced:
        print(i,datastream)
        break
