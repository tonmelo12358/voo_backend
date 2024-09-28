from pydantic import BaseModel, Field
from typing import Optional, List
from model.passageiro import Passageiro
import json
import numpy as np

class PassageiroSchema(BaseModel):
    """Define como um novo Passageiro a ser inserido deve ser representado"""

    name: str = Field("Maria", description="Nome do passageiro - não pode ser repetido")
    age: int = Field(40, description="Idade do passageiro")
    gender: int = Field(1, description="Gênero: 0 para Feminino, 1 para Masculino")
    customer_type: int = Field(1, description="Tipo de cliente: 1 para Fiel, 0 para Não fiel")
    type_of_travel: int = Field(1, description="Tipo de viagem: 0 para Viagem a Negócios, 1 para Viagem Pessoal")
    flight_distance: int = Field(420, description="Distância do voo em milhas")
    class_type: int = Field(1, description="Classe: 0 para Business, 1 para Econômica, 2 para Econômica Plus")
    seat_comfort: int = Field(5, description="Conforto do assento (1 a 5)")
    inflight_entertainment: int = Field(4, description="Entretenimento a bordo (1 a 5)")
    checkin_service: int = Field(4, description="Serviço de check-in (1 a 5)")
    inflight_service: int = Field(4, description="Serviço de bordo (1 a 5)")
    cleanliness: int = Field(4, description="Limpeza do voo (1 a 5)")
    departure_delay: int = Field(25, description="Atraso na partida em minutos")
    arrival_delay: float = Field(20.0, description="Atraso na chegada em minutos")


from pydantic import BaseModel, Field

class PassageiroViewSchema(BaseModel):
    """Define como um passageiro será retornado
    """
    name: str = Field("Maria", description="Nome do passageiro")
    age: int = Field(40, description="Idade do passageiro")
    gender: int = Field(1, description="Gênero: 0 para Feminino, 1 para Masculino")
    customer_type: int = Field(1, description="Tipo de cliente: 1 para Fiel, 0 para Não fiel")
    type_of_travel: int = Field(1, description="Tipo de viagem: 0 para Viagem a Negócios, 1 para Viagem Pessoal")
    flight_distance: int = Field(420, description="Distância do voo em milhas")
    class_type: int = Field(1, description="Classe: 0 para Business, 1 para Econômica, 2 para Econômica Plus")
    seat_comfort: int = Field(5, description="Conforto do assento (1 a 5)")
    inflight_entertainment: int = Field(4, description="Entretenimento a bordo (1 a 5)")
    checkin_service: int = Field(4, description="Serviço de check-in (1 a 5)")
    inflight_service: int = Field(4, description="Serviço de bordo (1 a 5)")
    cleanliness: int = Field(4, description="Limpeza do voo (1 a 5)")
    departure_delay: int = Field(25, description="Atraso na partida em minutos")
    arrival_delay: float = Field(20.0, description="Atraso na chegada em minutos")
    satisfaction: bool = Field(True, description="Satisfação: True para Satisfeito, False para Insatisfeito")
    
class PassageiroBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do passageiro.
    """
    name: str = "Maria"

class ListaPassageirosSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    passageiros: List[PassageiroSchema]

    
class PassageiroDelSchema(BaseModel):
    """Define como um passageiro para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um passageiro    
def apresenta_passageiro(passageiro: Passageiro):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassageiroViewSchema.
    """
    
    # Definir o valor de 'gender' com base nos atributos binários
    gender = 1 if passageiro.gender_male else 0

    # Definir o valor de 'customer_type' com base nos atributos binários
    customer_type = 1 if passageiro.customer_type_loyal else 0

    # Definir o valor de 'type_of_travel' com base nos atributos binários
    type_of_travel = 1 if passageiro.type_of_travel_personal else 0

    # Definir o valor de 'class_type' com base nos atributos binários
    if passageiro.class_business:
        class_type = 0
    elif passageiro.class_eco:
        class_type = 1
    else:
        class_type = 2

    return {
        "id": passageiro.id,  # ID do passageiro
        "name": passageiro.name,  # Nome do passageiro
        "age": passageiro.age,  # Idade do passageiro
        "gender (1 para Masculino, 0 para Feminino)": gender,  # Gênero: 1 para Masculino, 0 para Feminino
        "customer_type": customer_type,  # Tipo de cliente: 1 para Fiel, 0 para Não Fiel
        "type_of_travel": type_of_travel,  # Tipo de viagem: 1 para Pessoal, 0 para Negócios
        "flight_distance": passageiro.flight_distance,  # Distância do voo
        "class_type": class_type,  # Classe: 0 para Business, 1 para Econômica, 2 para Econômica Plus
        "seat_comfort": passageiro.seat_comfort,  # Conforto do assento (1 a 5)
        "inflight_entertainment": passageiro.inflight_entertainment,  # Entretenimento a bordo (1 a 5)
        "checkin_service": passageiro.checkin_service,  # Serviço de check-in (1 a 5)
        "inflight_service": passageiro.inflight_service,  # Serviço de bordo (1 a 5)
        "cleanliness": passageiro.cleanliness,  # Limpeza do voo (1 a 5)
        "departure_delay": passageiro.departure_delay,  # Atraso na partida (minutos)
        "arrival_delay": passageiro.arrival_delay,  # Atraso na chegada (minutos)
        "satisfaction": passageiro.satisfaction  # Satisfação: True para Satisfeito, False para Não Satisfeito

    }

    
# Apresenta uma lista de pacientes
def apresenta_passageiros(passageiros: List[Passageiro]):
    """ Retorna uma representação dos passageiros seguindo o schema definido em
        PassageiroViewSchema.
    """
    result = []
    for passageiro in passageiros:
        # Definir o valor de 'gender'
        gender = 1 if passageiro.gender_male else 0

        # Definir o valor de 'customer_type'
        customer_type = 1 if passageiro.customer_type_loyal else 0

        # Definir o valor de 'type_of_travel'
        type_of_travel = 1 if passageiro.type_of_travel_personal else 0

        # Definir o valor de 'class_type'
        if passageiro.class_business:
            class_type = 0
        elif passageiro.class_eco:
            class_type = 1
        else:
            class_type = 2

        result.append({
            "id": passageiro.id,
            "name": passageiro.name,
            "age": passageiro.age,
            "gender": gender,
            "customer_type": customer_type,
            "type_of_travel": type_of_travel,
            "flight_distance": passageiro.flight_distance,
            "class_type": class_type,
            "seat_comfort": passageiro.seat_comfort,
            "inflight_entertainment": passageiro.inflight_entertainment,
            "checkin_service": passageiro.checkin_service,
            "inflight_service": passageiro.inflight_service,
            "cleanliness": passageiro.cleanliness,
            "departure_delay": passageiro.departure_delay,
            "arrival_delay": passageiro.arrival_delay,
            "satisfaction": passageiro.satisfaction
        })

    return {"passageiros": result}
