#probbably don't use this as an acutal password gen. It's just a fun excercise

import random as r
from time import perf_counter as t


class PwGen:
    UTF_map = {1: (33, 47),    # spec1
               2: (48, 57),    # dec
               3: (58, 64),    # spec2
               4: (65, 90),    # UC_alpha
               5: (91, 96),    # spec3
               6: (97, 122),   # lc_alpha
               7: (123, 126)}  # spec4

    def __init__(self):
        self.password = []
        self.type_list = []

    def gen_pass(self, pw_len):

        temp_list = [0, 0, 0, 0]
        last_num = -1
        i = 0
        while i <= pw_len:
            utf_num = r.randint(1, 7)
            if utf_num in (1, 3, 5, 7) and last_num not in (1, 3, 5, 7):
                temp_list[3] += 1
                self.password.append(self.get_char(utf_num))

            elif utf_num == 2 and utf_num != last_num:
                temp_list[0] += 1
                self.password.append(self.get_char(utf_num))

            elif utf_num == 4 and utf_num != last_num:
                temp_list[1] += 1
                self.password.append(self.get_char(utf_num))

            elif utf_num == 6 and utf_num != last_num:
                temp_list[2] += 1
                self.password.append(self.get_char(utf_num))
            else:
                i -= 1
            last_num = utf_num
            self.type_list = temp_list
            i += 1

    def get_char(self, i):
        """i : int in UTF_map"""
        f, g = self.UTF_map[i]
        return chr(r.randrange(f, g))

    def get_pass(self):
        return "".join(self.password)


if __name__ == "__main__":

    test_val = (4, 8, 16, 24)
    for k in test_val:
       
        t1 = t()
        gen = PwGen()
        gen.gen_pass(k)
        t2 = t()
        print("Password: " + gen.get_pass())
        print("Generation of {} letter password took {:.4f} seconds\n".format(k, t2-t1))
