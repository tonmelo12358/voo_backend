from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


info = Info(title="Voo API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
passageiro_tag = Tag(name="Passageiro", description="Adição, visualização e remoção de Passageiros à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de passageiros
@app.get('/passageiros', tags=[passageiro_tag],
         responses={"200": PassageiroViewSchema, "404": ErrorSchema})
def get_passageiros():
    """Lista todos os passageiros cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de passageiros cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os passageiros")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os passageiros
    passageiros = session.query(Passageiro).all()
    
    if not passageiros:
        # Se não houver passageiros
        return {"passageiros": []}, 200
    else:
        logger.debug(f"%d passageiros econtrados" % len(passageiros))
        return apresenta_passageiros(passageiros), 200
    
    


# Rota de adição de avaliação de passageiro
@app.post('/passageiro', tags=[passageiro_tag], responses={"200": PassageiroViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PassageiroSchema):
    """Adiciona um novo passageiro à base de dados e realiza a predição de satisfação."""

    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    
    # Carregando o pipeline
    rf_pipeline_path = './Machine Learning/pipelines/rf_voo_pipeline.pkl'
    pipeline = Pipeline.carrega_pipeline(rf_pipeline_path)

    # Verifica se o pipeline foi carregado corretamente
    if pipeline is None:
        return {"message": "Erro ao carregar o pipeline."}, 500

    print("Pipeline carregado com sucesso.")

    # Log para verificar como os dados estão sendo escalonados
    rescaled_input = pipeline.named_steps['scaler'].transform(X_input)
    print(f"Dados de entrada escalonados: {rescaled_input}")

    # Predição isolada pelo modelo RandomForest
    model = pipeline.named_steps['rf']
    prediction = model.predict(rescaled_input)
    print(f"Predição isolada pelo modelo RandomForest: {prediction}")

    # Exibir as importâncias das features
    importances = model.feature_importances_
    for i, importance in enumerate(importances):
        print(f"Importância da feature {i}: {importance}")


    # Realizando a predição
    satisfaction = int(Model.realiza_predicao(pipeline, X_input)[0])
    print(f"Resultado da predição bruta: {Model.realiza_predicao(pipeline, X_input)}")
    print(f"Satisfaction predito: {satisfaction}")


    # Criando um novo objeto Passageiro diretamente a partir do form e da predição
    passageiro = Passageiro(
        name=form.name,
        age=form.age,
        gender_female=form.gender == 0,  # Calculando com base no campo gender
        gender_male=form.gender == 1,    # Calculando com base no campo gender
        customer_type_loyal=form.customer_type == 1,
        customer_type_disloyal=form.customer_type == 0,
        type_of_travel_business=form.type_of_travel == 0,
        type_of_travel_personal=form.type_of_travel == 1,
        flight_distance=form.flight_distance,
        class_business=form.class_type == 0,
        class_eco=form.class_type == 1,
        class_eco_plus=form.class_type == 2,
        seat_comfort=form.seat_comfort,
        inflight_entertainment=form.inflight_entertainment,
        checkin_service=form.checkin_service,
        inflight_service=form.inflight_service,
        cleanliness=form.cleanliness,
        departure_delay=form.departure_delay,
        arrival_delay=form.arrival_delay,
        satisfaction=satisfaction
    )
    
    
    logger.debug(f"Adicionando passageiro de nome: '{passageiro.name}'")
    
    try:
        session = Session()
        if session.query(Passageiro).filter(Passageiro.name == form.name).first():
            error_msg = "Passageiro já existente na base."
            logger.warning(f"Erro ao adicionar passageiro '{passageiro.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        session.add(passageiro)
        session.commit()
        logger.debug(f"Passageiro '{passageiro.name}' adicionado com sucesso.")
        return apresenta_passageiro(passageiro), 200
    
    except IntegrityError as e:
        session.rollback()
        error_msg = "Erro de integridade ao salvar passageiro."
        logger.error(f"Erro: {error_msg} - {str(e)}")
        return {"message": error_msg}, 400
    
    except Exception as e:
        session.rollback()
        error_msg = "Erro ao adicionar passageiro."
        logger.error(f"Erro ao adicionar passageiro '{passageiro.name}': {str(e)}")
        return {"message": error_msg}, 400


# Métodos baseados em nome
# Rota de busca de passageiro por nome
@app.get('/passageiro', tags=[passageiro_tag],
         responses={"200": PassageiroViewSchema, "404": ErrorSchema})
def get_passageiro(query: PassageiroBuscaSchema):    
    """Faz a busca por um passageiro cadastrado na base a partir do nome

    Args:
        nome (str): nome do passageiro
        
    Returns:
        dict: representação do passageiro e avaliação associada
    """
    
    passageiro_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{passageiro_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    passageiro = session.query(Passageiro).filter(Passageiro.name == passageiro_nome).first()
    
    if not passageiro:
        # se o passageiro não foi encontrado
        error_msg = f"Passageiro {passageiro_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar passageiro '{passageiro_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Passageiro econtrado: '{passageiro.name}'")
        # retorna a representação do passageiro
        return apresenta_passageiro(passageiro), 200
   


# Rota de remoção de passageiro por nome
@app.delete('/passageiro', tags=[passageiro_tag],
            responses={"200": PassageiroViewSchema, "404": ErrorSchema})
def delete_passageiro(query: PassageiroBuscaSchema):
    """Remove um passageiro cadastrado na base a partir do nome

    Args:
        nome (str): nome do passageiro
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    passageiro_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre passageiro #{passageiro_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando passageiro
    passageiro = session.query(Passageiro).filter(Passageiro.name == passageiro_nome).first()
    
    if not passageiro:
        error_msg = "Passageiro não encontrado na base :/"
        logger.warning(f"Erro ao deletar passageiro '{passageiro_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(passageiro)
        session.commit()
        logger.debug(f"Deletado passageito #{passageiro_nome}")
        return {"message": f"Passageiro {passageiro_nome} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)