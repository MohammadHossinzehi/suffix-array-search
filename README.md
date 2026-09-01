# Suffix Array Search

Efficient suffix array construction and fast pattern matching using suffix arrays and LCP (Longest Common Prefix) arrays.

## What It Does

This library provides production-grade implementations of:
- **Suffix Array Construction**: O(n log n) or O(n) time complexity suffix array building
- **LCP Array**: Linear-time LCP array computation using Kasai's algorithm
- **Pattern Matching**: Fast substring searching using the suffix array and binary search
- **Statistics**: Character frequency analysis and compression ratio metrics

## Why It's Useful

Suffix arrays are fundamental data structures used in:
- Bioinformatics (DNA sequence analysis)
- Text compression and indexing
- Full-text search engines
- Plagiarism detection
- Data deduplication

They offer better cache locality than suffix trees and require less memory while maintaining fast query times.

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Run the example
python examples/demo.py
```

## Design Decisions

1. **Language Choice**: Python for clarity and ease of implementation, with Cython optimizations available for performance-critical sections
2. **Algorithm**: Uses the DC3 algorithm for O(n) suffix array construction, with optional O(n log n) fallback
3. **LCP Computation**: Kasai's algorithm provides linear-time LCP array computation
4. **Pattern Search**: Binary search on sorted suffix array for O(log n * m) query time, where m is pattern length
5. **Testing**: Comprehensive unit tests with random string generation for validation

## Files

- `suffix_array.py` - Core suffix array implementation
- `lcp_array.py` - LCP array computation
- `pattern_matcher.py` - Pattern matching interface
- `tests/` - Unit tests with benchmarks
- `examples/` - Usage examples

## Example Usage

```python
from suffix_array import SuffixArray

text = "banana"
sa = SuffixArray(text)

# Find all occurrences of pattern
pattern = "ana"
matches = sa.find_all(pattern)
print(f"Pattern '{pattern}' found at positions: {matches}")
```

## Performance

- Construction: O(n log n) to O(n) depending on algorithm
- Pattern Search: O(log n + m + k) where k is number of matches
- Space: O(n) for suffix array and LCP array

## License

MIT License
