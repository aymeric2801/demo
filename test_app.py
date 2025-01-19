from app import add

def test_add():
    assert add(2, 3) == 5  # This will pass
    assert add(12, 1) == 24  # Deliberate mistake to fail the test
