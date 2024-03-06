def generate_sequence_a():
    sequence_a = [1, 3, 5, 7]
    next_element = sequence_a[-1] + 2
    sequence_a.append(next_element)
    return sequence_a


def generate_sequence_b():
    sequence_b = [2, 4, 8, 16, 32, 64]
    next_element = sequence_b[-1] * 2
    sequence_b.append(next_element)
    return sequence_b


def generate_sequence_c():
    sequence_c = [0, 1, 4, 9, 16, 25, 36]
    next_element = sequence_c[-1] + 13
    sequence_c.append(next_element)
    return sequence_c


def generate_sequence_d():
    sequence_d = [4, 16, 36, 64]
    next_element = 4 * 32
    sequence_d.append(next_element)
    return sequence_d


def generate_sequence_e():
    sequence_e = [1, 1, 2, 3, 5, 8]
    next_element = sequence_e[-1] + sequence_e[-2]
    sequence_e.append(next_element)
    return sequence_e


def generate_sequence_f():
    sequence_f = [2, 10, 12, 16, 17, 18, 19]
    subt = sequence_f[-1] - sequence_f[-2]
    next_element = sequence_f[-1] + subt
    sequence_f.append(next_element)
    return sequence_f


sequence_a_result = generate_sequence_a()
print(f"A) {sequence_a_result }")

sequence_b_result = generate_sequence_b()
print(f"B) {sequence_b_result}")

sequence_c_result = generate_sequence_c()
print(f"C) {sequence_c_result}")

sequence_d_result = generate_sequence_d()
print(f"D) {sequence_d_result}")

sequence_e_result = generate_sequence_e()
print(f"E) {sequence_e_result }")

sequence_f_result = generate_sequence_f()
print(f"F) {sequence_f_result}")
