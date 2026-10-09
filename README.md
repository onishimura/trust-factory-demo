# trust-factory-demo

A small demo project for [trust-factory](https://github.com/onishimura/trust-factory). trust-factory builds its issues with agents, checks each PR with fixed checks and a verifier agent, and records each run.

pocketlib has small helpers for text, prices and durations. Python 3.9, standard library only.

Run the tests: `python3 -m unittest discover -s tests -v`

- `slugify(text)`: "Hello World" → "hello-world". Lowercase ASCII letters and digits, words joined with "-".
- `parse_price(text)`: "$12.50" → 1250 (cents).
- `format_price(cents)`: 1250 → "$12.50".
- `parse_duration(text)`: "1h30m" → 5400 (seconds). The units are h, m and s.
- `format_duration(seconds)`: 5400 → "1h 30m". Zero is "0s".

