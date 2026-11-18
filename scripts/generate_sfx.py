import os
import wave
import struct
import numpy as np

SFX_DIR = "assets_tsmc/sfx"
os.makedirs(SFX_DIR, exist_ok=True)
SAMPLE_RATE = 44100

def write_wav(filename, samples):
    path = os.path.join(SFX_DIR, filename)
    samples = np.clip(samples, -1.0, 1.0)
    int_samples = (samples * 32767).astype(np.int16)
    with wave.open(path, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(int_samples.tobytes())
    print(f"Generated SFX: {filename}")

# 1. Sub-bass Impact Boom (Deep 808 drop)
def gen_impact_boom():
    duration = 2.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    # Pitch drops from 120Hz to 38Hz
    freq = 120 * np.exp(-t * 2.5) + 38
    phase = 2 * np.pi * np.cumsum(freq) / SAMPLE_RATE
    env = np.exp(-t * 2.0)
    wave_data = np.sin(phase) * env
    # Add subtle sub harmonic
    wave_data += 0.5 * np.sin(phase * 0.5) * env
    return wave_data

# 2. Paper Slap / Polaroid drop
def gen_paper_slap():
    duration = 0.35
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    noise = np.random.normal(0, 1, len(t))
    # Quick attack, exponential decay
    attack = int(0.005 * SAMPLE_RATE)
    env = np.zeros(len(t))
    env[:attack] = np.linspace(0, 1, attack)
    env[attack:] = np.exp(-t[attack:] * 25.0)
    # Bandpass simulation (low punch + mid papery rustle)
    low_punch = np.sin(2 * np.pi * 95 * t) * np.exp(-t * 30.0) * 0.8
    wave_data = (noise * env * 0.5) + low_punch
    return wave_data

# 3. Highlighter Marker Wipe
def gen_marker_wipe():
    duration = 0.4
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    noise = np.random.normal(0, 1, len(t))
    # Bell envelope
    env = np.sin(np.pi * t / duration) ** 1.8
    # High frequency squeak modulation
    mod = np.sin(2 * np.pi * 1800 * t + np.sin(2 * np.pi * 35 * t) * 5)
    wave_data = noise * env * 0.4 + (mod * env * 0.2)
    return wave_data

# 4. Clock Tick
def gen_clock_tick():
    duration = 0.15
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    # Sharp impulse at 2.4 kHz with fast 15ms decay
    env = np.exp(-t * 70.0)
    wave_data = np.sin(2 * np.pi * 2400 * t) * env * 0.9
    return wave_data

# 5. Typewriter Key Click
def gen_typewriter():
    duration = 0.2
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    env = np.exp(-t * 50.0)
    click = np.sin(2 * np.pi * 3200 * t) * env
    thud = np.sin(2 * np.pi * 220 * t) * np.exp(-t * 30.0) * 0.6
    return (click * 0.6) + thud

# 6. Ambient Sub Drone (Loopable background tension)
def gen_sub_drone():
    duration = 10.0
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration))
    lfo = (np.sin(2 * np.pi * 0.2 * t) + 1.2) * 0.5
    drone = np.sin(2 * np.pi * 48 * t) + 0.3 * np.sin(2 * np.pi * 96 * t)
    wave_data = drone * lfo * 0.4
    return wave_data

write_wav("impact_boom.wav", gen_impact_boom())
write_wav("paper_slap.wav", gen_paper_slap())
write_wav("marker_wipe.wav", gen_marker_wipe())
write_wav("clock_tick.wav", gen_clock_tick())
write_wav("typewriter.wav", gen_typewriter())
write_wav("sub_drone.wav", gen_sub_drone())
print("All studio SFX generated in assets_tsmc/sfx!")
