from rich.console import Console
from rich.table import Table
import pandas as pd
from finclient import containers

def style_negative(val):
    if isinstance(val, bool):
        return val and "[grey53]closed[/grey53]" or "[green]open[/green]"  
    elif isinstance(val, (int, float)):
        formatted_val = f"{val:.2f}"  
        if val < 0:
            return f"[red]{formatted_val}[/red]"
        return formatted_val
    return str(val)


if __name__ == "__main__":
    container = containers.Container()
    
    client=container.client()

    df = client.all_months_df()

    table = Table(title="My monthly finance")

    for column in df.columns:
        table.add_column(column, justify="right")

    for _, row in df.iterrows():
        table.add_row(*[style_negative(val) for val in row])

    console = Console()
    console.print(table)
    