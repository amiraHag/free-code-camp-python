fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#    count += 1
# print('The total number of lines in file:', count)

# ftext = fhand.read()
# print(len(ftext))
# print(ftext[:22])

# for line in fhand:
#     if line.startswith('From:'):
#         print(line, end='')

# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)


# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)


# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

# fname = input("Please enter file name: ").strip()
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith("Subject: "):
#         count += 1
# print("There is", count, "# of lines starts with Subject in the file")


fname = input("Please enter file name: ").strip()
try:
    fhand = open(fname)
except:
    print("File", fname, "can't be opened")
    quit()
count = 0
for line in fhand:
    if line.startswith("Subject: "):
        count += 1
print("There is", count, "# of lines starts with Subject in the file")