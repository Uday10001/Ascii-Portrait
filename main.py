def decode_line(line):
    if not line:
        return ""
    decoded = ""
    i = 0
    while i < len(line):
        char = line[i]
        i += 1
        count_str = ""
        while i < len(line) and line[i].isdigit():
            count_str += line[i]
            i += 1
        if count_str:
            count = int(count_str)
            decoded += char * count
    return decoded
def decode_file(file = "reference_encoded.txt"):
    lines = []
    with open(file, 'r') as f:
        lines = f.readlines()
    output = []
    for line in lines:
        output.append(decode_line(line.strip('\n')))
    for line in output:
        print(line)
decode_file()