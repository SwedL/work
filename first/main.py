

def parse_ranges(ranges):
    generator_ranges = ranges.split(',')
    return generator_ranges


print(*parse_ranges('1-2,4-4,8-10'))