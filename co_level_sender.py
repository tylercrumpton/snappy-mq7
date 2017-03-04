from mq7 import *

REPORT_PERIOD = 60  # in seconds
time_until_report = REPORT_PERIOD  # in seconds


@setHook(HOOK_STARTUP)
def init():
    mq7_init()


@setHook(HOOK_1S)
def timer_1s():
    global time_until_report
    if time_until_report <= 0:
        time_until_report = REPORT_PERIOD
        mcastRpc(1, 3, "co_level_report", mq7_get_co_level())
    else:
        time_until_report -= 1
