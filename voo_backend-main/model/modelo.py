import pickle
import joblib

class Model:
    
    @staticmethod
    def carrega_modelo(path):
        """Carrega o modelo treinado. Dependendo se o final for .pkl ou outro formato, carregamos de uma forma ou de outra"""
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    @staticmethod
    def realiza_predicao(pipeline, X_input):
        """Realiza a predição usando o modelo fornecido"""
        prediction = pipeline.predict(X_input)
        return prediction

