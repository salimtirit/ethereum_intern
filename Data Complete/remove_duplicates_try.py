blocks_file_one = open('output_total_1.txt','r')
blocks_one = blocks_file_one.readlines()

total_blocks_one = list(dict.fromkeys(blocks_one))

print(len(blocks_one))
print(len(total_blocks_one))

blocks_file_two = open('output_total_2.txt','r')
blocks_two = blocks_file_two.readlines()

total_blocks_two = list(dict.fromkeys(blocks_two))

print(len(blocks_two))
print(len(total_blocks_two))

total_blocks = total_blocks_two + total_blocks_one

file = open('total_first_two.txt','a')
file.writelines(total_blocks)
file.close()


