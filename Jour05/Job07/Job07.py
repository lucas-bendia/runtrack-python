def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40:
            # Calculer le prochain multiple de 5
            prochain_multiple = (note // 5 + 1) * 5
            # Si la note est à moins de 3 points du prochain multiple de 5, l'arrondir
            if prochain_multiple - note < 3:
                notes_arrondies.append(prochain_multiple)
            else:
                notes_arrondies.append(note)
        else:
            notes_arrondies.append(note)  # Les notes inférieures à 40 ne sont pas arrondies
    return notes_arrondies

# Exemple d'utilisation :
notes = [39, 58, 84, 85, 86, 48, 88, 89, 90]
print(arrondir_notes(notes))
