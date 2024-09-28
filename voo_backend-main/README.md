# API Satisfação de Voo

Este projeto faz parte da Disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** da pós graduação em Engenharia de Software da PUC-RIO.

O objetivo é criar treinar um modelo de machine learning utilizando um dataset escolhido pelo aluno e utilizar esse modelo treinado em uma aplicação no padrão MVC composta de API e um front-end.

O dataset escolhido para este projeto é de análise para satisfação de voo. Nele existem diversas informações colhidas com os passageiros (desde informações pessoais, como informações de experiência pré-voo e durante o voo), em que os passageiros contam como foi a experiência daquele voo, e no final eles indicam se ficaram satisfeitos ou não com a experiência.

A aplicação que utiliza este modelo treinado possui um formulário para que possamos inserir dados de experiência de um voo, e baseado nessas informações inseridas podemos determinar com grande precisão se a experiência foi satisfatória ou não.


## Como executar

Para executar a aplicação devemos realizar 3 passos. O primeiro é o treinamento do modelo. O segundo é rodar o teste de acuráciae o terceiro é rodar a aplicação.

### Passo 1: Treinamento do modelo

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

 É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para criação de ambiente virtual, execute o seguinte comando:

```
python3 -m venv env  (ou outro nome de ambiente que você preferir)
```
Para ativar o ambiente virtual execute o seguinte comando:
```
source env/bin/activate
```
O comando a seguir instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.
```
(env)$ pip install -r requirements.txt
```
Após a criação do ambiente vamos realizar o treinamento do modelo. Para esta ação existe um notebook com todo o código de treinamento para exeecução.

O código do treinamento do modelo está na pasta "Notebook" dentro da pasta de "Machine Learning". Segue o path: 
```
./Machine Learning/notebook/Treinamento_Dataset_Voo_novo.ipynb
```
Execute todos os passos descritos no notebook.
#### Nota: 
O modelo que obteve os melhores indicadores e foi escolhido para este projeto é o Random Forester. Foram analisados diversos modelos e este foi o que se saiu melhor. Como exercídio fiz otimização de hiperparâmetros para todos os modelos treinados mas para o código final optei por fazer a otimização apenas do modelo escolhido.

Execute todos os códigos de treinamento e salve os arquivos (bloco "Salvando"). Após salvar o código o modelo estará pronto para uso.

### Passo 2: Teste de acurácia
Como parte do MVP foi criado um código de teste para verificar a acurácia do modelo. O nome do arquivo é test_modelos.py
Para testar a acurácia do modelo, execute o seguinte comando:
```
pytest -v test_modelos.py
```
### Passo 3: Execução da aplicação
Após a criação do ambiente virtual, instalação os arquivos/bibliotecas de requirements.txt, treinamento do modelo e teste de acurácia, vamos à execução da aplicação. Basta executar a API com o seguinte comando:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução. Você será redirecionado para Swagger, onde terá acesso às documentações das APIs.

## Como funciona o Back end

O Back end é composto por um banco de dados Sqlite3 com um tabela chamada **passageiros**. Ela guarda todas os passageiros analisados e as respostas das análises.
Para operações de leitura e escrita no banco foram criadas rotas, que estão escritas no arquivo principal do código (app.py).
foram criadas as seguintes rotas:

-  **get passageiros**: Retorna uma representação da listagem de todos os passageiros cadastrados no banco;
- **get passageiro**: Faz a busca por um passageiro a partir do nome dele (em trabalhos anteriores utilizei o ID como atributo de busca. Como este projeto tem como foco a utilização de ML utilizei o nome para simplificar o código do back end).
- **post passageiro**: Adiciona um novo passageiro e a respectiva análise de satisfação no banco de dados.
- **delete correlacao**: Exclui um passageiro a partir do atributo nome.

## Melhoria Contínua  
  
Este trabalho é um MVP de pós-graduação. O objetivo principal aqui é aplicar os conhecimentos adquiridos no módulo de Qualidade de Software, Segurança e Sistemas Inteligentes, em que foram tratados os temas de Machine Learning, segurança e testes de software, utilizando a linguagem python como base, Bancos de Dados e tópicos de desenvolvimento.

Alguns pontos foram identificados mas não foram tratados neste projetos. Segue proposta de melhorias para o Satisfação de Voo:

- Página de login.
- Página de Admin para gestão de acessos e perfis.
- O dataset analisado é muito grande (3MB). Para utilização neste MVP precisei reduzir a quantidade de dados a serem treinados. Acredito que o treinamento de toda a massa de dados pode gerar resultados mais precisos.

## Sobre o autor 

O autor deste projeto é Wellington Melo (Ton Melo), Global MBA, engenheiro eletricista com especialização em engenharia de automação. No momento da criação deste projeto atuo como líder de arquitetura de tecnologia na Globo e estou buscando conhecimento mais profundo em arquitetura e desenvolvimento de sistemas de TI.