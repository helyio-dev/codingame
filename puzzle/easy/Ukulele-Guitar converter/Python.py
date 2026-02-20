import sys

def solve():
    line1 = sys.stdin.readline().strip()
    if not line1:
        return
    instrument = line1
    
    line2 = sys.stdin.readline().strip()
    if not line2:
        return
    n = int(line2)
    
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    guitar_tuning = ["E4", "B3", "G3", "D3", "A2", "E2"]
    ukulele_tuning = ["A4", "E4", "C4", "G4"]

    def get_semitones(note_str):
        name = note_str[:-1]
        octave = int(note_str[-1])
        return octave * 12 + notes.index(name)

    guitar_base = [get_semitones(t) for t in guitar_tuning]
    ukulele_base = [get_semitones(t) for t in ukulele_tuning]

    if instrument == "guitar":
        src_tuning = guitar_base
        dst_tuning = ukulele_base
        max_fret = 15
    else:
        src_tuning = ukulele_base
        dst_tuning = guitar_base
        max_fret = 21

    for _ in range(n):
        line = sys.stdin.readline().split()
        if not line:
            continue
        s_idx, f_val = map(int, line)
        target_note = src_tuning[s_idx] + f_val
        
        matches = []
        for d_idx, base_note in enumerate(dst_tuning):
            fret_needed = target_note - base_note
            if 0 <= fret_needed <= max_fret:
                matches.append((d_idx, fret_needed))
        
        if matches:
            matches.sort()
            print(" ".join(f"{m[0]}/{m[1]}" for m in matches))
        else:
            print("no match")

if __name__ == "__main__":
    solve()