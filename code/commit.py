# Qing 
# 29th may 2017
'''
1. commit ROB_buffer
2. fetch header into ROB_buffer
'''

# function: print ROB entry 
def print_ROB(entry, instructions):
    item = instructions[entry.PC] + '  '
    item = item + str(entry.issue) + '  '
    item = item + str(entry.exe) + '  '
    item = item + str(entry.mem) + '  '
    item = item + str(entry.cdb) + '  '
    item = item + str(entry.commit) + '  '
    print (item)

# function: commit
def commit(ROB, ROB_buffer, reg_int, reg_fp, cycle, instructions):
    # commit ROB_buffer
    if len(ROB_buffer)>0:
        if ROB_buffer[0].dest_tag[0] == 'F':
            reg_fp[int(ROB_buffer[0].dest_tag[1:])] = ROB_buffer[0].value
            ROB_buffer[0].commit.append(cycle)
        elif ROB_buffer[0].dest_tag[0] == 'R':
            reg_int[int(ROB_buffer[0].dest_tag[1:])] = ROB_buffer[0].value
            ROB_buffer[0].commit.append(cycle)
        else:
            pass
        # print committed instruction
        print_ROB(ROB_buffer.popleft(), instructions) 
    # fetch header into ROB_buffer
    if len(ROB_buffer) == 0:
        if len(ROB)>0:
            # Sd instruction
            if (len(ROB[0].commit)!=0):
                print_ROB(ROB.popleft(), instructions)
                # next instruction after Sd
                if len(ROB)>0:
                    if (len(ROB[0].cdb)!=0):
                        ROB_buffer.append(ROB.popleft())
            else: # not Sd 
                if (len(ROB[0].cdb)!=0):
                    ROB_buffer.append(ROB.popleft())

