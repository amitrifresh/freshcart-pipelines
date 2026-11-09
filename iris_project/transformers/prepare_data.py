from sklearn.model_selection import train_test_split


def transform(df, test_size=0.2, random_state=42):
    """Return the Iris rows with a deterministic train/test split label.

    The input DataFrame is not modified. The returned DataFrame has a new
    `split` column containing either `train` or `test`.
    """
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")

    train_index, test_index = train_test_split(
        df.index,
        test_size=test_size,
        random_state=random_state,
        stratify=df["target"] if "target" in df.columns else None,
    )

    result = df.copy()
    result["split"] = "train"
    result.loc[test_index, "split"] = "test"
    return result
