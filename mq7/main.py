MQ_ADC = 0
MQ_PIN = 24


def mq7_init():
    setPinDir(MQ_PIN, False)


def mq7_get_co_level():
    level = readAdc(MQ_ADC)
    for i in xrange(15):
        level += readAdc(MQ_ADC)
    return level / 16

