# 📱 PhoneCost-Predictor

A machine learning project that predicts mobile phone prices.

## 🚀 About

This repository contains the code and resources for a mobile price classification project. The project aims to predict the price range of mobile phones based on their specifications using machine learning techniques. This project is a demonstration of applying machine learning for a real-world classification task.

## 🎯 Project Goals

*   Develop a robust machine learning model capable of accurately predicting mobile phone price ranges.
*   Provide a user-friendly interface to interact with the model for price predictions.
*   Showcase the use of Python and machine learning techniques in a practical application.

## ⚙️ Files and Structure

Here's an overview of the project structure:

*   **`static/`**: 🖼️ Contains static assets like images and logos.
*   **`templates/`**: 💻 Frontend templates for the user interface.
*   **`README.md`**: 📖 The project's README file (you're reading it!).
*   **`app.py`**: 🧮 Contains the application logic for the model.
*   **`download.jfif`**: 🖼️ Logo image.
*   **`main.py`**: ⚙️ Main Python file, entry point of the application.
*   **`mobile.jfif`**: 🖼️ Logo image.
*   **`model.pkl`**: 💾 Trained machine learning model, pickled for easy loading.
*   **`th.jfif`**: 🖼️ Logo image.
*   **`train.csv`**: 📊 Data file used to train the model, containing mobile phone specifications and price ranges.

## 🤖 Machine Learning Model

The project uses a **K-Nearest Neighbors (KNN)** machine learning model. The model is trained on the `train.csv` dataset to learn the relationship between phone features and their price ranges. The KNN model has been chosen for its efficacy in **handling classification problems, ease of implementation, and its simplicity to understand**.

## 📊 Data Description

The training data is stored in `train.csv` and consists of the following features:

*   `battery_power`: Total energy a battery can store in one time measured in mAh
*   `blue`: Has bluetooth or not
*   `clock_speed`: speed at which microprocessor executes instructions
*  `dual_sim`: Has dual sim support or not
*  `fc`: Front Camera mega pixels
*  `four_g`: Has 4G or not
*  `int_memory`: Internal Memory in Gigabytes
*  `m_dep`: Mobile Depth in cm
*  `mobile_wt`: Weight of mobile phone
*  `n_cores`: Number of cores of processor
*  `pc`: Primary Camera mega pixels
*  `px_height`: Pixel Resolution Height
*  `px_width`: Pixel Resolution Width
*  `ram`: Random Access Memory in Megabytes
* `sc_h`: Screen Height of mobile in cm
* `sc_w`: Screen Width of mobile in cm
* `talk_time`: longest time that a single battery charge will last
* `three_g`: Has 3G or not
*  `touch_screen`: Has touch screen or not
* `wifi`: Has wifi or not

*   The target variable is the price range of the phone.

## 💻 Languages Used

The project primarily uses:

*   **HTML**: 80.5% 🌐 - For structuring the frontend.
*   **Python**: 19.5% 🐍 - For model building, application logic, and backend functionality.

## ✨ Key Features

*   **Machine Learning**: Uses a trained **K-Nearest Neighbors (KNN)** model to predict phone prices.
*   **Frontend**: User interface to interact with the price prediction model.
*   **Data Driven**: Relies on the data provided in `train.csv` for model training and prediction.
*   **Model Persistence**: The trained model is saved using `model.pkl`, allowing for quick loading without retraining.

## 🚀 How to Run

To run the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [paste your repo link here]
    cd PhoneCost-Predictor
    ```
2.  **Install dependencies:**
    ```bash
    pip install numpy pandas scikit-learn flask
    ```
3.  **Run the application:**
    ```bash
    python app.py # or main.py, depending on your entry point
    ```
4.  **Access the application**: Open your web browser and navigate to `http://localhost:5000` (or the specific address printed in your terminal).

## ✨ Contributions

Contributions are always welcome. If you would like to make any changes or additions, create a new branch and submit a pull request!.
