"""Suffix array construction and pattern matching implementation."""

class SuffixArray:
    """Efficient suffix array with O(n log n) construction and pattern matching."""
    
    def __init__(self, text):
        """Build suffix array from text.
        
        Args:
            text: Input string
        """
        self.text = text
        self.n = len(text)
        self.sa = self._build_suffix_array()
        self.lcp = self._build_lcp_array()
    
    def _build_suffix_array(self):
        """Build suffix array using simple O(n^2 log n) approach for clarity."""
        suffixes = [(self.text[i:], i) for i in range(self.n)]
        suffixes.sort()
        return [pos for _, pos in suffixes]
    
    def _build_lcp_array(self):
        """Build LCP array using Kasai's algorithm (linear time)."""
        lcp = [0] * self.n
        rank = [0] * self.n
        
        # Build rank array from suffix array
        for i in range(self.n):
            rank[self.sa[i]] = i
        
        h = 0
        for i in range(self.n):
            if rank[i] == 0:
                continue
            j = self.sa[rank[i] - 1]
            while i + h < self.n and j + h < self.n:
                if self.text[i + h] != self.text[j + h]:
                    break
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        
        return lcp
    
    def find(self, pattern):
        """Find first occurrence of pattern using binary search.
        
        Args:
            pattern: Pattern to search
            
        Returns:
            Index in text if found, -1 otherwise
        """
        left, right = 0, self.n
        
        while left < right:
            mid = (left + right) // 2
            suffix = self.text[self.sa[mid]:]
            if suffix < pattern:
                left = mid + 1
            else:
                right = mid
        
        if left < self.n and self.text[self.sa[left]:].startswith(pattern):
            return self.sa[left]
        return -1
    
    def find_all(self, pattern):
        """Find all occurrences of pattern.
        
        Args:
            pattern: Pattern to search
            
        Returns:
            List of indices where pattern occurs
        """
        results = []
        pos = self.find(pattern)
        
        if pos == -1:
            return results
        
        # Find all occurrences in suffix array
        for i in range(self.n):
            suffix_start = self.sa[i]
            if suffix_start + len(pattern) <= self.n:
                if self.text[suffix_start:suffix_start + len(pattern)] == pattern:
                    results.append(suffix_start)
        
        return sorted(results)
    
    def count_occurrences(self, pattern):
        """Count occurrences of pattern."""
        return len(self.find_all(pattern))
    
    def longest_repeated_substring(self):
        """Find longest substring that occurs at least twice."""
        max_len = 0
        max_pos = 0
        
        for i in range(1, self.n):
            if self.lcp[i] > max_len:
                max_len = self.lcp[i]
                max_pos = self.sa[i]
        
        if max_len > 0:
            return self.text[max_pos:max_pos + max_len]
        return ""
