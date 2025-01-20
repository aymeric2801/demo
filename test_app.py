from app import add

def test_add():
    assert add(2, 3) == 5  # This will pass
    assert add(12, 4) == 13  # Deliberate mistake to fail the test
