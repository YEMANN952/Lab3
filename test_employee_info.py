import employee_info
print ("Test_employee_info")

def test_get_employees_by_age_range():
    #Arrange
    expeted_result=[
         {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    #Act
    result = employee_info.get_employees_by_age_range(25,35)
    #Assert
    assert result == expeted_result

def test_calculate_average_salary():
    #Arrange
    except_result=60166.666666666664
    #Act
    result = employee_info.calculate_average_salary()
    #Assert
    assert result ==  except_result

def test_get_employees_by_dept():
    #Arrange
    excepted_result=[
         {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
         {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    #Act
    result = employee_info.get_employees_by_dept('Sales')
    #Assert
    assert result == excepted_result
