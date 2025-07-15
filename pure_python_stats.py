import csv
import math
from collections import defaultdict, Counter


def parse_int(val):
    try:
        return int(val.replace(',', '').strip()) if val else 0
    except:
        return 0

def mean(values):
    return sum(values) / len(values) if values else 0

def std_dev(values):
    if len(values) < 2:
        return 0
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

def summarize_numeric(col_values):
    return {
        "count": len(col_values),
        "mean": round(mean(col_values), 2),
        "min": min(col_values),
        "max": max(col_values),
        "std_dev": round(std_dev(col_values), 2)
    }

def summarize_categorical(col_values):
    counter = Counter(col_values)
    return {
        "unique": len(counter),
        "most_common": counter.most_common(1)[0] if counter else None
    }



def analyze_csv(file_path):
    numeric_cols = ['Total Interactions', 'Likes', 'Comments', 'Shares', 'Love', 'Wow', 'Haha', 'Sad', 'Angry', 'Care']
    categorical_cols = ['Type', 'Page Category', 'Page Admin Top Country', 'Is Video Owner?', 'Video Share Status']

    raw_data = defaultdict(list)
    grouped_by_page_id = defaultdict(lambda: defaultdict(list))
    grouped_by_page_ad = defaultdict(lambda: defaultdict(list))  # (page_id, post_id)

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            page_id = row['Facebook_Id']
            post_id = row['post_id']

            for col in numeric_cols:
                value = parse_int(row.get(col, '0'))
                raw_data[col].append(value)
                grouped_by_page_id[page_id][col].append(value)
                grouped_by_page_ad[(page_id, post_id)][col].append(value)

            for col in categorical_cols:
                val = row.get(col, '')
                raw_data[col].append(val)
                grouped_by_page_id[page_id][col].append(val)
                grouped_by_page_ad[(page_id, post_id)][col].append(val)

    print("=== OVERALL NUMERIC SUMMARY ===")
    for col in numeric_cols:
        stats = summarize_numeric(raw_data[col])
        print(f"{col}: {stats}")

    print("\n=== OVERALL CATEGORICAL SUMMARY ===")
    for col in categorical_cols:
        stats = summarize_categorical(raw_data[col])
        print(f"{col}: Unique={stats['unique']}, Most Common={stats['most_common']}")

    print("\n=== AGGREGATED BY PAGE_ID ===")
    for group, group_data in grouped_by_page_id.items():
        print(f"\nGroup: Page ID = {group}")
        for col in numeric_cols:
            if group_data[col]:
                stats = summarize_numeric(group_data[col])
                print(f"  {col}: {stats}")
        for col in categorical_cols:
            stats = summarize_categorical(group_data[col])
            print(f"  {col}: Unique={stats['unique']}, Most Common={stats['most_common']}")

    print("\n=== AGGREGATED BY (PAGE_ID, POST_ID) ===")
    for group, group_data in grouped_by_page_ad.items():
        print(f"\nGroup: Page ID = {group[0]}, Post ID = {group[1]}")
        for col in numeric_cols:
            if group_data[col]:
                stats = summarize_numeric(group_data[col])
                print(f"  {col}: {stats}")
        for col in categorical_cols:
            stats = summarize_categorical(group_data[col])
            print(f"  {col}: Unique={stats['unique']}, Most Common={stats['most_common']}")


if __name__ == "__main__":
    analyze_csv("C:/Users/divya/Downloads/PresidentialElectionAnalysis/2024_fb_posts_president_scored_anon.csv")
