# Desafio Back-end SEOGPT

Primeiramente, obrigado pelo seu interesse em trabalhar na SEOGPT!
Abaixo você encontrará todas as informações necessárias para iniciar o seu teste.

## Avisos antes de começar

- Leia com atenção este documento todo e tente seguir ao **máximo** as instruções;
- Clone esse repositório, e pode subir como um commit por aqui mesmo.
- Você poderá consultar o Google, Stackoverflow, ChatGPT. Importa muito mais sua capacidade de resolver problemas dinâmicamente, e não os métodos que você usa para isso.
- Dê uma olhada nos [Materiais úteis](#materiais-úteis);
- Fique à vontade para perguntar qualquer dúvida aos recrutadores;
- Fique tranquilo, respire, assim como você, também já passamos por essa etapa. Boa sorte! :)
- Após terminar, suba o commit com um readme explicando a logística da sua aplicação.

### Sobre o ambiente da aplicação:

- Crie um container de Docker para rodar sua aplicação.

- A linguagem principal usada deve ser python. É aceítavel criar scripts menores como em Javascript para ingestão de páginas, mas o core da aplicação deve ser feito em Python.

- Escolha qualquer framework tanto de back-end e front-end que se sinta **confortável** em trabalhar. Esse teste **não faz** nenhuma preferência,
  portanto decida por aquele com o qual estará mais seguro em apresentar e conversar com a gente na entrevista ;)

- Não se preocupe com o Design do Front-End. Queremos saber sua habilidade de resolver os problemas, não de fazer uma interface bonitinha.

## Objetivo: Knowledge Extractor

O Knowledge Extractor é um aplicativo que permite enviar uma URL de um site, que será lida e processada por uma IA para criar um resumo para estudos. A ideia é possibilitar que qualquer página da internet possa ser convertida em conhecimento valioso de forma simples.

### Requisitos

A seguir estão algumas regras de negócio que são importantes para o funcionamento do SEOGPT Knowledge Extractor:

- Use a linguagem Python;
- Utilize LangChain e ChatGPT 3.5 para processamento de linguagem natural;
- Entre em contato com o recrutador para obter uma chave da OPENAI a ser usada nesse teste (limite de $10 de gasto);
- O aplicativo deve permitir o envio de uma URL de um site e retornar um resumo do conteúdo da página;
- O resumo deve ser criado em Markdown, e poder facilitar o aprendizado.
- O input deve ser dinâmico, e aceitar vários tipos de página da internet:
- - Páginas de documentação de Código
- - Páginas da Wikipédia
- - Artigos de Jornais online
- - Páginas de Papéis Científicos

### Adicionais legais:

- Conseguir utilizar imagens dentro ou fora da página para os resumos.
- Estrutura formatada de Markdown para o resumo

### Materiais úteis

- [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
- [OpenAI API Documentation](https://beta.openai.com/docs/)
- [Docker Documentation](https://docs.docker.com/)

## Instruções para envio

- Clone o repositório disponibilizado pelo recrutador.
- Crie uma branch com seu nome e sobrenome, por exemplo, `fulano_silva`.
- Implemente sua solução, fazendo commits regulares com mensagens claras sobre o que foi implementado em cada etapa.
- Ao finalizar, suba a branch e envie um pull request.
- Inclua um README com explicações detalhadas sobre a solução implementada, como rodar o projeto, decisões de design, entre outros pontos que julgar relevantes.

## Critérios de Avaliação

- **Funcionalidade**: O aplicativo funciona conforme esperado? Atende a todos os requisitos especificados?
- **Código**: O código é limpo, organizado e bem documentado?
- **Docker**: A aplicação roda corretamente dentro de um container Docker?
- **Inovação**: O candidato implementou alguma funcionalidade extra ou tomou decisões criativas que agregam valor ao projeto?
- **README**: O arquivo README é claro e fornece todas as informações necessárias para entender e executar o projeto?

Boa sorte! Estamos ansiosos para ver sua solução!
