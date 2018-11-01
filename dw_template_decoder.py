from lookup_dict import skill_lookup_dictionary
from lookup_dict import profession_lookup
from lookup_dict import attribute_lookup


def template_decoder_func(x):
    coded_string = x
    decoded_array = []
    bit_decoded_array = []
    number_of_skills = 8

    b64_table = [
        ['A', 0],
        ['B', 1],
        ['C', 2],
        ['D', 3],
        ['E', 4],
        ['F', 5],
        ['G', 6],
        ['H', 7],
        ['I', 8],
        ['J', 9],
        ['K', 10],
        ['L', 11],
        ['M', 12],
        ['N', 13],
        ['O', 14],
        ['P', 15],
        ['Q', 16],
        ['R', 17],
        ['S', 18],
        ['T', 19],
        ['U', 20],
        ['V', 21],
        ['W', 22],
        ['X', 23],
        ['Y', 24],
        ['Z', 25],
        ['a', 26],
        ['b', 27],
        ['c', 28],
        ['d', 29],
        ['e', 30],
        ['f', 31],
        ['g', 32],
        ['h', 33],
        ['i', 34],
        ['j', 35],
        ['k', 36],
        ['l', 37],
        ['m', 38],
        ['n', 39],
        ['o', 40],
        ['p', 41],
        ['q', 42],
        ['r', 43],
        ['s', 44],
        ['t', 45],
        ['u', 46],
        ['v', 47],
        ['w', 48],
        ['x', 49],
        ['y', 50],
        ['z', 51],
        ['0', 52],
        ['1', 53],
        ['2', 54],
        ['3', 55],
        ['4', 56],
        ['5', 57],
        ['6', 58],
        ['7', 59],
        ['8', 60],
        ['9', 61],
        ['+', 62],
        ['/', 63],
    ]

    for x in coded_string:
        for y in b64_table:
            if x == y[0]:
                decoded_array.append(str(y[1]))

    for x in decoded_array:
        temp_decoded_binary = '{0:06b}'.format(int(x))
        bit_decoded_array.append(temp_decoded_binary)

    for index, x in enumerate(bit_decoded_array):
        bit_decoded_array[index] = x[::-1]

    bit_decoded_string = ''.join(bit_decoded_array)

    template_type = bit_decoded_string[:4][::-1]
    template_type_true = int(template_type, 2)

    version_number = bit_decoded_string[4:8][::-1]
    version_number_true = int(version_number, 2)

    profession_bits = bit_decoded_string[8:10][::-1]
    # A code controlling the number of encoded bits per profession id, decoded as follows: bits_per_profession_id = code * 2 + 4 (e.g. 0 = 4 bits per profession, 1 = 6 bits per profession, etc.)
    profession_bits_true = (int(profession_bits, 2) * 2) + 4

    primary_profession = bit_decoded_string[10:10 + profession_bits_true][::-1]
    primary_profession_true = int(primary_profession, 2)
    primary_profession_true = profession_lookup(primary_profession_true)

    secondary_profession = bit_decoded_string[10 + profession_bits_true:10 + (2 * profession_bits_true)][::-1]
    secondary_profession_true = int(secondary_profession, 2)
    secondary_profession_true = profession_lookup(secondary_profession_true)

    bit_to_start_from_attributes = 10 + (2 * profession_bits_true)

    count_of_attributes = bit_decoded_string[bit_to_start_from_attributes:bit_to_start_from_attributes + 4][::-1]
    count_of_attributes_true = int(count_of_attributes, 2)

    num_bits_per_attr = bit_decoded_string[bit_to_start_from_attributes + 4:bit_to_start_from_attributes + 8][::-1]
    # A code controlling the number of encoded bits per attribute id, decoded as follows: bits_per_attribute_id = code + 4
    num_bits_per_attr_true = int(num_bits_per_attr, 2) + 4

    bit_to_start_from_each_attr = bit_to_start_from_attributes + 8

    attributes = []
    attributes_true = []
    for x in range(0, count_of_attributes_true):
        attribute_id = bit_decoded_string[bit_to_start_from_each_attr + (x * num_bits_per_attr_true) + (x * 4):bit_to_start_from_each_attr + ((1 + x) * num_bits_per_attr_true) + (x * 4)][::-1]
        attribute_id_true = int(attribute_id, 2)

        attirbute_points = bit_decoded_string[bit_to_start_from_each_attr + ((1 + x) * num_bits_per_attr_true) + (x * 4):bit_to_start_from_each_attr + ((1 + x) * num_bits_per_attr_true) + (x * 4) + 4][::-1]
        attirbute_points_true = int(attirbute_points, 2)

        attributes.append([attribute_id_true, attirbute_points_true])
        bit_to_start_from_skill_bit_code = bit_to_start_from_each_attr + ((1 + x) * num_bits_per_attr_true) + (x * 4) + 4

    for x, y in attributes:
        attributes_true.append([attribute_lookup(x), y])

    bits_per_skill_id = bit_decoded_string[bit_to_start_from_skill_bit_code:bit_to_start_from_skill_bit_code + 4][::-1]
    # A code controlling the number of encoded bits per skill id, decoded as follows: bits_per_skill_id = code + 8
    bits_per_skill_id_true = int(bits_per_skill_id, 2) + 8

    skill_ids_start_bit = bit_to_start_from_skill_bit_code + 4

    skills = []
    skills_true = []
    for x in range(0, number_of_skills):
        skill_id = bit_decoded_string[skill_ids_start_bit + (bits_per_skill_id_true * x): skill_ids_start_bit + (bits_per_skill_id_true * (x + 1))][::-1]
        skill_id_true = int(skill_id, 2)
        skills.append(skill_id_true)
        skills_true.append(skill_lookup_dictionary(skill_id_true))

    return version_number_true, template_type_true, primary_profession_true, secondary_profession_true, attributes_true, skills_true
