# bot_concurseiro

### [PT/BR]

Este é um projeto de web-scrapping focado em adquirir informações sobre concursos públicos do Brasil. Atualmente está na versão que considero a Beta 1.0, com a seguinte configuração de funcionalidades:

- Roda diariamente pelo GitHub Actions;
- Retira os dados de um site focado em notícias de concursos;
- Busca e filtra os concursos listados por área / cargo;
- Envia mensagens para um canal pub/sub privado, APENAS quando há informações novas;
- Serviço Pub/Sub utilizado: [Ntfy](https://docs.ntfy.sh);
- Commita diariamente uma atualização do registro de dados captados.


Esta ferramenta continua sob melhoria constante, estou ativamente modificando e otimizando-a. 
Pretendo continuar trabalhando e mantendo este projeto ainda que como dev independente, então sinta-se a vontade para fazer um fork desse projeto e adaptá-lo às suas necessidades, ou deixar um comentário sugerindo alguma alteração / melhoria!

***

### [EN]

This is a web scrapping project focused on gathering information about Brazil's public tenders (concurso público). It is currently on what I consider to be the Beta 1.0 version, with the following configuration and functionalities:

- Runs on a daily basis over GitHub Actions;
- Gathers data from a website focused on public tender news;
- Searches and filters the tenders by area / role;
- Sends messages through a private pub/sub channel, ONLY when there is new information;
- Pub/Sub service in use: [Ntfy](https://docs.ntfy.sh)
- Daily commits an update of the retrieved data.


This tool is still under frequent updates, and I'm actively working on modifying and enhancing it.
I intend to continue working and maintaining this project, even if as a solo independent dev, so, feel free to fork it to adapt to your needs or leave a comment with your suggestion!

***

# Mensagem Exemplo // Example Message

<img width="869" height="343" alt="image" src="https://github.com/user-attachments/assets/12967389-01f9-41f6-bcee-3790b69b1a2a" />


[PT/BR]   Este é um exemplo de como a mensagem se parece no canal de notificação. O destaque em verde é um link que leva para a página do concurso no site de onde retiro os dados.

[EN]   This is an example of how the message looks like in the notification channel. The green highlight is a link that takes to the tender page within the site I scrapped the data from.
