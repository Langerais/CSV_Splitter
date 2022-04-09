import os
import csv
import random
import sys

#
#   Takes ',' delimited .csv from 'IN' folder. / Loops through every file in the folder
#   Splits it randomly to 2 .csv according to provided share
#   Saves in 2 separate files in the 'OUT' folder
#   Share can be passed as cmd argument or, if not provided, prompts for share. If left blank - set to default

in_folder = os.path.join('./IN/')
out_folder = os.path.join('./OUT/')

filenum = 0  # Num of file in the IN folder for output naming
share = 20  # Default share

if len(sys.argv) > 1:
    shareInp = sys.argv[1]
    if shareInp.isnumeric() and 0 <= int(shareInp) <= 100:
        share = int(shareInp)
    else:
        print("Invalid share argument / Default: Share = 20")
else:
    print("Leave BLANK for default of 20")
    inp = input("Provide the share (0-100) for Share list: ")
    if inp.isnumeric() and 0 <= int(inp) <= 100:
        share = int(inp)
    else:
        print("Invalid share argument / Set to default: " + str(share) + "%")


def check_random():
    return random.randint(0, 100) < share


def count_lines(file_to_count):
    fcr = open(file_to_count, 'rb')
    for count, line in enumerate(fcr):
        pass
    fcr.close()
    return count


for file in os.listdir(in_folder):
    filenum += 1
    fullpath = os.path.join(in_folder, file)
    lines = count_lines(fullpath)

    body_file = open(out_folder + '/splitFile_Body_' + str(filenum) + '.csv', 'w', encoding='UTF8')
    share_file = open(out_folder + '/splitFile_Share_' + str(filenum) + '.csv', 'w', encoding='UTF8')

    body_len = 0
    share_len = 0

    fh = open(fullpath, 'r')
    reader = csv.reader(fh)
    index = 0

    for row in reader:

        writer_body = csv.writer(body_file, lineterminator='\n')
        writer_share = csv.writer(share_file, lineterminator='\n')

        newline = row
        rnd = check_random()
        if index == 0:
            writer_body.writerow(newline)
            writer_share.writerow(newline)
        elif share_len > lines * share or not rnd:
            writer_body.writerow(newline)
            body_len += 1
        else:
            writer_share.writerow(newline)
            share_len += 1
        index += 1

    print("File_" + str(filenum) + ": " + str(lines) + "\t|\tBody: " + str(body_len) + "\t|\tShare: " + str(
        share_len) + "\t|")
    print("Shares:\t100 %\t|\t\t" + str(round(body_len / lines * 100, 2)) + " %\t|\t\t" + str(
        round(share_len / lines * 100, 2)) + " %\t|")
    fh.close()
    body_file.close()
    share_file.close()
