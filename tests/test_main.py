from src.main import main


def test_main_returns_expected_string():
    assert main() == "Claude Code starter is running."
