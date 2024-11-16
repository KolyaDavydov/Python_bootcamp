import ctypes
import os


CLOCK_MONOTONIC_RAW = 4


class Timespec(ctypes.Structure):
    _fields_ = [('tv_sec', ctypes.c_long)]


def monotonic() -> float:

    librt = ctypes.CDLL('librt.so.1', use_errno=True)
    clock_gettime = librt.clock_gettime
    clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(Timespec)]

    t = Timespec()

    if clock_gettime(CLOCK_MONOTONIC_RAW, ctypes.pointer(t)):
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return t.tv_sec


if __name__ == "__main__":
    print('monotonic время из библиотеки ctypes: ', monotonic(), 'c')
