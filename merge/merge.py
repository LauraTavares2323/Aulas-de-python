import sys
sys.path


m = pd.merge(tabela_1, tabela_2, how = 'inner', on = 'Nome')