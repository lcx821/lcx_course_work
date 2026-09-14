import pytest
from greetlab.cli import main


def test_blank_name_exits_with_code_2():
    with pytest.raises(SystemExit) as excinfo:
        main(["--name", "   "])
    assert excinfo.value.code == 2
