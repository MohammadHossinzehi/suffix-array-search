"""Unit tests for suffix array implementation."""

import unittest
from suffix_array import SuffixArray


class TestSuffixArray(unittest.TestCase):
    """Test suffix array construction and operations."""
    
    def test_basic_construction(self):
        """Test basic suffix array construction."""
        sa = SuffixArray("banana")
        self.assertIsNotNone(sa.sa)
        self.assertEqual(len(sa.sa), 6)
    
    def test_find_single_occurrence(self):
        """Test finding single occurrence."""
        sa = SuffixArray("hello world")
        pos = sa.find("world")
        self.assertEqual(pos, 6)
    
    def test_find_not_found(self):
        """Test pattern not found."""
        sa = SuffixArray("hello world")
        pos = sa.find("xyz")
        self.assertEqual(pos, -1)
    
    def test_find_all_occurrences(self):
        """Test finding all occurrences."""
        sa = SuffixArray("banana")
        matches = sa.find_all("ana")
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches, [1, 3])
    
    def test_count_occurrences(self):
        """Test counting occurrences."""
        sa = SuffixArray("mississippi")
        count = sa.count_occurrences("i")
        self.assertEqual(count, 4)
    
    def test_longest_repeated_substring(self):
        """Test longest repeated substring."""
        sa = SuffixArray("abcabcabc")
        lrs = sa.longest_repeated_substring()
        self.assertTrue(len(lrs) >= 2)
    
    def test_empty_string(self):
        """Test empty string handling."""
        sa = SuffixArray("")
        self.assertEqual(len(sa.sa), 0)
    
    def test_single_character(self):
        """Test single character."""
        sa = SuffixArray("a")
        self.assertEqual(len(sa.sa), 1)
    
    def test_repeated_characters(self):
        """Test repeated characters."""
        sa = SuffixArray("aaaa")
        matches = sa.find_all("aa")
        self.assertEqual(len(matches), 3)
    
    def test_complex_text(self):
        """Test with more complex text."""
        text = "The quick brown fox jumps over the lazy dog"
        sa = SuffixArray(text)
        matches = sa.find_all("the")
        self.assertGreaterEqual(len(matches), 1)


class TestLCPArray(unittest.TestCase):
    """Test LCP array construction."""
    
    def test_lcp_construction(self):
        """Test LCP array is constructed."""
        sa = SuffixArray("banana")
        self.assertIsNotNone(sa.lcp)
        self.assertEqual(len(sa.lcp), 6)
    
    def test_lcp_first_element_zero(self):
        """Test first LCP element is always zero."""
        sa = SuffixArray("mississippi")
        self.assertEqual(sa.lcp[0], 0)


if __name__ == "__main__":
    unittest.main()
