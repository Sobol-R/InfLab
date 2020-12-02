import string
from models import HintData


type_fib = "fib"
type_16 = "16"
type_3 = "3"

s_value_16 = 16
s_value_3 = 3

group1 = ['a', 'b', 'c', 'd', 'f', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v']
group2 = ['g', 'h', 'k', 'q', 'x', 'y', 'z']
group3 = ['e', 'j', 'w']

groups_ids_values = ['x', 'y', 'z']
groups_ids = {type_16: 'x', type_3: 'y', type_fib: 'z'}
groups_types = {'x': type_16, 'y': type_3, 'z': type_fib}

data10to16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
data16to10 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

char_type_error_mess = 'Char type should be determined'
num_base_error_mess = 'Wrong num base'
caught_error_mess = 'Caught this error: '

max_num_code_len = 8

process_key_values = [str(), str(), str(), str()]
process_word_values = [str(), str()]


def create_key(word):
    init_key_values()
    key = str()
    word = str(word).lower()
    for ch in word:
        key += create_char_code(ch)
    process_key_values[2] = key
    return key


def create_word(key):
    init_word_values()
    word = str()
    for i in range(0, len(key)):
        if key[i] in groups_ids_values:
            num_code = get_num_code(i+1, key)
            letter = decode_letter(num_code, key[i])
            word += letter
    process_word_values[1] = word
    return word


def get_key_hints():
    return HintData.create_key_hints(process_key_values)


def get_word_hints():
    return HintData.create_word_hints(process_word_values)


def decode_letter(code, group_id):
    t = groups_types[group_id]
    num = 0
    if t == type_16:
        num = from_s_to_10(code, s_value_16)
    elif t == type_3:
        num = from_s_to_10(code, s_value_3)
    elif t == type_fib:
        num = from_fib_to_10(code)
    process_word_values[0] += str(num) + " "
    return string.ascii_lowercase[num-1]


def get_num_code(i, key):
    res = str()
    while i < len(key) and key[i] not in groups_ids_values:
        res += key[i]
        i += 1
    return res


def create_char_code(char):
    num = string.ascii_lowercase.index(char) + 1
    process_key_values[0] += str(num) + " "
    t = get_char_type(char)
    code = str()
    if t == type_fib:
        code = create_num_fib_code(num)
    elif t == type_16:
        code = from_10_to_s(num, s_value_16)
    elif t == type_3:
        code = from_10_to_s(num, s_value_3)
    if not code:
        throw_value_error(char_type_error_mess)
    process_key_values[1] += code + " "
    code = groups_ids[t] + code
    return code


def get_char_type(char):
    if char in group1:
        return type_16
    elif char in group2:
        return type_3
    else:
        return type_fib


def get_type_value(t):
    if t == type_16:
        return s_value_16
    else:
        return s_value_3


def get_fib_nums(num):
    data = list()
    data.append(1)
    data.append(1)
    i = 1
    while data[i] + data[i-1] <= num:
        data.append(data[i] + data[i-1])
        i += 1
    del data[0]
    return data


def create_num_fib_code(num):
    data = get_fib_nums(num)
    code = str()
    var = 0
    for i in range(len(data) - 1, -1, -1):
        if var + data[i] <= num:
            var += data[i]
            code += "1"
        else:
            code += "0"
        i -= 1
    return code


def from_fib_to_10(num):
    res = 0
    num = num[::-1]
    data = get_fib_nums_by_cnt(len(num))
    for i in range(len(data)-1, -1, -1):
        if num[i] == "1":
            res += data[i]
    return res


def get_fib_nums_by_cnt(cnt):
    res = list()
    res.append(1)
    res.append(1)
    i = 1
    while len(res) != cnt+1:
        res.append(res[i] + res[i-1])
        i += 1
    del res[0]
    return res


def from_s_to_10(num, s):
    num = num[::-1]
    res = 0
    for i in range(0, len(num)):
        a = num[i]
        if a in data16to10:
            a = int(data16to10[a])
        else:
            a = int(a)
        res += a * pow(s, i)
    return res


def from_10_to_s(num, s):
    if not check_num_base(num, 10):
        return "-"
    res = ""
    var = num
    if 9 < num < 16 and s == s_value_16:
        var = data10to16[num]
    else:
        while var >= s:
            a = var % s
            if a > 9:
                a = data10to16[a]
            res += str(a)
            var //= s
    res += str(var)
    return res[::-1]


def check_num_base(num, s):
    var = num
    while var > 0:
        a = var % 10
        if a >= s:
            throw_value_error(num_base_error_mess + ": " + "num == " + str(a) + " base == " + str(s))
            return False
        var //= 10
    return True


def throw_value_error(message):
    try:
        raise ValueError(message)
    except Exception as error:
        print(caught_error_mess + repr(error))


def init_key_values():
    global process_key_values
    process_key_values = [str(), str(), str(), str()]


def init_word_values():
    global process_word_values
    process_word_values = [str(), str()]
