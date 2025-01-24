import pandas as pd 
import sys
from pathlib import Path

data_path= Path(__file__).parent / "data"

print(data_path / "prog_book.csv")

df = pd.read_csv(data_path / "prog_book.csv")
print(df.head())

df.head().to_csv(data_path / "prog_book_head.csv")

