from reference_manual import color_codes_mapper


def test_reference_manual(color_code, zero_based_pair_number):
    color_codes = color_codes_mapper()
    assert (color_codes[zero_based_pair_number] == color_code)


def execute_tests():
    test_reference_manual([5, 'White', 'Slate'], 4)
    test_reference_manual([19, 'Yellow', 'Brown'], 18)
    test_reference_manual([25, 'Violet', 'Slate'], 24)
