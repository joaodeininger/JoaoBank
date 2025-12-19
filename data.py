import pandas as pd

df = pd.DataFrame({
    "Produto": ["Python", "Pandas", "Streamlit", "NumPy"],
    "Categoria": ["Linguagem", "Biblioteca", "Framework", "Biblioteca"],
    "Popularidade": [95, 90, 85, 92],
    "Ano": [1991, 2008, 2019, 2005]
})


df.to_csv("entrada")