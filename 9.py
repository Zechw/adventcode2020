parse_nums = lambda inp: [int(x) for x in inp.split("\n")]

def find_first_error(input_text, preamble_length=25):
    nums = parse_nums(input_text)
    previous_numbers = [] # list of preamble_length previously seen numbers
    sum_window = [] # list of preamble_length-1! currently valid sums. removes & adds preamble_length-1 vals each cycle*(sum_drop)
    sum_drop = 0 # keeps track of how many sums to drop from the window
    for _ in range(preamble_length):
        # preamble
        n = nums.pop(0)
        for x in previous_numbers:
            sum_window.append(x + n)
        previous_numbers.append(n)
    for n in nums:
        if n not in sum_window:
            return n
        sum_drop = min(sum_drop + 1, preamble_length - 1)
        sum_window = sum_window[sum_drop:]
        previous_numbers.pop(0)
        for x in previous_numbers:
            sum_window.append(x + n)
        previous_numbers.append(n)
    return False


def find_consecutive_sums(input_text, target):
    nums = parse_nums(input_text)
    sum_window = []
    current_sum = 0
    while True:
        if current_sum > target:
            current_sum -= sum_window.pop(0)
        elif current_sum < target:
            x = nums.pop(0)
            current_sum += x
            sum_window.append(x)
        elif current_sum == target:
            return min(sum_window) + max(sum_window)
