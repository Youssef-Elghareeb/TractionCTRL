from project.base_reader import CustomObject
from project.advanced_reader import ExtendedCustomObject

def main():
    reader = CustomObject("text1.txt")
    print(reader)
    for line in reader:
        print(f"> {line}")

    r1 = ExtendedCustomObject("text1.txt")
    r2 = ExtendedCustomObject("text2.txt")
    merged = r1 + r2
    print(f"\nMerged file: {merged.filename}")
    for line in merged:
        print(line)

    r3 = ExtendedCustomObject("text2.txt")
    r4 = ExtendedCustomObject("extra.txt")
    combo = r1.concatenate(r3, r4, output_filename="combo.txt")
    print(f"\nCombo file: {combo.filename}")
    for line in combo:
        print(line)

if __name__ == "__main__":
    main()