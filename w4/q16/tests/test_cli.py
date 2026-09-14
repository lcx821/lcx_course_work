import pytest
from greetlab.cli import main


def test_normal_name(capsys, monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, Alice!\n"


def test_blank_name_exits_with_2(monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 2
