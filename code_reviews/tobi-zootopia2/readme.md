# Zootopia2 🦁

A small Python CLI tool that fetches animal data from the [API Ninjas Animals API](https://api-ninjas.com/api/animals), lets you optionally filter results by skin type, and renders the results as HTML cards injected into a template page.

## Features

- Search animals by name via the API Ninjas Animals API
- Automatic retry on intermittent connection errors
- Optional filtering by skin type
- Generates a static `animals_template.html` page with styled animal cards
- Generic nested-dict search utility for pulling fields out of deeply nested JSON

## Requirements

- Python 3.10+
- An [API Ninjas](https://api-ninjas.com/) API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/zootopia2.git
   cd zootopia2
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your API key:
   ```
   API_KEY=your_api_ninjas_key_here
   ```

## Usage

Run the generator:

```bash
python animals_web_generator.py
```

You'll be prompted to enter an animal name. Matching results are fetched from the API, and you'll have the option to filter them by skin type. The finished page is saved as `animals_template.html` in the project root — open it in your browser to view it.

## Project Structure

```
.
├── animals_web_generator.py      # Entry point / orchestration
├── config.py                     # API and file path configuration
├── data_fetcher.py                # API requests with retry logic
├── file_handler.py                # Template loading and saving
├── get_from_nested_object.py     # Generic nested dict/list search utility
├── helpers.py                    # User input and misc helpers
├── html_constructor.py           # HTML card generation
├── animals_template_orig_backup.html   # Base HTML template
└── .env                           # API key (not committed)
```

## License

This project is licensed under the MIT License.