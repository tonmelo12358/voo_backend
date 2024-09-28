from model import *
import pandas as pd
from sklearn.model_selection import train_test_split  # Para dividir os dados

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Carga dos dados de teste a partir dos arquivos corretos
src_x_test = './Machine Learning/data/X_test_dataset_voo.csv'
src_y_test = './Machine Learning/data/y_test_dataset_voo.csv'

# Carregando os dados de teste
X_test = pd.read_csv(src_x_test, delimiter=',')
y_test = pd.read_csv(src_y_test, delimiter=',')

# Verificar as dimensões de X_test e y_test
print(f"Dimensões de X_test: {X_test.shape}")
print(f"Dimensões de y_test: {y_test.shape}")


# Método para testar o pipeline completo do Random Forest
def test_pipeline_rf():
    # Importando o pipeline completo de Random Forest
    rf_pipeline_path = './Machine Learning/pipelines/rf_voo_pipeline.pkl'
    modelo_rf_pipeline = Pipeline.carrega_pipeline(rf_pipeline_path)

    # Obtendo as métricas do pipeline do Random Forest
    acuracia_rf_pipeline = Avaliador.avaliar(modelo_rf_pipeline, X_test.values, y_test.values.ravel())  # Usando X_test e y_test
    
    print(acuracia_rf_pipeline)
    
    # Testando as métricas do pipeline (assert para verificar se a acurácia é maior ou igual a 80%)
    assert acuracia_rf_pipeline['accuracy'] >= 0.8
