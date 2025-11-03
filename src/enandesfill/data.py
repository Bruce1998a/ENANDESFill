# src/enandesfill/data.py
import pandas as pd
from pathlib import Path
try:
    # Python 3.9+: usa importlib.resources cuando el archivo está empaquetado
    from importlib import resources
    def load_example():
        with resources.files(__package__).joinpath("ejemplo_fill_py.csv").open("rb") as f:
            return pd.read_csv(f)
except Exception:
    # Respaldo: carga por ruta relativa al archivo actual (útil en editable)
    def load_example():
        p = Path(__file__).with_name("ejemplo_fill_py.csv")
        return pd.read_csv(p)

