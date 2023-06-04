import re

file_path = "links.txt"  # Path to the text file containing the download links
output_file = "links-output.txt"  # Path to the output file

pattern = r"https?://[^\s'\"]+"  # Regular expression pattern to match the download links

with open(file_path, "r") as file, open(output_file, "w") as output:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            if "put url here to ignore" not in match:
                print(match)
                output.write(match + "\n")

# Close the output file
output.close()
