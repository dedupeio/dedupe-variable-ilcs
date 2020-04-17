# dedupe-variable-ilcs

Dedupe variable for Illinois Compiled Statute (ILCS) codes.

Part of the [Dedupe.io](https://dedupe.io/) cloud service and open source toolset for de-duplicating and finding fuzzy matches in your data.

## Installation

Install with `pip`:

```
pip install git+https://github.com/dedupeio/dedupe-variable-ilcs.git
```

## Development

Local development requires an installation of Python.

Install development requirements:

```
pip install -e .[tests]
```

Train the `ilcs_parser` model:

```
parserator train training/labeled.xml ilcs_parser
```

The variable should now be ready to use.

### Running tests

Run the tests:

```
pytest
```

All tests should pass.
