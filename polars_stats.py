import polars as pl

def analyze_with_polars(file_path):
    numeric_cols = ['Total Interactions', 'Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care']
    categorical_cols = ['Type', 'Page Category', 'Page Admin Top Country', 'Is Video Owner?', 'Video Share Status']

    df = pl.read_csv(file_path)

    # Clean numeric columns
    for col in numeric_cols:
        df = df.with_columns(
            pl.col(col).cast(str).str.replace_all(",", "").cast(pl.Float64).alias(col)
        )

    print("=== OVERALL NUMERIC SUMMARY ===")
    print(df.select(numeric_cols).describe())

    print("\n=== OVERALL CATEGORICAL SUMMARY ===")
    for col in categorical_cols:
        print(f"\n{col}:")
        print("  Unique:", df.select(pl.col(col).n_unique()).item())
        print("  Top 5:")
        print(
            df.select(pl.col(col).value_counts())
              .sort("count", descending=True)
              .limit(5)
        )

# Run it
if __name__ == "__main__":
    analyze_with_polars("C:/Users/divya/Downloads/PresidentialElectionAnalysis/2024_fb_posts_president_scored_anon.csv")
