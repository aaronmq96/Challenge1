file_names = [
    "sample.1",
    "sample.2",
    "sample.3",
    "sample.4",
    "sample.5",
    "sample.6",
    "sample.7",
    "sample.8",
    "sample.9",
    "sample.10"
]

file_strings = {}

# readFiles
for i, name in enumerate(file_names):
    try:
        with open("Samples/"+name, "r", encoding='ISO-8859-1') as f:
            file_strings[i] = f.read()
    except IOError:
        print('Error While Opening the file:' + name)

# print(file_strings)

output = open("output.txt", "w", encoding='ISO-8859-1')


# Function to find the longest common strand


def lcs(file1, file2, m, n):

    mx_len = 0           # to store max length of longest common strand
    ending_index = m         # stores the ending index of LCS in `file1`

    # to store length of LCS in file1 &file 2
    dp = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if file1[i - 1] == file2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > mx_len:
                    mx_len = dp[i][j]
                    ending_index = i

    # return longest common strand having length `mx_len`
    return file1[ending_index - mx_len: ending_index]


longestCommon = ""
max_length = -1

for i in range(len(file_names)):
    name1 = file_names[i]
    for j in range(i):
        name2 = file_names[j]
        string1 = file_strings[i]
        string2 = file_strings[j]
        curr_lcs = lcs(string1, string2, len(string1), len(string2))
        if len(curr_lcs) > max_length:
            longestCommon = curr_lcs
            max_length = len(curr_lcs)

output.write(f"The maximum length is:  {max_length}")
output.write(f"The longest common strand is: {longestCommon}")

names = []
offsets = []

for name, string in file_strings.items():
    if longestCommon in string:
        names.append(name)
        offsets.append(string.find(longestCommon))

for i in range(len(names)):
    output.write(
        f"The offset in string {names[i]} is: {offsets[i]} characters")


output.close()
