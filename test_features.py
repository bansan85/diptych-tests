import unittest

from diptych.debug_image import DebugImage
from diptych.fsext import (
    copy_file,
    del_pattern,
    delete_file,
    extract_path,
    get_absolute_from_current_path,
    is_file_exists,
)
from diptych.script import SeparatePage
from .mock_separate_page import MockDisableSeparatePage

tc = unittest.TestCase()


def test_disabled_enable_debug() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_debug.png"),
    )
    SeparatePage().treat_file(
        get_absolute_from_current_path(__file__, "0001_debug.png"),
        debug=DebugImage(DebugImage.Level.OFF),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_debug.png"))


def test_mock_stop_at_0() -> None:
    """Check that stop_at 0 works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_0.png"),
    )
    del_pattern(extract_path(__file__), "0001_0.png_*")
    MockDisableSeparatePage(0).treat_file(
        get_absolute_from_current_path(__file__, "0001_0.png"),
        debug=DebugImage(DebugImage.Level.TOP),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_0.png"))
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_1_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_2_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_3_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_3_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_4_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_5_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_6_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_6_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_7_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_7_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_page_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_page_2.png")
        )
    )


def test_mock_stop_at_1() -> None:
    """Check that stop_at 1 works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_1.png"),
    )
    del_pattern(extract_path(__file__), "0001_1.png_*")
    MockDisableSeparatePage(1).treat_file(
        get_absolute_from_current_path(__file__, "0001_1.png"),
        debug=DebugImage(DebugImage.Level.TOP),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_1.png"))
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_1_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_2_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_3_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_3_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_4_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_5_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_6_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_6_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_7_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_7_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_page_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_page_2.png")
        )
    )


def test_mock_stop_at_2() -> None:
    """Check that stop_at 2 works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_2.png"),
    )
    del_pattern(extract_path(__file__), "0001_2.png_*")
    MockDisableSeparatePage(2).treat_file(
        get_absolute_from_current_path(__file__, "0001_2.png"),
        debug=DebugImage(DebugImage.Level.TOP),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_2.png"))
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_1_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_2_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_3_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_3_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_4_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_5_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_6_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_6_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_7_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_7_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_page_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_page_2.png")
        )
    )


def test_mock_stop_at_3() -> None:
    """Check that stop_at 3 works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_3.png"),
    )
    del_pattern(extract_path(__file__), "0001_3.png_*")
    MockDisableSeparatePage(3).treat_file(
        get_absolute_from_current_path(__file__, "0001_3.png"),
        debug=DebugImage(DebugImage.Level.TOP),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_3.png"))
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_1_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_2_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_3_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_3_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_4_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_5_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_6_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_6_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_7_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_7_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_page_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_page_2.png")
        )
    )


def test_mock_stop_at_4() -> None:
    """Check that stop_at 4 works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_4.png"),
    )
    del_pattern(extract_path(__file__), "0001_4.png_*")
    MockDisableSeparatePage(4).treat_file(
        get_absolute_from_current_path(__file__, "0001_4.png"),
        debug=DebugImage(DebugImage.Level.TOP),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_4.png"))
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_1_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_2_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_3_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_3_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_4_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_5_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_6_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_6_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_7_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_7_2.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_page_1.png")
        )
    )
    tc.assertFalse(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_page_2.png")
        )
    )


def test_mock_stop_at_5() -> None:
    """Check that stop_at 5 works."""
    tc.assertTrue(
        is_file_exists(get_absolute_from_current_path(__file__, "0001.png"))
    )
    copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_5.png"),
    )
    del_pattern(extract_path(__file__), "0001_5.png_*")
    MockDisableSeparatePage(5).treat_file(
        get_absolute_from_current_path(__file__, "0001_5.png"),
        debug=DebugImage(DebugImage.Level.TOP),
    )
    delete_file(get_absolute_from_current_path(__file__, "0001_5.png"))
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_1_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_2_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_3_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_3_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_4_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_5_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_6_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_6_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_7_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_7_2.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_page_1.png")
        )
    )
    tc.assertTrue(
        is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_page_2.png")
        )
    )
