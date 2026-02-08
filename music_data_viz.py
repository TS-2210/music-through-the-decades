from glob import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    decades_files = glob("data/*.csv")
    decades_dfs = []
    for file in decades_files:
        decade_df = pd.read_csv(file)
        decade_df["Decade"] = file.split("/")[-1].split(".")[0] + "s"
        decades_dfs.append(decade_df)
    return pd.concat(decades_dfs, ignore_index=True)
def clean_data(df):
    return df.dropna()
def line_plot(df):
    sns.lineplot(
        data=df,
        x="Decade",
        y="dB"
    )
    plt.title("Loudness (dB) of music by Decade")
    plt.show()
def heatmap(df):
    corr = df[
        ["bpm", "dB", "nrgy", "live", "spch", "pop", "dnce", "val", "acous"]
    ].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap of Music Features")
    plt.show()

def main():
    music = load_data()
    music_clean = clean_data(music)
    line_plot(music_clean)
    heatmap(music_clean)
if __name__ == "__main__":
    sns.set_theme(
    style="whitegrid",
    palette="muted",
    font_scale=1.1
)
    main()
    