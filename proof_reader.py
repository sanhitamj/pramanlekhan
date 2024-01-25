from replace import EDITS

infile = "sample.txt"
outfile = infile.replace(".txt", "_edited.txt")

with open(infile, "r") as file:
    text = file.read()

for wrong, right in EDITS.items():
    text = text.replace(wrong, right)

with open(outfile, "w") as file:
    file.write(text)
