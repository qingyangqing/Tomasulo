# Qing 
# 21st May 2017 

from collections import namedtuple

'''define data types'''
# reservation station 
def rs_entry():
    rs_entry = namedtuple('rs_entry', 'busy, op, tag_1st, value_1st, valid_1st, tag_2nd, value_2nd, valid_2nd, dest_tag')
    temp = rs_entry
    return temp 
# functional unit 
def fu_entry():
    fu_entry = namedtuple('fu_entry', 'cycle, op, value1, value2, dest_tag')
    temp = fu_entry
    return temp
# function result 
def fu_result():
    fu_result = namedtuple('fu_result', 'value, dest_tag')
    temp = fu_result
    return temp
# ld/sd entry
def ld_sd_entry():
    ld_sd_entry = namedtuple('ld_sd_entry', 'ld_sd_tag, ready, op, address, data, dest_tag, immediate, reg_tag, reg_value, valid')
    temp = ld_sd_entry
    return temp
# ld/sd exe
def ld_sd_exe():
    ld_sd_exe = namedtuple('ld_sd_exe', 'busy, cycle, value1, value2, dest_tag')
    temp = ld_sd_exe
    return temp
# ld/sd mem
def ld_sd_mem():
    ld_sd_mem = namedtuple('ld_sd_mem', 'busy, cycle, op, data, address, dest_tag')
    temp = ld_sd_mem
    return temp
# cdb
def cdb():
    cdb = namedtuple('cdb', 'valid, value, dest_tag')
    temp = cdb
    return temp
# ROB_entry 
def ROB_entry():
    ROB_entry = namedtuple('ROB_entry', 'ROB_tag, PC, value, dest_tag, issue, exe, mem, cdb, commit')
    temp = ROB_entry
    temp.issue = []
    temp.exe = []
    temp.mem = []
    temp.cdb = []
    temp.commit =[]
    return temp
# PC 
def PC():
    PC = namedtuple('PC', 'PC, valid')
    temp = PC
    return temp
# function: read instructions
def read_instruction(codefile):
    with open(codefile) as f:
            instructions = f.read().splitlines()
    return instructions
# function: build rs
def build_rs(num):
    rs = []
    for _ in range(num):
        temp = rs_entry()
        temp.busy = 0
        rs.extend([temp])
    return rs

