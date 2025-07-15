# Descriptive Statistics Engine: 2024 US Presidential Social Media Analysis

This project is part of an OPT experiential learning initiative focused on building a multi-method descriptive statistics system. The dataset used contains social media interactions related to the 2024 US Presidential Elections.

## 👤 Author
**Shetty, Shreshth**

---

## 📁 Project Structure

This repository includes three Python scripts demonstrating different approaches to descriptive statistical analysis:

### 1. `pure_python_stats.py`
- Uses **only Python standard libraries**
- Computes count, mean, min, max, standard deviation
- Supports group-by aggregations (`Facebook_Id`, `post_id`)
- Handles both numeric and categorical columns

### 2. `pandas_stats.py`
- Implements the same logic using **Pandas**
- Utilizes `DataFrame.describe()`, `value_counts()`, `groupby()`
- Efficient for medium to large datasets

### 3. `polars_stats.py`
- Uses the **Polars** DataFrame library for performance
- Handles numeric and categorical summaries
- Deals with lazy evaluation and uses `.collect()` for grouping and sorting
- Significantly faster for large-scale datasets

---

## 📊 Dataset

The dataset contains Facebook posts and engagement metrics:
- `Total Interactions`, `Likes`, `Comments`, `Shares`, and other reactions
- `Page Category`, `Type`, `Page Admin Country`, etc.
- Each post has a unique `Facebook_Id` and `post_id`



---

## 🧠 Skills Developed

- Python scripting (standard library, file I/O, error handling)
- Data analysis using Pandas and Polars
- Performance tuning and memory-efficient computations
- Data cleaning, type casting, and frequency distributions
- Comparative analysis of Python data libraries

---
