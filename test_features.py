import unittest

import fsext
from script import SeparatePage, get_absolute_from_current_path, treat_file
from tests.mock_separate_page import MockDisableSeparatePage


tc = unittest.TestCase()


def test_disabled_enable_debug() -> None:
    """Check that enable_debug=False works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_debug.png"),
    )
    treat_file(
        SeparatePage(),
        get_absolute_from_current_path(__file__, "0001_debug.png"),
        enable_debug=False,
    )
    fsext.delete_file(
        get_absolute_from_current_path(__file__, "0001_debug.png")
    )


def test_mock_stop_at_0() -> None:
    """Check that stop_at 0 works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_0.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_0.png_*")
    treat_file(
        MockDisableSeparatePage(0),
        get_absolute_from_current_path(__file__, "0001_0.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path(__file__, "0001_0.png"))
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_1_7.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_2_7.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_3_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_3_2.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_4_1_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_0.png_page_2.png")
        )
    )


def test_mock_stop_at_1() -> None:
    """Check that stop_at 1 works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_1.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_1.png_*")
    treat_file(
        MockDisableSeparatePage(1),
        get_absolute_from_current_path(__file__, "0001_1.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path(__file__, "0001_1.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_3_2.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_4_1_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_1.png_page_2.png")
        )
    )


def test_mock_stop_at_2() -> None:
    """Check that stop_at 2 works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_2.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_2.png_*")
    treat_file(
        MockDisableSeparatePage(2),
        get_absolute_from_current_path(__file__, "0001_2.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path(__file__, "0001_2.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_2.png_page_2.png")
        )
    )


def test_mock_stop_at_3() -> None:
    """Check that stop_at 3 works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_3.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_3.png_*")
    treat_file(
        MockDisableSeparatePage(3),
        get_absolute_from_current_path(__file__, "0001_3.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path(__file__, "0001_3.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_3.png_page_2.png")
        )
    )


def test_mock_stop_at_4() -> None:
    """Check that stop_at 4 works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_4.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_4.png_*")
    treat_file(
        MockDisableSeparatePage(4),
        get_absolute_from_current_path(__file__, "0001_4.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path(__file__, "0001_4.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_4_2_5.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_page_1.png")
        )
    )
    tc.assertFalse(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_4.png_page_2.png")
        )
    )


def test_mock_stop_at_5() -> None:
    """Check that stop_at 5 works."""
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001.png")
        )
    )
    fsext.copy_file(
        get_absolute_from_current_path(__file__, "0001.png"),
        get_absolute_from_current_path(__file__, "0001_5.png"),
    )
    fsext.del_pattern(fsext.extract_path(__file__), "0001_5.png_*")
    treat_file(
        MockDisableSeparatePage(5),
        get_absolute_from_current_path(__file__, "0001_5.png"),
        enable_debug=True,
    )
    fsext.delete_file(get_absolute_from_current_path(__file__, "0001_5.png"))
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_1_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_2_7.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_3_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_3_2.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_4_1_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_4_2_5.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_page_1.png")
        )
    )
    tc.assertTrue(
        fsext.is_file_exists(
            get_absolute_from_current_path(__file__, "0001_5.png_page_2.png")
        )
    )
