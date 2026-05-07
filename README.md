# NTPU Statistical Computing 2024 Fall

This repository contains the source code (.ipynb) and projects for the `Statistical Computing (I)` course at National Taipei University (NTPU), Department of Statistics.

The projects range from foundational probability distribution exploration and parameter estimation theory verification to reliability analysis of complex systems. Through Python and Monte Carlo simulations, these projects investigate the properties and performance of various statistical methods in depth.

## 📋 Table of Contents

* [Project 1: Exploring Probability Distributions](./Project_1)
* [Project 2: MLE Experiment for Normal Distribution](./Project_2)
* [Project 3: Two-Sample T-Test Analysis](./Project_3)
* [Project 4: J-B Test & Normality Verification](./Project_4)
* [Project 5: Normal Mixture Models (MLE vs. GMM)](./Project_5)
* [Project 6: Component Reliability Analysis](./Project_6)

## 📂 File Directory

| Project | Source Code (.ipynb) | Static Report (.html) |
| :--- | :---: | :---: |
| **Project 1** | [💻 Notebook](./Project_1/Probability_Distribution_with_Different_Samples.ipynb) | [🌐 Preview](https://htmlpreview.github.io/?https://github.com/shengsia02/NTPU-StatComp-2024-Fall/blob/main/Project_1/Probability_Distribution_with_Different_Samples.html) |
| **Project 2** | [💻 Notebook](./Project_2/MLE_Estimate_Experiment.ipynb) | [🌐 Preview](https://htmlpreview.github.io/?https://github.com/shengsia02/NTPU-StatComp-2024-Fall/blob/main/Project_2/MLE_Estimate_Experiment.html) |

---

### 🔔 Project 1: Exploring Probability Distributions and Random Samples
This project aims to intuitively understand the characteristics of common continuous distributions.
* Visualized and compared the Probability Density Functions (PDF) of **Normal, Chi-square, T, Beta, and F** distributions under different parameters.
* Generated random samples of varying sizes ($N$) to plot Histograms, Boxplots, Probability plots (Q-Q plots), and Empirical Cumulative Distribution Functions (ECDF).
* Analyzed the impact of sample size on the stability and representativeness of statistical visualizations.

### 🔍 Project 2: Maximum Likelihood Estimation Experiment for Normal Distribution
This project verifies the performance of Maximum Likelihood Estimation (MLE) in various scenarios.
* Visualized joint likelihood functions to investigate the influence of sample characteristics and sample size on the estimator $\hat{\mu}$.
* Implemented and compared three estimation methods: `scipy.optimize` numerical optimization, Analytical Formulas, and **Grid Search**.
* Conducted parameter estimation using log-likelihood functions under conditions where both the mean and standard deviation are unknown.

### 📏 Project 3: Analysis of T-values, P-values, and Power in Two-Sample T-Tests
This project validates the theoretical properties of the Two-Sample T-test through large-scale simulations.
* Verified whether the distribution of simulated T-values aligns with the theoretical T-distribution.
* Investigated the impact of sample size on P-value distributions and **Statistical Power** under both $H_0$ (same populations) and $H_1$ (different populations).
* Demonstrated the effectiveness of the Two-Sample T-test in controlling **Type I Error**.

### ✔️ Project 4: Verifying J-B Test Statistics and Power via Monte Carlo Simulation
This project utilizes Monte Carlo methods to evaluate the performance of normality tests.
* Verified whether the Skewness and Kurtosis statistics follow a Standard Normal distribution and if the **Jarque-Bera (J-B)** statistic follows a Chi-square distribution.
* Compared the **Power** of multiple normality tests (including J-B, K-S, Shapiro-Wilk, Anderson-Darling, etc.) across various population distributions.

### 🧩 Project 5: Parameter Estimation for Normal Mixture Models — MLE vs. GMM
This project focuses on parameter estimation and performance evaluation for complex mixture distributions.
* Implemented Maximum Likelihood Estimation (MLE) to estimate parameters for Normal Mixture models.
* Employed the `sklearn.mixture.GaussianMixture` (GMM) method and conducted a comparative analysis against the self-built MLE model.
* Calculated **Mean, Bias, and RMSE** through Monte Carlo simulations to assess estimation precision across different sample sizes.

### ⚙️ Project 6: Reliability Analysis and Simulation for Different Component Structures
This project performs reliability analysis and simulation based on component connection configurations.
* Simulated the reliability distributions for components in **Series** and **Parallel** configurations.
* Estimated system distribution parameters using four methods: LSM, MLE, MME, and KDE.
* Designed and compared the reliability of complex systems (e.g., "Series-Parallel" vs. "Parallel-Series") to identify the optimal system combination.

---

## ⚙️ Environment Setup

**1. Python Version** \
The development environment for this project is **Python 3.11.3**. It is recommended to refer to the `.python-version` file for configuration.

**2. Dependencies** \
Ensure the following core scientific computing libraries are installed:
* `numpy`, `scipy`, `matplotlib`, `pandas`
* `statsmodels`, `sklearn`

You can quickly install them using the following command:
```bash
pip install -r requirements.txt
```