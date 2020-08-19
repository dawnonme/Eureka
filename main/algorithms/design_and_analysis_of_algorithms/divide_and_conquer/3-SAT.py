from collections import defaultdict

class BoolVar:
    def __init__(self, id_num, rev, val):
        self.id = id_num
        self.rev = rev
        self.val = val

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return (self.id == other.id)

    def set_val(self, val):
        if val in [-1, 0, 1]:
            self.val = val
        else:
            print("Invalid value assignment!")

    def __str__(self):
        name = 'x' + str(self.id) + ': ' + str(self.val)
        if self.rev:
            name = '~' + name
        return name

    def __repr__(self):
        name = 'x' + str(self.id) + ': ' + str(self.val)
        if self.rev:
            name = '~' + name
        return name

class BoolSet:
    def __init__(self, bool_list):
        self.bool_list = bool_list

    def get_bool(self, var):
        for bool_var in self.bool_list:
            if var.id == bool_var.id:
                return bool_var
        return None
    def __getitem__(self, idx):
        return self.bool_list[idx]

    def __iter__(self, idx):
        yield self.bool_list[idx]


# def bool_set_finished(bool_set):
#     for bool_var in bool_sets:
#         if bool_var.val == 1:
#             return True
#     return False


# def boolean_assignment(bool_vars, bool_sets):
#     lookup = defaultdict(list)
#     for var in bool_vars:
#         for bool_set in bool_sets:
#             item = bool_set.get_bool(var)
#             if item is not None:
#                 lookup[var].append(bool_set)

# def _boolean_assignment(lookup, bool_vars, idx):
#     if idx == len(bool_vars):
#         return bool_vars
#     bool_var = bool_vars[idx]
#     bool_sets = [bs for bs in lookup[bool_var] if not bool_set_finished(bs)]

#     end_idx = min(idx + 4, len(bool_vars) - 1)
#     bool_vars_related = bool_vars[idx: end_idx + 1]    
        

def naive_helper(bool_vars, bool_sets):
    if not bool_vars:
        return []

    if not bool_sets:
        return [bool_vars]

    var = bool_vars[0]
    finished, unfinished, not_in = [], [], []
    for bs in bool_sets:
        bss = BoolSet(bs)
        bs_var = bss.get_bool(var)
        if bs_var is None:
            not_in.append(bs)
        elif not bs_var.rev:
            finished.append(bs)
        else:
            unfinished.append(bs)

    next_assignment1 = naive_helper(bool_vars[1:], unfinished + not_in)

    next_assignment2 = naive_helper(bool_vars[1:], finished + not_in)

    next_assignment3 = naive_helper(bool_vars[1:], finished + unfinished + not_in)

    ret = []

    for assign in next_assignment1:
        ret.append([BoolVar(var.id, False, 1)] + assign)

    for assign in next_assignment2:
        ret.append([BoolVar(var.id, False, -1)] + assign)

    for assign in next_assignment3:
        ret.append([BoolVar(var.id, False, 0)] + assign)

    return ret

if __name__ == '__main__':
    bool_vars = []
    for i in range(1, 6):
        bool_vars.append(BoolVar(i, False, 0))

    A1 = [BoolVar(1, False, 0), BoolVar(4, True, 0), BoolVar(3, False, 0)]
    A2 = [BoolVar(1, True, 0), BoolVar(5, False, 0), BoolVar(2, True, 0)]
    A3 = [BoolVar(1, False, 0), BoolVar(2, False, 0), BoolVar(4, False, 0)]
    A4 = [BoolVar(1, True, 0), BoolVar(3, True, 0), BoolVar(5, True, 0)]
    bool_sets = [A1, A2, A3, A4]

    print(naive_helper(bool_vars, bool_sets))

















