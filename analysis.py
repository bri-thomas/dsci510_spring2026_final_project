import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

DATA_DIR = Path("data")

def load_merged() -> pd.DataFrame:
    path = DATA_DIR / "merged_work_happiness_countries.csv"
    df = pd.read_csv(path)
    return df

def basic_eda(df: pd.DataFrame):
    print(df.shape)
    print(df.isna().mean())
    print(df.describe())

    df = df.dropna(subset=["work_hours", "happiness_score"]).copy()

    #Scatterplot
    plt.figure(figsize = (8,6))
    sns.scatterplot(
        data = df,
        x = "work_hours",
        y = "happiness_score",
        hue = "Region"
    )
    plt.title("Work hours vs happiness by Region")
    plt.grid(True, alpha=0.3)
    plt.show()

    #Correlation
    print(df[["work_hours", "happiness_score"]].corr())

def clustering_and_regression(df: pd.DataFrame):
    df = df.dropna(subset=["work_hours", "happiness_score"]).copy()

    #Clustering
    X = df[["work_hours", "happiness_score"]].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    km = KMeans(n_clusters = 4).fit(X_scaled) #The range of n_clusters
    labels = km.fit_predict(X_scaled)
    df["cluster"] = labels

    plt.figure(figsize = (8,6))
    sns.scatterplot(
        data = df,
        x = "work_hours",
        y = "happiness_score",
        hue = "cluster",
        palette = "viridis" #AI suggested palette as original palette is hard to differentiate
    )
    plt.title("Clusters pof Countries by Work Hours and Happiness")
    plt.grid(True, alpha=0.3)
    plt.show()

    print(df.groupby("cluster")[["work_hours", "happiness_score"]].mean())

    #Regression
    X = df[["work_hours"]].values
    y = df[["happiness_score"]].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2 #randomly selecting 20% of data into test set and 80% into training set
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    print("Coefficient: ", model.coef_[0])
    print("Intercept: ", model.intercept_)
    print("R^2 train: ", model.score(X_train, y_train))
    print("R^2 test: ", model.score(X_test, y_test))

    cluster_summary = (
        df.groupby(["cluster"])[["work_hours", "happiness_score"]].mean().round(2)
    )
    cluster_counts = df["cluster"].value_counts().sort_index()

    print(cluster_summary)
    print(cluster_counts)

    region_cluster = (
        df.groupby(["cluster", "Region"])["country"] #AI Generated
        .count() #AI Generated
        .unstack(fill_value=0) #AI Generated
    )

    print(region_cluster)