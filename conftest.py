import pytest
import os

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser to run in headed mode with slowmo (headless in CI)"""
    # Run headless in CI (GitHub Actions), headed locally
    is_ci = os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true"
    return {
        **browser_type_launch_args,
        "headless": is_ci,  # Headless in CI, headed locally
        "slow_mo": 500 if not is_ci else 0,  # Slowmo only when headed (local)
    }
