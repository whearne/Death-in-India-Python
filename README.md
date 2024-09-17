# Death in India Data Analysis Project ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
This project focuses on analyzing death statistics in India using Python. It involves data exploration and visualization to understand trends in population, birth rates, and death rates over time.

## Features
- Data loading and cleaning using pandas.
- Exploratory Data Analysis (EDA) on death statistics data, including:
    - Displaying data summary and structure.
    - Visualising distributions of numerical data using histograms.
- Visualisation of trends in population, birth rates, and death rates using line plots.
- Utilises matplotlib and seaborn for data visualisation.

## Getting Started
### Prerequisites
- Python 3.x
- Required libraries: pandas, matplotlib, numpy, seaborn

You can install the required libraries using the following command:

pip install pandas matplotlib numpy seaborn
### Installation
1. Clone the repository or download the script directly:

    git clone https://github.com/whearne/death-in-india-python.git

2. Navigate to the project directory:


    cd death-in-india

3. Ensure you have the necessary CSV files (Deathdata.csv and rate.csv) in the same directory as the script.

### Usage
1. Open the script (Death in India.py) in your code editor.

2. Update the file paths for the datasets (Deathdata.csv and rate.csv) in the script if they are located in different directories:

    df = pd.read_csv('path/to/Deathdata.csv')
    rate = pd.read_csv('path/to/rate.csv')

3. Run the script to perform the analysis:

   python Death\ in\ India.py

4. The script will display data summaries and visualisations, including:

      - Histograms of numerical columns in the dataset.
      - Line plots showing trends in population, birth rates, and death rates over time.

### Visualisations

- **Histograms**: Display distributions of various numerical columns in the death data.
- **Line Plots**: Show population changes and trends in birth and death rates over the years.
### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments
- This project utilises the pandas library for data processing.
- Visualisations are created using matplotlib and seaborn.
