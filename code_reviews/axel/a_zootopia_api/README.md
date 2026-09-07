# My Zootopia - API 🦁

My Zootopia is a small Python application that fetches animal information from the **API Ninjas Animals API** and generates an HTML webpage displaying the results.

## Features

* Search for an animal by name
* Display the animal's diet, location, and type
* Generate an `animals.html` webpage from an HTML template
* Show a message when no animal is found
* Optional filtering by skin type

## Requirements

* `Python 3`
* `requests`
* `python-dotenv`
* `An API Ninjas API key`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your API key:

```text
API_KEY=your_api_key_here
```

## Usage

Run the application with:

```bash
python animals_web_generator.py
```

Enter the name of an animal when prompted. The generated webpage will be saved as `animals.html`.
