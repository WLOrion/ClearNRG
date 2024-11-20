# ClearNRG
Esse repos é uma API Restful para implementar que implementa os conceitos visto na matéria de Banco de Dados na UNICAMP (MC536).

A API foi desenvolvida para atender ao objetivo de mapear o potencial energético de fontes renováveis no Brasil, alinhando-se ao Objetivo de Desenvolvimento Sustentável da ONU número 7: energia limpa e acessível. O Brasil, com vastos recursos naturais e um grande potencial renovável, enfrenta desafios como a dependência de hidrelétricas e a falta de planejamento para diversificar sua matriz energética. A proposta busca auxiliar a transição energética, utilizando dados geoespaciais, meteorológicos e de infraestrutura para identificar áreas ideais para a implementação de energia solar, eólica e outras fontes renováveis.

O sistema visa ajudar a criação de mapas temáticos, relatórios detalhados e dashboards que apoiem governos, empresas e comunidades locais na tomada de decisões sustentáveis com dados de fácil acesso. Com isso, espera-se impulsionar a expansão de projetos renováveis no Brasil, mitigando as mudanças climáticas e promovendo benefícios econômicos e sociais. As partes interessadas incluem agências governamentais, empresas do setor e populações de áreas remotas, contribuindo para a democratização do acesso à energia limpa no país.

## Banco de Dados

O schema presente em `database/schema.sql` foi desenvolvido pensando para ser executado em um servidor MySQL.

Caso necessário, segue um link com instruções para instanciar um servidor MySQL em sua máquina localmente.

- [Instruções](https://www.prisma.io/dataguide/mysql/setting-up-a-local-mysql-database)

Lembre-se de usar as instruções adequadas ao seu sistema operacional.

## Api

Para rodar o projeto é necessário primeiro instalar as dependências:

> pip install -r requirements.txt

Lembre de configurar um arquivo `.env` com as seguintes variáveis de ambiente:
 - MYSQL_USER -> Usuário do servidor
 - MYSQL_PASSWORD -> Senha relativa ao usuário utilizado
 - MYSQL_HOST -> IP de onde está o servidor (se estiver na mesma máquina, utilize `localhost`)
 - MYSQL_PORT -> Porta do servidor
 - MYSQL_DATABASE -> Nome do banco de dados utilizado

Logo após isso, podemos excutar o comando para iniciar o projeto:

> python -m uvicorn src.main:app --reload

E pronto, estará com a API funcionando e pronta para ajudar o gerenciamento energético do Brasil!