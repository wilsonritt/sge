# Projeto de Sistema de Gestão de Estoque

Este é um projeto de sistema de gestão de estoque desenvolvido com Django, feito para acompanhar um curso de desenvolvimento. O sistema visa auxiliar empresas a gerenciar de forma eficiente seus estoques, oferecendo funcionalidades de registro, consulta e atualização de produtos.

## Motivação

Este projeto foi criado com o objetivo de consolidar conhecimentos sobre o framework Django e boas práticas no desenvolvimento de sistemas de gerenciamento. O sistema de gestão de estoque é uma aplicação prática que simula cenários reais de gerenciamento de recursos, permitindo um aprendizado abrangente nas áreas de banco de dados, interface de usuário e lógica de negócios. A ideia é que o sistema seja funcional, intuitivo e, ao mesmo tempo, um showcase de habilidades no desenvolvimento de software.

## Funcionalidades

- **Cadastro e gerenciamento de produtos**: Criação, atualização, visualização e exclusão de produtos.
- **Controle de inventário**: Controle de entrada e saída de estoque com logs detalhados.
- **Relatórios e visualização de dados**: Geração de relatórios básicos para acompanhar a movimentação e status dos produtos.
- **Interface de usuário amigável**: Interface desenvolvida com Django Template Language para fácil navegação.
- **API REST**: Integração com Django REST Framework para acesso e manipulação dos dados de forma programática.

## Tecnologias Utilizadas

- **Django**: Framework principal para o desenvolvimento do backend, com uma estrutura robusta e flexível.
- **Django ORM**: Utilizado para manipulação e gerenciamento de dados de forma eficiente.
- **Django REST Framework**: Implementação da API REST para fornecer uma interface programática ao sistema.
- **SQLite**: Banco de dados escolhido para facilitar a configuração e uso, ideal para projetos de pequeno e médio porte.
- **HTML5 e CSS3**: Para criação da interface de usuário.
- **Bootstrap**: Framework CSS para tornar a interface responsiva e moderna.
- **Django Template Language**: Para construção das páginas front-end, integrando dados de backend de forma dinâmica.

## Abordagens Técnicas

- **Estruturação em Apps**: O projeto é modular, organizado em aplicações Django específicas para cada funcionalidade principal (produtos, estoque, relatórios), facilitando a escalabilidade e manutenção.
- **MVC (Model-View-Controller)**: Estruturação das camadas de apresentação, lógica de negócios e manipulação de dados de maneira organizada.
- **API RESTful**: O uso do Django REST Framework permite que o sistema se comunique com outras aplicações e interfaces, oferecendo endpoints para operações de CRUD.
- **Validação de Formulários**: Implementação de validações no backend para garantir a integridade e qualidade dos dados inseridos.
- **Autenticação e Autorização**: Uso do sistema de autenticação do Django para controlar o acesso ao sistema e proteger as informações sensíveis.

## Como Rodar o Projeto

### Pré-requisitos

- **Python 3.x**
- **Pip** (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/inventory-management.git
   cd inventory-management
   ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # no Windows, use `venv\Scripts\activate`
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Realize as migrações iniciais:
    ```bash
    python manage.py migrate
    ```
5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```
6. Acesse o sistema em http://localhost:8000.

## Contribuições

Sinta-se à vontade para enviar sugestões, correções e melhorias. Este projeto está em constante evolução para se tornar um recurso cada vez mais completo e funcional.
