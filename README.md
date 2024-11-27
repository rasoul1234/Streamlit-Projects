# The Machine Learning Algorithm Comparison App - README

## Project Overview

This project is a **Streamlit-based web application** designed to compare the performance of various machine learning algorithms using the `lazypredict` library. It provides an intuitive interface for users to upload datasets, adjust model parameters, and visualize the performance metrics of multiple regression models.

---

## Features

1. **Upload and Analyze Data:**
   - Supports CSV file uploads.
   - Provides a preview of the uploaded dataset and its structure.

2. **Automated Machine Learning Modeling:**
   - Uses the `LazyRegressor` from the `lazypredict` library to build and compare regression models.
   - Splits the data into training and testing subsets based on user-defined parameters.

3. **Performance Metrics:**
   - Displays key metrics for each model, including R-squared, RMSE, and computation time.
   - Generates visualizations for R-squared, RMSE, and calculation time for better understanding.

4. **Interactive User Experience:**
   - User-defined split ratio for training/testing data.
   - Option to set a random seed for reproducibility.

5. **Export Results:**
   - Provides downloadable CSV files for training and test performance metrics.
   - Allows users to download generated plots in PDF format.

---

## Installation

1. **Prerequisites:**
   - Python 3.7 or higher.
   - Libraries: `streamlit`, `pandas`, `lazypredict`, `scikit-learn`, `matplotlib`, `seaborn`, `base64`, `io`.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-project-folder
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App:**
   ```bash
   streamlit run app.py
   ```

---

## How to Use

1. **Launch the App:**
   Open the app in your browser by running the Streamlit server.

2. **Upload Data:**
   - Use the sidebar to upload a CSV file containing your dataset.
   - Alternatively, use the example dataset provided in the app.

3. **Set Parameters:**
   - Adjust the data split ratio for training and testing.
   - Specify a random seed for reproducibility.

4. **View Results:**
   - Check the performance of models on the training and test sets.
   - Download results and visualizations for further analysis.

---

## Dependencies

- **Python**: 3.7+
- **Libraries**:
  - `streamlit`
  - `pandas`
  - `lazypredict`
  - `scikit-learn`
  - `matplotlib`
  - `seaborn`
  - `base64`

---

## Example

### Input Data:
You can use the example dataset provided in the app or upload your own CSV file with features and target variables.

### Output:
The app provides:
- A table of performance metrics for various regression models.
- Visualizations of R-squared, RMSE, and computation time.
- Download links for metrics and plots.

---

## Developed By
**Mohammad Rasoul Sahibzadah**  
[Visit Website](https://auaf.edu.af/)  

---

## License
This project is licensed under the MIT License.

---

Feel free to customize the content as per your specific requirements!
