
# Workout Tracker using Google Sheet

## Overview

This Python script integrates the Nutritionix API and Sheety API to log your exercise data into a Google Sheet. Users input their exercise details, and the script fetches calorie data, calculates duration, and logs the results in a spreadsheet with timestamps in the Asia/Manila timezone.

---

## Features

- **Exercise Data Analysis:** Utilizes Nutritionix's Natural Language Processing (NLP) API to analyze input exercise details and return calorie data.
- **Google Sheets Logging:** Uses Sheety API to save exercise data into a Google Sheet, including:
  - Date and time (formatted for Asia/Manila timezone)
  - Exercise description
  - Duration (minutes)
  - Calories burned
- **User Interaction:** Prompts for user inputs such as weight, height, and age.

---

## Prerequisites

### Environment Variables
Set the following environment variables in your system:
- `BEARER_TOKEN`: Your Sheety API Bearer Token for authentication.
- `APP_ID`: Nutritionix App ID.
- `APP_KEYS`: Nutritionix App Keys.

### Required APIs
1. **Nutritionix API**:
   - Provides exercise data analysis.
   - Register at [Nutritionix Developer Portal](https://developer.nutritionix.com/) for API keys.
2. **Sheety API**:
   - Enables Google Sheets integration.
   - Get started at [Sheety](https://sheety.co/).

---

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install requests pytz
   ```
3. Configure environment variables:
   - Set up `BEARER_TOKEN`, `APP_ID`, and `APP_KEYS` using a `.env` file or export them directly in your terminal.

---

## Usage

1. **Run the Script**:
   Execute the script in your terminal:
   ```bash
   python exercise_tracker.py
   ```
2. **Input Details**:
   The script prompts you for:
   - Exercise performed (e.g., "ran 5km").
   - Weight in kilograms.
   - Height in centimeters.
   - Age.

3. **Output**:
   - Exercise data is logged into your specified Google Sheet via Sheety API.
   - JSON response from the APIs is displayed in the terminal for debugging or verification.

---

## Code Explanation

### Key Components
1. **Date and Time Handling**:
   - Uses `pytz` to manage timezone and format date/time.
   ```python
   ph_now = pytz.timezone('Asia/Manila')
   date_in_ph = datetime.now(ph_now)
   formatted_date = date_in_ph.strftime("%d/%m/%Y")
   formatted_time = date_in_ph.strftime("%H:%M:%S")
   ```

2. **API Interaction**:
   - Sends a POST request to the Nutritionix API to analyze exercise data:
   ```python
   response_nutrition = requests.post(
       url=natural_exercise_endpoint,
       json=description_parameters,
       headers=headers
   )
   ```
   - Logs exercise data into Google Sheets via Sheety API:
   ```python
   response = requests.post(
       url=sheety_endpoint,
       json=sheets_params,
       headers=auth_headers
   )
   ```

3. **Error Handling**:
   - Raises exceptions if API calls fail:
   ```python
   response_nutrition.raise_for_status()
   ```

---

## Example Output

### User Input
```
Tell me what exercise you did today: ran 5km
Input your weight in kg: 70
Input your height in cm: 175
Input your age: 25
```

### Logged Data in Google Sheet
| Date       | Time     | Exercise | Duration (min) | Calories |
|------------|----------|----------|----------------|----------|
| 06/12/2024 | 08:30:00 | Ran      | 30             | 250      |

---

## Troubleshooting

1. **API Key Errors**:
   - Ensure `APP_ID`, `APP_KEYS`, and `BEARER_TOKEN` are correctly set.
2. **Invalid Input**:
   - Provide valid numerical inputs for weight, height, and age.
3. **Sheety API Authorization**:
   - Ensure the correct Bearer Token is configured.

---

## License

This script is open-source and available for personal or educational use. Commercial use or redistribution requires permission.
