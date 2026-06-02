import pygame
import array
import math
import time

pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)

def generate_beep(freq, duration_ms, volume=0.5):
    sample_rate = 44100
    n_samples = int(sample_rate * (duration_ms / 1000.0))
    buf = array.array('h')
    
    max_amp = int(32767 * volume)
    for i in range(n_samples):
        t = float(i) / sample_rate
        # Sine wave
        val = int(max_amp * math.sin(2 * math.pi * freq * t))
        buf.append(val)
        
    sound = pygame.mixer.Sound(buffer=buf)
    return sound

print("Playing sine wave...")
sound = generate_beep(440, 500)
sound.play()
time.sleep(1)
print("Done")
