import Lab2.bmi as bmi

def test_bmi_under_weight():
    #Arrange
    height = 1.73
    weight = 45
    #Act
    result = bmi.calculate_bmi(height, weight)
    #Assert
    assert result == -1

def test_bmi_normal_weight():
    #Arrange
    height = 1.73
    weight = 57
    #Act
    result = bmi.calculate_bmi(height, weight)
    #Assert
    assert result == 0

def test_bmi_normal_weight():
    #Arrange
    height = 1.73
    weight = 80
    #Act
    result = bmi.calculate_bmi(height, weight)
    #Assert
    assert result == 1

