import string

class Enum():
    dur = 'duration'
    start = 'start'
    stop = string.printable[90]
    IO = 'IOTest'
    Net = 'NetworkTest'
    iter = 'NumberOfIterations'
    tcp = 'TCPTest'
    mat = 'MatTest'
    rw = 'RWTest'
    band = 'BandwidthTest'
    stopClient = 'SystemExit'
    data = 'sendData'
    config = 'sendConfig'
    seek = 'SeekAndWrite'
    iteration = 'Iteration'
    plot = 'plotResults'
    chunkSize = 4096