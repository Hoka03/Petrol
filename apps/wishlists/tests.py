def format_text(s, length):
    s = s.replace(" ,", ",")
    words = s.split()
    lines = []
    current_line = ""

    for word in words:
        if word[-1] == ",":
            if len(current_line) + len(word) <= length:
                current_line += word + " "
            else:
                lines.append(current_line.rstrip())
                current_line = word + " "
        else:
            if len(current_line) + len(word) <= length:
                current_line += word + " "
            else:
                lines.append(current_line.rstrip())
                current_line = word + " "

    if current_line:
        lines.append(current_line.rstrip())

    return '\n'.join(lines)

input_text = "once upon a time , in a land far far away lived a princess , whose beauty was yet unmatched"
max_word_length = max(len(word) for word in input_text.split())
length = max_word_length * 3
result = format_text(input_text, length)
print(result)

