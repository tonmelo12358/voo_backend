from sqlalchemy import Column, String, Integer, Float, Boolean
from model import Base

class Passageiro(Base):
    __tablename__ = 'passageiros'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Informações sobre o passageiro
    name = Column("Name", String(50))
    age = Column("Age", Integer, nullable=False)
    gender_female = Column("Gender_Female", Boolean, nullable=False)
    gender_male = Column("Gender_Male", Boolean, nullable=False)
    customer_type_loyal = Column("Customer_Type_Loyal_Customer", Boolean, nullable=False)
    customer_type_disloyal = Column("Customer_Type_Disloyal_Customer", Boolean, nullable=False)

    # Informações sobre a viagem
    type_of_travel_business = Column("Type_of_Travel_Business", Boolean, nullable=False)
    type_of_travel_personal = Column("Type_of_Travel_Personal", Boolean, nullable=False)
    flight_distance = Column("Flight_Distance", Integer, nullable=False)
    class_business = Column("Class_Business", Boolean, nullable=False)
    class_eco = Column("Class_Eco", Boolean, nullable=False)
    class_eco_plus = Column("Class_Eco_Plus", Boolean, nullable=False)
    
    # Informações de serviço e conforto
    seat_comfort = Column("Seat_Comfort", Integer, nullable=False)
    inflight_entertainment = Column("Inflight_Entertainment", Integer, nullable=False)
    checkin_service = Column("Checkin_Service", Integer, nullable=False)
    inflight_service = Column("Inflight_Service", Integer, nullable=False)
    cleanliness = Column("Cleanliness", Integer, nullable=False)
    departure_delay = Column("Departure_Delay_in_Minutes", Integer, nullable=False)
    arrival_delay = Column("Arrival_Delay_in_Minutes", Integer, nullable=False)
    satisfaction = Column("Satisfaction", Boolean, nullable=False)

    def __init__(self, name: str, age: int, gender_female: bool, gender_male: bool, customer_type_loyal: bool, 
                 customer_type_disloyal: bool, type_of_travel_business: bool, type_of_travel_personal: bool, 
                 flight_distance: int, class_business: bool, class_eco: bool, class_eco_plus: bool, seat_comfort: int, 
                 inflight_entertainment: int, checkin_service: int, inflight_service: int, cleanliness: int, 
                 departure_delay: int, arrival_delay: int, satisfaction: bool):
        """
        Cria um objeto Passageiro com informações relevantes
        """
        self.name = name
        self.age = age
        self.gender_female = gender_female
        self.gender_male = gender_male
        self.customer_type_loyal = customer_type_loyal
        self.customer_type_disloyal = customer_type_disloyal
        self.type_of_travel_business = type_of_travel_business
        self.type_of_travel_personal = type_of_travel_personal
        self.flight_distance = flight_distance
        self.class_business = class_business
        self.class_eco = class_eco
        self.class_eco_plus = class_eco_plus
        self.seat_comfort = seat_comfort
        self.inflight_entertainment = inflight_entertainment
        self.checkin_service = checkin_service
        self.inflight_service = inflight_service
        self.cleanliness = cleanliness
        self.departure_delay = departure_delay
        self.arrival_delay = arrival_delay
        self.satisfaction = satisfaction

def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender_female": self.gender_female,
            "gender_male": self.gender_male,
            "customer_type_loyal": self.customer_type_loyal,
            "customer_type_disloyal": self.customer_type_disloyal,
            "type_of_travel_business": self.type_of_travel_business,
            "type_of_travel_personal": self.type_of_travel_personal,
            "flight_distance": self.flight_distance,
            "class_business": self.class_business,
            "class_eco": self.class_eco,
            "class_eco_plus": self.class_eco_plus,
            "seat_comfort": self.seat_comfort,
            "inflight_entertainment": self.inflight_entertainment,
            "checkin_service": self.checkin_service,
            "inflight_service": self.inflight_service,
            "cleanliness": self.cleanliness,
            "departure_delay": self.departure_delay,
            "arrival_delay": self.arrival_delay,
            "satisfaction": self.satisfaction
        }