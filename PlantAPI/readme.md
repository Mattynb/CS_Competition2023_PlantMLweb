# CS_Competition2023_PlantMLweb

Welcome to the CS_Competition2023_PlantMLweb repository! This project is focused on developing a web application for plant disease identification using machine learning.

## Overview

Our application leverages a machine learning model, encapsulated in a Jupyter Notebook (`Model/PlantML.ipynb`), to identify plant diseases from images. The web interface is built using Flask and is located in the `PlantAPI` directory.

## Features

- **Machine Learning Model**: A Jupyter Notebook (`Model/PlantML.ipynb`) containing the machine learning model for plant disease identification.
- **Web Interface**: A Flask-based web application allowing users to upload images and receive disease identification results.
  - **Home Page**: (`PlantAPI/templates/home.html`) The landing page of the application.
  - **Submission Page**: (`PlantAPI/templates/index.html`) Where users can submit their plant images.
  - **Results Page**: (`PlantAPI/templates/results.html`) Displays the identification results.
  - **JavaScript Integration**: (`PlantAPI/templates/submit_script.js`) Enhances the user interaction with the web application.

## Getting Started

To get started with this project:

1. Clone the repository.
2. Install the required dependencies.
3. Run the Flask application located in `PlantAPI/API.py`.

## Contributing

We welcome contributions to this project. Please feel free to submit issues or pull requests.

## License

This project is licensed under [appropriate license]. Please see the LICENSE file for more details.
