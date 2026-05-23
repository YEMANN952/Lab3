import price_info
print("Test price info")
def test_total_cost_shopping():
    #Arrange
    expected_result=46.75
    #Act
    result=price_info.total_cost_shopping()
    #Assert
    assert result == expected_result
    
def test_cost_of_fruits():
    #Arrange
    fruit_name='apple'
    quantity = 5
    expected_result = 6.0
    #Act
    result=price_info.cost_of_fruits(fruit_name, quantity)
    #Assert
    assert result == expected_result