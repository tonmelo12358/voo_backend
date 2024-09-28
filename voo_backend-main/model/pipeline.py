import pickle

class Pipeline:
    
    @staticmethod
    def carrega_pipeline(path):
        """Carregamos o pipeline construído durante a fase de treinamento"""
        try:
            with open(path, 'rb') as file:
                pipeline = pickle.load(file)
            return pipeline
        except FileNotFoundError:
            print(f"Arquivo {path} não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao carregar o pipeline: {e}")
            return None
