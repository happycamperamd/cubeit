import pytest

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser to run in headed mode with slowmo"""
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,  # 500ms delay between actions
    }
