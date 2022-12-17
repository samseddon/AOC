file = open('input_day_6.txt', 'r')                                            
Line = file.readlines()
signal = Line[0].strip()
length_signal_search = 14

for i in range(length_signal_search,len(signal)):
    datastream = list(signal[i-length_signal_search:i])
    datastream_reduced = list(set(datastream))
    datastream_reduced.sort()
    datastream.sort()
    if datastream == datastream_reduced:
        print(i,datastream)
        break
