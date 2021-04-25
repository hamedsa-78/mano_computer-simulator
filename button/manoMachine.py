
def run(obj_dict):
    keys = obj_dict.keys
    reg = {'SC': 0, 'AC': 0, 'DR' : 0, 'AR': 0, 'PC' : keys[0], 'IR' : 0, 'TR' :0, 'INPR':0, 'OUTR' :0}
    actions = []
    while (reg['PC'] in keys):
        reg['SC'] = 0

        actions.append(['SC_0', 'PC -> AR'])
        reg['AR'] = reg['PC']

        actions.append(['SC_1', 'M[AR] -> IR, PC + 1 -> PC'])
        reg['IR'] = obj_dict[reg['AR']]
        reg['PC'] += 1

        b = bin(reg['IR'])
        opcode = b[2:6]
        add = b[6:]
