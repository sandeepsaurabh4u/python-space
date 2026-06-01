# python-space

A small collection of Python example scripts and data-structure exercises used
for learning and quick utility tasks.

## Overview

This folder contains compact, self-contained Python scripts demonstrating
basic algorithms, data structures, and small utilities (OTP and password
generators). Each file is intended to be readable and easy to run directly
with the system Python interpreter.

## What's inside

- `otp-generator.py` — simple one-time-password (OTP) generator example
- `password-generator.py` — configurable random password generator
- `queue.py`, `queue-queue.py`, `queue-one.py`, `queue-collection.py` —
	queue implementations / experiments
- `priorityqueue.py` — minimal priority queue demo
- `stack.py` — simple stack implementation
- `LICENSE` — project license

## Requirements

- Python 3.8+

No external packages are required for the included examples — they use only
the standard library.

## Usage

Run any script directly with Python. Examples:

```bash
python otp-generator.py
python password-generator.py
python stack.py
```

If you want to reuse functions from these files inside another project,
import them as modules from this folder (for example, place this folder on
your `PYTHONPATH` or install it as a package for larger projects).

## Contributing

Small improvements and bug fixes are welcome. Open a PR with a clear title
and description of the change.

## License

See the `LICENSE` file for license details.

---

If you'd like, I can also:

- add usage examples to each script,
- add a small test or example runner, or
- create a `requirements.txt` / `pyproject.toml` if you plan to publish.

Tell me which of these you'd like next.
