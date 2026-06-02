import ctypes
import time

winmm = ctypes.windll.winmm
hmidi = ctypes.c_void_p()
res = winmm.midiOutOpen(ctypes.byref(hmidi), -1, 0, 0, 0)
print(f"midiOutOpen result: {res}")

if res == 0:
    # Program change to Piano (0)
    winmm.midiOutShortMsg(hmidi, 0xC0 + (0 << 8))
    
    # Note on C4 (60)
    msg = 0x90 + (60 << 8) + (127 << 16)
    print("Playing Note On...")
    winmm.midiOutShortMsg(hmidi, msg)
    
    time.sleep(1)
    
    # Note off C4
    msg = 0x80 + (60 << 8) + (0 << 16)
    print("Playing Note Off...")
    winmm.midiOutShortMsg(hmidi, msg)
    
    winmm.midiOutClose(hmidi)
    print("Closed.")
