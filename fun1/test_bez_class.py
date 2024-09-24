from czy_rowne import czy_sa_rowne

def test_True():
    print(f"module name z inn: {__name__}")
    # Expect the first and last elements (30 and 30) to be equal, so it should return True
    assert czy_sa_rowne([30, 65, 35, 75, 30]) == True, 'First and last elements should be equal'


def test_False():
    # Expect the first and last elements (30 and 40) to be unequal, so it should return False
    assert czy_sa_rowne([40, 65, 35, 75, 30]) == False, 'First and last elements should not be equal'


def test_both_str_numeric_notEqual():
    assert czy_sa_rowne(['30', 65, 35, 75, '40']) == False, 'First and last elements are numeric strings and should NOT be equal'



test_True()
test_False()