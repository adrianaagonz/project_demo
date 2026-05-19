import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path 

def plot_graph(df: pd.DataFrame) -> None:
    """ Generate and save the key exploratory plots for the sephora dataset."""
    # Define the output directory to save plots
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "data" / "processed"

    # 1. Price distribution plot (histogram)
    plt.figure(figsize=(10, 5))
    sns.histplot(df['price_usd'], bins=30, kde=True, color='purple')
    plt.title('Distribution of Product Prices in Sephora')
    plt.xlabel('Price (USD)')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(output_dir / "price_distribution.png")
    plt.close()
    print("Saved price distribution plot succesfully.")

    # 2. Top brands plot (bar chart)
    plt.figure(figsize=(10, 5))
    top_brands = df['brand_name'].value_counts().head(10)
    sns.barplot(x=top_brands.values, y=top_brands.index, palette='viridis')
    plt.title('Top 10 Brands in Sephora')
    plt.xlabel('Number of Products')
    plt.ylabel('Brand name')
    plt.tight_layout()
    plt.savefig(output_dir / "top_brands.png")
    plt.close()
    print("Saved top brands plot succesfully.")
    
    # 3. Rating vs Number of Reviews 
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df, x='rating', y='reviews', alpha=0.5, color='teal')
    plt.title('Product Ratings vs. Number of Reviews')
    plt.xlabel('Rating (Stars)')
    plt.ylabel('Number of Reviews')
    plt.savefig(output_dir / "rating_vs_reviews.png")
    plt.close()
    print("Saved rating vs reviews plot successfully.")
    
    # 4. Top 10 Most Loved Products 
    plt.figure(figsize=(10, 5))
    top_loved = df.nlargest(10, 'loves_count')
    sns.barplot(data=top_loved, x='loves_count', y='product_name', palette='magma')
    plt.title('Top 10 Most Loved Products (User Favorites)')
    plt.xlabel('Loves Count')
    plt.ylabel('Product Name')
    plt.tight_layout()
    plt.savefig(output_dir / "top_loved_products.png")
    plt.close()
    print("Saved top loved products plot successfully.")
