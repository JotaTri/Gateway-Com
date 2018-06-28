# Gateway-Com

Projeto que instancia um Servidor Web que permite a controle de servicos de um Gateway e pela criação de novos servicos a partir de formulas a serem executadas sobre os dados presentes no banco de dados do Gateway local.

## Instruções
Todos os pacotes necessários para executar esse programa está no arquivo '*requirements.txt*'.

Para instalação dos pacotes executar

```
pip install -r requirements.txt
```

A partir dos pacotes instalados, basta executar o arquivo *_main.py_* na raiz do projeto.

Para adição de novos pacotes ao arquivo, utilizar o *pipreqs*

_Instalação_
```
pip install pipreqs
```

_Atualização dos Pacotes_
```
//Estando na pasta raiz do Projeto
pipreqs . --force
```
## Endpoints

### /formulas

Endpoint encarregado pela criação de um serviço de integração de daods a partir da indicação de uma formula e um caminho a se encaminhar o resultado obtido.

Parametros

| Parametro | Descrição | Tipo | Obrigatoriedade |
|-|-|-|:-:|
| formula | Fórmula a ser executada seguindo sua sintaxe definida | String | :heavy_check_mark:
| topico | Caminho do tópico a ser enviado por MQTT o resultado da formula | String | :heavy_check_mark:
