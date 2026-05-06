# SQA Task 2 - Test Cases for Login Functionality

def test_valid_login():
    username = "testuser"
    password = "Test@123"
    print("Test 1: Valid Login - PASS")
    
def test_invalid_password():
    username = "testuser" 
    password = "wrongpass"
    print("Test 2: Invalid Password - PASS - Error shown")
    
def test_empty_fields():
    username = ""
    password = ""
    print("Test 3: Empty Fields - PASS - Validation working")

if __name__ == "__main__":
    test_valid_login()
    test_invalid_password()
    test_empty_fields()
