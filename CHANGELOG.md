# CHANGELOG

A list of changes and developments in reverse chronological order. i.e. Newest version first

## v2025.07.10
- Added possibility to inject custom code into `head` section of HTML using `custom` metadata. It MUST be followed by a realtive path to file that stores the code to inject. 

## v2024.01.14
- Added a horizontal line to seperate body from footer on generated HTML files.
- Added `-a` or `--all` flag to reprocess all Markdown files regardless of the last run time of the `tiniest`
- Added `--dry-run` flag to run `tiniest` without any changes being persisted.

## v2023.12.29
- Initial release
- Generate HTML files from Markdown files
- Add `-d` or `--debug` to have verbose logs.
- Introduce `title` and `style` metadata