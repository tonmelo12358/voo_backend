from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.modelo import Model

class Avaliador:

    @staticmethod
    def avaliar(model, X_test, Y_test):
        """
        Faz uma predição e avalia o modelo com base nas métricas de desempenho.
        
        Retorna o accuracy_score. Outras métricas podem ser parametrizadas.
        """
        predicoes = Model.realiza_predicao(model, X_test)
        
        # Avaliação usando diversas métricas
        accuracy = accuracy_score(Y_test, predicoes)
        recall = recall_score(Y_test, predicoes, average='binary')
        precision = precision_score(Y_test, predicoes, average='binary')
        f1 = f1_score(Y_test, predicoes, average='binary')
        
        return {
            'accuracy': accuracy,
            'recall': recall,
            'precision': precision,
            'f1_score': f1
        }
