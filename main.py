# Project Title: Energy Insights - Electricity Usage Dashboard 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the electricity data
df = pd.read_csv("CONV.csv")

# Step 1: Initial Overview
print("Checking for missing data...\n")
print(df.isnull().sum())

# Main Interactive Interface
def main_menu():
    while True:
        print("\n🔌 E-Consumption Analyzer 🔌")
        print("1. Dataset Overview & Insights")
        print("2. Built-In Analytical Dashboards")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            show_overview()
        elif choice == "2":
            run_objectives()
        elif choice == "3":
            print("Exiting... Stay bright ⚡")
            break
        else:
            print("Invalid input. Try again!")

# Option 1: Basic EDA
def show_overview():
    print("\n🧠 Dataset Information:")
    print(df.info())
    print("\n👀 First Few Rows:")
    print(df.head())
    print("\n📈 Statistical Summary:")
    print(df.describe())

    # Correlation Matrix
    numeric = df.select_dtypes(include=[np.number])
    if 'CatCode' in numeric.columns:
        numeric = numeric.drop('CatCode', axis=1)
    
    plt.figure(figsize=(9, 6))
    sns.heatmap(numeric.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix - Numeric Fields")
    plt.tight_layout()
    plt.show()

# Option 2: Predefined Visual Objectives
def run_objectives():
    print("\n🎯 Choose Analysis Objective:")
    print("1. Load vs Units Consumed")
    print("2. Top 10 High-Usage Areas")
    print("3. Total vs Billed Services")
    print("4. Circle-wise Usage")
    print("5. Spread of Billed Services")
    print("6. Billing Percentage Pie")
    print("7. Load Distribution Curve")
    
    choice = input("Your pick (1-7): ")

    if choice == "1":
        sns.scatterplot(data=df, x='Load', y='Units', alpha=0.6, color='orange')
        plt.title("Load vs Electricity Units")
        plt.xlabel("Load")
        plt.ylabel("Units Consumed")
        plt.show()

    elif choice == "2":
        top = df.groupby('Area')['Units'].sum().nlargest(10)
        top.plot(kind='bar', color='teal')
        plt.title("Top 10 Areas by Consumption")
        plt.xlabel("Area")
        plt.ylabel("Units")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    elif choice == "3":
        sns.scatterplot(x=df['TotServices'], y=df['BilledServices'], alpha=0.5)
        plt.title("Total Services vs Billed")
        plt.xlabel("Total Services")
        plt.ylabel("Billed Services")
        plt.show()

    elif choice == "4":
        sns.barplot(x='Circle', y='Units', data=df, estimator=sum, palette='magma')
        plt.title("Electricity Usage by Circle")
        plt.xticks(rotation=60)
        plt.ylabel("Total Units")
        plt.tight_layout()
        plt.show()

    elif choice == "5":
        sns.boxplot(y='BilledServices', data=df, color='skyblue')
        plt.title("Billed Services Spread")
        plt.ylabel("Billed Services")
        plt.show()

    elif choice == "6":
        billed = df['BilledServices'].sum()
        total = df['TotServices'].sum()
        sizes = [billed, total - billed]
        labels = ['Billed', 'Unbilled']
        colors = ['green', 'red']

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops=dict(edgecolor='black'))
        plt.title("Billed vs Unbilled Services")
        plt.show()

    elif choice == "7":
        sns.histplot(df['Load'], bins=30, kde=True, color='navy')
        plt.title("Distribution of Electrical Load")
        plt.xlabel("Load")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("Invalid selection.")

# Fire it up 🚀
main_menu()
