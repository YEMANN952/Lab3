import Lab2.bmi as bmi

def test_bmi_under_weight():
    result, category = bmi.calculate_bmi(45, 1.7)
    assert category == -1


def test_bmi_normal_weight():
    result, category = bmi.calculate_bmi(65, 1.7)
    assert category == 0


def test_bmi_over_weight():
    result, category = bmi.calculate_bmi(85, 1.7)
    assert category == 1