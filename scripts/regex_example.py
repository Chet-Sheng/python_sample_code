import re
input_file_name = "ic_ai.md"
output_file_name = "ic_ai_2.md"
with open(input_file_name, 'r') as input_file:
    with open(output_file_name, 'w') as output_file:
        lines = input_file.readlines()
        for line in lines:
            # print(line)
            output_file.write(re.sub(r'(\b\.\s\b)', r'.\n', line))
print("PS reformated")
