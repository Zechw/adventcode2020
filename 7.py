from collections import defaultdict
import re

def eventually_contains(target_bag, input_string):
    rule_map = parse_input(input_string)
    contained_in_map = build_contained_in_map(rule_map)
    found = set()
    checked = set()
    recursively_check_contains(target_bag, contained_in_map, found, checked)
    return found

def count_contained(bag, input_string):
    rule_map = parse_input(input_string)
    return recursively_count_bags(bag, rule_map, {})



def parse_input(input_string):
    rule_map = {}
    for rule_string in input_string.split("\n"):
        bag, rules = parse_rule(rule_string)
        rule_map[bag] = rules
    return rule_map

def parse_rule(rule_string):
    bag, rules_string = rule_string.split(" bags contain", 1)
    return (bag, re.findall(" (\d+) ([\w ]+) bag", rules_string))


def build_contained_in_map(rule_map):
    """converts a mapping of bags and what they contain -- rulemap: bag => [(#, bag),]
    to a mapping of bags and what they are contianed in -- contains_map: bag => set(bag,)
    """
    contained_in_map = defaultdict(set)
    for parent_bag, children in rule_map.items():
        for _, child_bag in children:
            contained_in_map[child_bag].add(parent_bag)
    return contained_in_map

def recursively_check_contains(target_bag, contained_in_map, found, checked):
    """mutates found"""
    if target_bag in checked or target_bag not in contained_in_map:
        # already checked (or) no bags hold this bag
        return
    checked.add(target_bag)
    for bag in contained_in_map[target_bag]:
        found.add(bag)
        if bag not in checked:
            recursively_check_contains(bag, contained_in_map, found, checked)

def recursively_count_bags(target_bag, rule_map, known_counts):
    if target_bag not in rule_map:
        return 0
    total_count = 0
    for num, bag in rule_map[target_bag]:
        if bag not in known_counts:
            known_counts[bag] = recursively_count_bags(bag, rule_map, known_counts)
        total_count += int(num) * (known_counts[bag] + 1) # counting itself
    return total_count
