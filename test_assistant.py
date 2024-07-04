import pytest
import FreeCAD
import assistant

def test_example():
    result = assistant.has_old_freecad_version()
    assert result == False
