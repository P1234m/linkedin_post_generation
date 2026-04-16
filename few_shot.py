import pandas as pd
import json


class FewShotPosts:
    def __init__(self, file_path="data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8", errors="ignore") as f:
            posts = json.load(f)
        pd.options.mode.string_storage = "python"

        self.df = pd.json_normalize(posts)

        if "line_count" in self.df.columns:
            self.df["length"] = self.df["line_count"].apply(self.categorize_length)
        else:
            self.df["length"] = "Unknown"

        all_tags = []
        if "tags" in self.df.columns:
            for tags in self.df["tags"]:
                if isinstance(tags, list):
                    all_tags.extend(tags)
        self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df["tags"].apply(lambda tags: isinstance(tags, list) and tag in tags)) &
            (self.df["language"] == language) &
            (self.df["length"] == length)
        ]
        return df_filtered.to_dict(orient="records")

    def categorize_length(self, line_count):
        try:
            if line_count < 5:
                return "Short"
            elif 5 <= line_count <= 10:
                return "Medium"
            else:
                return "Long"
        except Exception:
            return "Unknown"

    def get_tags(self):
        return self.unique_tags


if __name__ == "__main__":
    fs = FewShotPosts()
    posts = fs.get_filtered_posts("Medium", "Hinglish", "Job Search")
    print(posts)
