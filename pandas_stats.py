import pandas as pd

def analyze_with_pandas(file_path):
    
    numeric_cols = ['Total Interactions', 'Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care']
    categorical_cols = ['Type', 'Page Category', 'Page Admin Top Country', 'Is Video Owner?', 'Video Share Status']

    
    df = pd.read_csv(file_path)
    for col in numeric_cols:
        df[col] = df[col].astype(str).str.replace(',', '').replace('', '0').astype(float)

    print("=== OVERALL NUMERIC SUMMARY ===")
    print(df[numeric_cols].describe().round(2))

    print("\n=== OVERALL CATEGORICAL SUMMARY ===")
    for col in categorical_cols:
        print(f"\n{col}:")
        print("  Unique:", df[col].nunique())
        print("  Top 5:\n", df[col].value_counts().head(5))

    print("\n=== GROUPED BY Facebook_Id ===")
    grouped_page = df.groupby('Facebook_Id')
    for name, group in grouped_page:
        print(f"\nGroup: Facebook_Id = {name}")
        print(group[numeric_cols].describe().round(2).loc[['count', 'mean', 'min', 'max', 'std']])

    print("\n=== GROUPED BY (Facebook_Id, post_id) ===")
    grouped_page_post = df.groupby(['Facebook_Id', 'post_id'])
    for name, group in grouped_page_post:
        print(f"\nGroup: Facebook_Id = {name[0]}, post_id = {name[1]}")
        print(group[numeric_cols].describe().round(2).loc[['count', 'mean', 'min', 'max', 'std']])


if __name__ == "__main__":
    analyze_with_pandas("C:/Users/divya/Downloads/PresidentialElectionAnalysis/2024_fb_posts_president_scored_anon.csv")
