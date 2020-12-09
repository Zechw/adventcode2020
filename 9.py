
def find_first_error(input_text, preamble_length=25):
    nums = [int(x) for x in input_text.split("\n")]
    previous_numbers = [] # list of preamble_length previously seen numbers
    sum_window = [] # list of preamble_length-1! currently valid sums. removes & adds preamble_length-1 vals each cycle*(sum_drop)
    sum_drop = 0 # keeps track of how many sums to drop from the window
    for _ in range(preamble_length):
        # preamble
        n = nums.pop(0)
        for x in previous_numbers:
            sum_window.append(x + n)
        previous_numbers.append(n)
    # print("pre", previous_numbers, sum_window)
    # input()
    for n in nums:
        # print(n, nums)
        if n not in sum_window:
            return n
        # print("a", previous_numbers, sum_window)
        sum_drop = min(sum_drop + 1, preamble_length - 1)
        sum_window = sum_window[sum_drop:]
        previous_numbers.pop(0)
        # print("b", previous_numbers, sum_window)
        for x in previous_numbers:
            sum_window.append(x + n)
        previous_numbers.append(n)
        # print("c", previous_numbers, sum_window)
        # input()
    return False
