import matplotlib.pyplot as plt
import os

def plot_highest_from_col(df, col, num, save=False):
    """
    Takes in a dataframe, a column name, and a number

    Creates a bar graph with the number of highest values
    in that column
    """
    num_highest = df.sort_values(col, ascending=False).iloc[:num]

    _, ax = plt.subplots(figsize=(num, 8))
    plt.xticks(rotation=45)
    ax.bar(num_highest["school"], num_highest[col])
    ax.set_title(f"{num} School Fight Songs with Highest {col}")
    ax.set_ylabel(col)

    if save:
        img_name = f"highest_{num}_{col}.png"
        img_path = os.path.join(os.pardir, os.pardir,
                                "report", "img", img_name)
        plt.savefig(img_path)

    plt.show()
