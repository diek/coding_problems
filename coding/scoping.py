# Define a global variable
global_number = 100


def access_global_number():
    """
    This function accesses the global_number without modifying it.
    """
    print(f"Inside access_global_number: {global_number}")


def modify_global_number():
    """
    This function modifies the global_number using the 'global' keyword.
    """
    global global_number  # Declare intent to modify the global variable
    global_number += 50
    print(f"Inside modify_global_number (after modification): {global_number}")


def create_local_variable():
    """
    This function creates a local var with the same name as the global var.
    It does not affect the global variable.
    """
    global_number = 25  # Creates a local variable, not mod the global
    print(f"Inside create_local_variable (local): {global_number}")


# Demonstrate global variable access
print(f"Initial global_number: {global_number}")
access_global_number()

# Demonstrate global variable modification
modify_global_number()
print(f"Global_number after modification: {global_number}")

# Demonstrate local variable creation with the same name
create_local_variable()
print(f"Global_number after loc var creation (unchanged): {global_number}")
