from playwright.sync_api import Page, expect
import pytest

def test_change_title(page):
    page.goto("http://localhost:8000")
    new_title = page.get_by_placeholder("Enter new title...")
    new_title.click()
    new_title.fill("Dave is Scared")
    page.get_by_role("button", name="Change Title").click()
    
    # Check that the H1 title on the page was updated
    page_title = page.locator("#pageTitle")
    expect(page_title).to_have_text("Dave is Scared")
    
    # Check that the browser tab title was updated
    expect(page).to_have_title("Dave is Scared")

def test_clear_title(page):
    page.goto("http://localhost:8000")
    new_title = page.get_by_placeholder("Enter new title...")
    new_title.click()
    new_title.fill("")
    page.get_by_role("button", name="Change Title").click()
    
    # Check that the H1 title on the page was updated
    page_title = page.locator("#pageTitle")
    expect(page_title).to_have_text("")
    
    # Check that the browser tab title was updated
    expect(page).to_have_title("")