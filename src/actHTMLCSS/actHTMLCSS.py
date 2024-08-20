import os

# Creates necessary directories
def createDirs(dirs):
    if not os.path.isdir("css"):
            os.makedirs("css")
    for d in dirs:
        if not os.path.isdir("css/" + d):
            os.makedirs("css/" + d)


# Creates css-file file_name.css from list of (r,g,b) tuples for volume v, layer l, module m
# Note: css-files are opened with "a" so that the file can be written to out of order
# This means that if a css-file is not deleted before running the program again with the same data
# it will simply add the css data to the existing file a second time
def createCSS(file_name, colors, v, l):
    with open(file_name + ".css", "a") as f:
        for i in colors:
            start = "#module_vol" + str(v) + "_lay" + str(l) + "_sen" + str(i) + "{\n"
            fill = "    fill: rgb(" + str(colors[i][0]) + ", " + str(colors[i][1]) + ", " + str(colors[i][2]) + ") !important ;\n"
            opacity = "    fill-opacity: 0.75;\n"
            end = "}\n"
            f.write(start + fill + opacity + end)

# Creates the HTML-file from start and end text files in the source directory
# Includes an option for each volume layer combination from the data
def createHTML(VID, LID):
    with open("../src/htmlstart.txt", 'r') as file1:
        html_str_strart = file1.read()

    with open("../src/htmlend.txt", 'r') as file2:
        html_str_end = file2.read()

    # Create dict so every volume-layer combination appears only once
    options = {}
    for i in range(VID.size):
        for j in range(VID[i].size()):
            key = "vol_" + str(VID[i][j]) + "_layer_" + str(LID[i][j]) + "_modules"
            options[key] = 0

    # Finish writing HTML file
    option_string = ''
    for i in options:
        option_string = option_string + "        <option value=\"" + i + "\">" + i + "</option>\n"

    html_full = html_str_strart + option_string + html_str_end
    with open("index.html", "a") as h:
        h.write(html_full)
