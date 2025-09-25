# AI Medical Transcription

This project extracts medical information from transcriptions using OpenAI's GPT models. It processes medical transcriptions to extract patient age, treatments, and generates corresponding ICD codes.

## Features

- Extract patient age and treatment information from medical transcriptions
- Generate ICD codes for treatments using AI
- Process CSV files containing medical transcription data
- Structured output with medical specialties and ICD codes

## Requirements

- Python 3.10+
- OpenAI API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/AI-medical-transcription.git
cd AI-medical-transcription
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install pandas openai python-dotenv
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
api_key=your_openai_api_key_here
```

## Usage

1. Place your transcription data in a CSV file named `transcriptions.csv` with columns:
   - `medical_specialty`: The medical specialty
   - `transcription`: The transcription text

2. Run the script:
```bash
python main.py
```

The script will process each transcription and output structured data including:
- Patient age
- Treatment recommendations
- Medical specialty
- ICD codes

## File Structure

```
AI-medical-transcription/
├── main.py                 # Main processing script
├── transcriptions.csv      # Input data file
├── .env                   # Environment variables (API key)
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Important Notes

- Ensure you have sufficient OpenAI API quota before running
- The `.env` file containing your API key is excluded from version control for security
- Review and validate all extracted medical information before use in any clinical context

## License

This project is for educational and research purposes. Please ensure compliance with healthcare data regulations and OpenAI's usage policies.