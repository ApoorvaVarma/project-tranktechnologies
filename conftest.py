import base64
from pathlib import Path

import pytest
from pytest_html import extras
from playwright.sync_api import sync_playwright
from config import base_url


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def page(request, browser):
    videos_dir = Path("videos")
    videos_dir.mkdir(exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        record_video_dir=str(videos_dir),
    )
    page = context.new_page()

    try:
        page.goto(base_url)
        page.wait_for_load_state("load")
        yield page
    finally:
        context.close()
        if page.video is not None:
            request.node._video_path = Path(page.video.path())


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    report_extras = list(getattr(report, "extras", []))

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            file_name = screenshots_dir / f"{item.name}.png"

            page.screenshot(path=str(file_name))

            report_extras.append(extras.image(str(file_name)))

    if report.when == "teardown":
        video_path = getattr(item, "_video_path", None)
        if video_path is not None:
            video_content = base64.b64encode(video_path.read_bytes()).decode("ascii")
            report_extras.append(
                extras.video(
                    video_content,
                    name="Execution video",
                    mime_type="video/webm",
                    extension="webm",
                )
            )

    if report_extras:
        report.extras = report_extras
