notes = [0] * 10  # създаваме лист с 10 елемента.    input-> 2-Walk the dog ///  1-drink coffie

while True:
    command = input()
    if command == "End":
        break
    split_notes = command.split("-")  # split the Command by (-) into a new list , so that we can reach each element
    priority = int(
        split_notes[0]) - 1  # за да ползваме и индекс 0 в листа -- ако 1 да стане 0 и да селожи на индекс 0 с pop()
    note = split_notes[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)


# Solution 2
def process_notes():
    to_do_notes = []
    while True:
        note = input()

        if note == "End":
            break

        to_do_notes.append(note)

    sorted_notes = sorted(to_do_notes, key=lambda x: int(
        x.split("-")[0]))  # Сортираме на база на числата от ноте, които са на индекс 0
    return [note.split("-")[1] for note in
            sorted_notes]  # връщаме само текста , без числата.. тоест на индекс 1 от целия ноут


result = process_notes()
print(result)
