PPQ: int = 480
bpm_global: int = 120

notas_midi: dict[str, int] = {
    'A': 21,  # La (A0 = MIDI 21)
    'B': 23,  # Si (B0 = MIDI 23)
    'C': 12,  # Do (C0 = MIDI 12)
    'D': 14,  # Re (D0 = MIDI 14)
    'E': 16,  # Mi (E0 = MIDI 16)
    'F': 17,  # Fa (F0 = MIDI 17)
    'G': 19,  # Sol (G0 = MIDI 19)
    'H': 22,  # Si Bemol (Bb0 = MIDI 22)
    'Eb': 15,  # Mi Bemol
    'Mb': 15,
    'Ab': 20,  # La Bemol
    'Bb': 22,  # Si Bemol
    'Db': 13,  # Re Bemol
    'Gb': 18  # Sol Bemol
}

character_voz: set[str] = {
    '?', '.', ' ', 'V'
}

character_pausa: set[str] = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
}

character_global: set[str] = {'>', '<'}

gm_intruments: dict[str, int] = {
    '!': 21,
    'O': 109,
    'o': 109,
    'U': 109,
    'u': 109,
    'I': 109,
    'i': 109,
    ',': 19,
    ';': 14
}
