# Data Mining Midterm Project

Welcome to the Data Mining Midterm Project repository! This project aims to provide an implementation of association rule mining algorithms and compare their performance using a variety of datasets. This README will guide you through the contents of this repository and how to utilize them effectively.

## Files Overview

1. **AmazonBooks.csv**: A dataset containing transactional data related to books purchased on Amazon.
2. **BestBuy.csv**: A dataset containing transactional data related to purchases made on Best Buy.
3. **Generic.csv**: A generic dataset for association rule mining experimentation.
4. **Grocery Store.csv**: A dataset containing transactional data related to grocery store purchases.
5. **K-Mart.csv**: A dataset containing transactional data related to purchases made at K-Mart.
6. **Nike.csv**: A dataset containing transactional data related to Nike product purchases.

7. **Brute_Force_Code.py**: Python script implementing a brute-force approach for association rule mining using the Apriori algorithm.

8. **Data_Mining_Midterm_Project.ipynb**: Jupyter Notebook containing the main project implementation. It includes user interfaces for selecting datasets, setting minimum support and minimum confidence values, and comparing the results of the brute-force approach with the mlxtend library's Apriori implementation.

9. **requirements.txt**: A file listing all the required Python packages for running the project.

## How to Use
1. **Clone the Repository** : Clone the repository in your local storage
   
2. **Set Parameters**: Open `Data_Mining_Midterm_Project.ipynb` and execute the notebook. Follow the instructions to input the chosen dataset, as well as the minimum support and minimum confidence values.

3. **Run the Analysis**: Execute the cells in the notebook to run the association rule mining algorithms. The notebook will use both the brute-force approach implemented in `Brute_Force_Code.py` and the mlxtend library's Apriori algorithm to find association rules.

4. **Review Results**: After execution, the notebook will present the generated association rules and compare the results obtained from both approaches. Analyze the performance and effectiveness of each method based on the chosen dataset and parameters.

## Requirements

Make sure you have all the required Python packages installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Conclusion

This project provides a comprehensive exploration of association rule mining techniques using real-world transactional datasets. Feel free to experiment with different datasets and parameters to gain insights into association patterns within the data.

Thank you for using our Data Mining Midterm Project repository! Happy mining! 🛒💡📊
