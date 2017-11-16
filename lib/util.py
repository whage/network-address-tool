def mask_to_prefix(mask):
    return sum([bin(int(x)).count('1') for x in mask.split('.')])