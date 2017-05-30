# Qing 
# 21st May 2017

# function: print RS/ROB status
def ps(unit):
    if(len(unit)==0):
        print('empty!')
    else:
        # get all fields in namedtuple
        fields_list = unit[0]._fields
        for unit_item in unit:
            print ('******')
            for field in fields_list:
                print(field+': ', str(getattr(unit_item, field)))

# function: print single namedtuple
def pss(snt):
    fields_list = snt._fields
    for field in fields_list:
        print (field+': ', str(getattr(snt, field)))

