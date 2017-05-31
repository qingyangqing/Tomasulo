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
# function: modify architectual reg
def modify_arch_reg(entry, reg_int, reg_fp):
    if entry.dest_tag[0] == 'F':
        reg_fp[int(entry.dest_tag[1:])] = entry.value
    elif entry.dest_tag[0] == 'R':
        reg_int[int(entry.dest_tag[1:])] = entry.value
    else:
        pass

# function: commit
def commit(ROB, reg_int, reg_fp, cycle, instructions):
    if len(ROB)>0:
        if instructions[ROB[0].PC].split(' ')[0]=='Bne':
            if len(ROB[0].exe)!=0:
                entry = ROB.popleft()
                print_ROB(entry, instructions)
        if (len(ROB)>0)&(instructions[ROB[0].PC].split(' ')[0]!='Bne'):
            if len(ROB[0].cdb)!=0: # broadcasted instructions
                ROB[0].commit.append(cycle+1)
                entry = ROB.popleft()
                modify_arch_reg(entry, reg_int, reg_fp)
                print_ROB(entry, instructions)
            elif len(ROB[0].commit)!=0: # Sd
                entry = ROB.popleft()
                print_ROB(entry, instructions)
                if len(ROB)>0:
                    if len(ROB[0].cdb)!=0: # broadcasted instructions
                        ROB[0].commit.append(cycle+1)
                        entry = ROB.popleft()
                        modify_arch_reg(entry, reg_int, reg_fp)
                        print_ROB(entry, instructions)
            else:
                pass

