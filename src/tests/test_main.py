# Test cases

def test_version():
    from app.utils.helpers import get_version
    assert get_version() == '0.1.0'
