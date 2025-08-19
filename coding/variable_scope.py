# Global scope
GLOBAL_VAR = "I am global"


# Built-in scope test
def test_builtin_scope():
    assert isinstance(len([1, 2, 3]), int)
    print("✅ Built-in scope works: len is globally available")


def test_global_scope():
    assert GLOBAL_VAR == "I am global"
    print("✅ Global scope works: GLOBAL_VAR is accessible in functions")


# Local scope
def test_local_scope():
    def inner():
        local_var = "I am local"
        return local_var
    result = inner()
    assert result == "I am local"
    print("✅ Local scope works: local_var is accessible only in inner()")


# Enclosing scope (nonlocal)
def test_nonlocal_scope():
    message = "original"

    def outer():
        msg = "outer"

        def inner():
            nonlocal msg
            msg = "modified in inner"
        inner()
        return msg

    modified = outer()
    assert modified == "modified in inner"
    print("✅ Nonlocal scope works: inner() modified outer() variable")


# Shadowing global variable locally
def test_shadowing():
    var = "outer"

    def inner():
        var = "inner"
        return var

    assert var == "outer"
    assert inner() == "inner"
    print("✅ Shadowing works: local var hides outer/global one")


# Trying to access local variable outside its scope (should raise NameError)
def test_local_scope_isolation():
    try:
        def inner():
            temp = "only here"
        inner()
        print(temp)  # This should fail
    except NameError:
        print("✅ Local scope isolation works: cannot access temp outside inner()")


# Run all tests
if __name__ == "__main__":
    test_builtin_scope()
    test_global_scope()
    test_local_scope()
    test_nonlocal_scope()
    test_shadowing()
    test_local_scope_isolation()
