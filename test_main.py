import main
import pytest

def test_add():
    assert main.add(3, 4) == 7
    assert main.add(1, 1) == 2
    assert main.add(-3, 7) == 4
    with pytest.raises(TypeError):
        assert main.add("truc", "machin")
    with pytest.raises(TypeError):
        assert main.add(5, "machin")