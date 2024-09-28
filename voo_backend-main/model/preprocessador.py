import pandas as pd
import numpy as np




class PreProcessador:
    
    @staticmethod
    def preparar_form(form):
        """
        Prepara os dados recebidos de um formulário para serem usados no modelo.
        Ajusta a ordem das features para corresponder à ordem usada no treinamento.
        """
        # Variáveis categóricas (One-Hot Encoding)
        gender_female = int(form.gender == 0)
        gender_male = int(form.gender == 1)
        customer_type_loyal = int(form.customer_type == 1)
        customer_type_disloyal = int(form.customer_type == 0)
        type_of_travel_business = int(form.type_of_travel == 0)
        type_of_travel_personal = int(form.type_of_travel == 1)
        class_business = int(form.class_type == 0)
        class_eco = int(form.class_type == 1)
        class_eco_plus = int(form.class_type == 2)
        
        # Criando o array de entrada com a ordem correta das features
        X_input = np.array([
            form.age,                        # 0
            form.flight_distance,            # 1
            form.seat_comfort,               # 2
            form.inflight_entertainment,     # 3
            form.checkin_service,            # 4
            form.inflight_service,           # 5
            form.cleanliness,                # 6
            form.departure_delay,            # 7
            form.arrival_delay,              # 8
            gender_female,                   # 9
            gender_male,                     # 10
            customer_type_loyal,             # 11
            customer_type_disloyal,          # 12
            type_of_travel_business,         # 13
            type_of_travel_personal,         # 14
            class_business,                  # 15
            class_eco,                       # 16
            class_eco_plus                   # 17
        ])
        
        # Log dos valores de entrada
        print("Valores de entrada (X_input):", X_input)
        
        # Fazemos o reshape para que o modelo entenda que estamos passando uma única amostra
        X_input = X_input.reshape(1, -1)
        return X_input
