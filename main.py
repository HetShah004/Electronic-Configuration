class Shells:
    def __init__(self, pqm, aqm, azipri):
        self.principal_q_num = pqm
        self.azimuthal_q_num = aqm
        self.electrons = 0
        self.azi_pri = azipri


def electron_config(electrons):
    # An ordered list of element symbols
    element_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
    'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
    'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
    'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
    'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
    'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No','Lr','Rf']
    possible_principal_q_num = [1, 2, 3, 4, 5, 6] # WARNING: Changes must be done in order in possible_principal_q_num, possible_azimuthal_q_num, electron_capacity and element_symbols
    possible_azimuthal_q_num = ["s", "p", "d", "f"]
    electron_capacity = [2, 6, 10, 14, 18, 22]
    tmp = [] # "tmp" is a list of all shells (1s, 2s, 2p, ....)
    total_electrons = electrons
    # Making shells based on quantum numbers
    for x in possible_principal_q_num:
        for y in possible_azimuthal_q_num:
            if possible_azimuthal_q_num.index(y) < x: # Since an orbital(s or p or d....) can hold n-1 electrons, this condition ensures that it only select those orbitals whose index is lower than principal quantum number 
                tmp.append(Shells(x, y, x + possible_azimuthal_q_num.index(y)))


    # Sorting the shells in ascending order of energy (bubble sort)
    # Sorting the shells is important because shells must be in ascending order of energy
    for h in range(len(tmp) - 1):
        for i in range(0, len(tmp) - h - 1):
            if tmp[i].azi_pri == tmp[i + 1].azi_pri: # If azimuthal quantum number is same for two shells then compare principal quantum number
                if tmp[i].principal_q_num > tmp[i].principal_q_num:
                    tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
                    break
            elif tmp[i].azi_pri > tmp[i + 1].azi_pri:
                tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]


    # Filling electrons in shells
    # Note: Electron must be filled only after sorting
    for t in tmp:
        my_var = electron_capacity[possible_azimuthal_q_num.index(t.azimuthal_q_num)] # This line gets the capacity for respective orbitals
        if total_electrons <  my_var: # If electrons are less than available, then fit all electrons in the orbital
            t.electrons = total_electrons
            total_electrons -= total_electrons
            break
        t.electrons = my_var
        total_electrons -= my_var
    
    if total_electrons > 0: # Raise value error if all electrons are not filled (you can change values of possible_principal_q_num, possible_azimuthal_q_num, electron_capacity and element_symbols)
            raise ValueError("High value of electron is entered. Try lowering it. (Range: 1-104)")

    tmp_d = tmp.copy()

    for h in range(len(tmp_d) - 1):
        for i in range(0, len(tmp_d) - h - 1):
            if tmp_d[i].principal_q_num > tmp_d[i + 1].principal_q_num:
                tmp_d[i], tmp_d[i + 1] = tmp_d[i + 1], tmp_d[i]

    # Printing final result
    final_result = ""
    last_elec = ""
    final_result_ordered = "" 
    for g in range(len(tmp)): 
        last_elec = str(tmp[g - 1].principal_q_num) + str(tmp[g - 1].azimuthal_q_num)
        if tmp[g].electrons == 0:
            break
        final_result += str(tmp[g].principal_q_num) + str(tmp[g].azimuthal_q_num) + str(tmp[g].electrons) + '.'
    
    for u in range(len(tmp_d)):
        if tmp_d[u].electrons > 0:
            final_result_ordered += str(tmp_d[u].principal_q_num) + str(tmp_d[u].azimuthal_q_num) + str(tmp_d[u].electrons) + '.'
    
    return final_result, final_result_ordered, element_symbols[electrons - 1], last_elec


config, config_ordered, elem, last,  = electron_config(56)

print(f"Electron Configuration: {config}\nElectron Configuration(Ordered): {config_ordered}\nElement Symbol: {elem}\nLast electron was added in {last}")
