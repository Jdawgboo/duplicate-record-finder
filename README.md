# Duplicate Record Finder

Find exact duplicate JSON-like records using canonical JSON SHA-256 fingerprints.

```bash
cat records.json | python tool.py
python -m unittest -v
```

Object key order does not affect fingerprints. This finds exact logical duplicates only; it does not perform fuzzy matching or entity resolution.
