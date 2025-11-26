amount = int(input())
denomination = int(input())
notes = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
for note in [100, 50, 20, 10, 5, 2, 1]:
    if note == denomination:
        notes[note] = amount // note
        amount = amount % note
        break
for note in [100, 50, 20, 10, 5, 2, 1]:
    if note < denomination:
        notes[note] = amount // note
        amount = amount % note
for note in [100, 50, 20, 10, 5, 2, 1]:
    if notes[note] > 0:
        print(f"{note} rupees note: {notes[note]}")
