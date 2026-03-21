"""Transform CV data from local CSV for rendering in Quarto."""

from pathlib import Path

import pandas as pd
from great_tables import GT

CSV_PATH = Path("data/cv_data.csv")


def _col_br(value: str | float) -> str:
    if pd.isna(value) or value == "N/A":
        return ""
    return f"<br> {value}"


def _col_no_br(value: str | float) -> str:
    if pd.isna(value) or value == "N/A":
        return ""
    return f"| {value}"


def _format_date(row: pd.Series) -> str:
    start = row["start"]
    end = row["end"]
    if pd.isna(end):
        return f"Current <br> | <br> {int(start)}"
    start, end = int(start), int(end)
    if end != start:
        return f"{end} <br> | <br> {start}"
    return str(end)


def _format_main_text(row: pd.Series) -> str:
    title = row["title"]
    institution = _col_no_br(row["institution"])
    loc = _col_no_br(row["loc"])
    description = _col_br(row["description_1"])
    return f"**{title}** {institution} {loc} {description}"


def create_section(df: pd.DataFrame, section_name: str) -> GT:
    section_df = df[
        (df["in_resume"].astype(str).isin(["TRUE", "True", "VERDADEIRO"]))
        & (df["section"] == section_name)
    ].copy()

    section_df.loc[section_df["loc"] == "Online", "loc"] = pd.NA

    section_df["date"] = section_df.apply(_format_date, axis=1)
    section_df["main_text"] = section_df.apply(_format_main_text, axis=1)

    section_df = section_df.sort_values(
        ["end", "start"], ascending=[False, False], na_position="first"
    )

    table_df = section_df[["date", "main_text"]]

    return (
        GT(table_df, id="table_id")
        .cols_width({"date": "15%"})
        .fmt_markdown(columns=["date", "main_text"])
        .cols_align(align="center", columns="date")
        .cols_align(align="left", columns="main_text")
        .tab_options(
            table_width="100%",
            column_labels_hidden=True,
        )
        .opt_css(
            """
            #table_id .gt_table {
                font-family: var(--bs-body-font-family);
            }
            """
        )
    )


cv = pd.read_csv(CSV_PATH)
