import pandas as pd

class Carregador:

    @staticmethod
    def carregar_dados(url: str, atributos: list):
        """
        Carrega e retorna um DataFrame a partir de uma URL ou caminho.
        
        Parameters:
        - url: O caminho do arquivo CSV.
        - atributos: Uma lista de nomes de colunas (atributos) para o DataFrame.
        
        Returns:
        - DataFrame com os dados carregados.
        """
        try:
            df = pd.read_csv(url, names=atributos, header=0, delimiter=',')
            return df
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return None
