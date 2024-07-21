import glob
import pandas as pd

columns = [
    "推",
    "噓",
    "分數",
    "作者",
    "標題",
    "時間",
]

# Define functions
def get_text_file_paths() -> list[str]:
    return glob.glob("/workspaces/TIR102_Shi/res_gossiping/*.txt")

def e_text_file(path: str) -> str:
    with open(path, "r", encoding = 'utf-8') as f:
        return f.read()

def t_text_to_df_row_list(reply_info_string: str) -> list[str]
    reply_info_string = article_string.split("---split---")[1]
    return reply_info_string.split("\n")[1:-1]


def t_conbine_list_to_df(reply_info_list: list[list]) -> pd.DataFrame:
    returb pd.DataFrame(data = reply_info_list, columns=columns)

def l_df_to_csv(df: pd.DataFrame) -> None:
    df.to_csv("ptt_2.csv", index=0)


if __name__ == "__main__":
    path_list = get_text_file_paths()

    # get paths of all text files
    path_list = get_text_file_paths()

    # Loop for file path
    data =[]
    for path in path_list:
        # Extract text files
        article_string = e_text_file(path: str)
        # Text to list-elemet in DataFrame
        t_text_to_df_row_list(reply_info_string: str)

    # concat lists to DataFrame
    df = t_concat_list_to_df(data)

    # Load Dataframe to csv
    l_df_to_csv(df)