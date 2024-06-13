🚀 Notificando Status de Propostas com Python 🚀

Gostaria de compartilhar um projeto recente que desenvolvi utilizando Python. O objetivo principal do projeto é automatizar o acompanhamento de propostas e notificar os usuários sobre o status atualizado das mesmas. Essa solução utiliza diversas bibliotecas e ferramentas, incluindo integração com Google Sheets e envio de emails automatizados. 🌐📧

📜 Visão Geral do Projeto:
1. Coleta de Dados:

◾ Utilização das bibliotecas google-auth e google-api-python-client para acessar uma planilha do Google Sheets que contém os dados das propostas.

◾Os dados são filtrados e processados para identificar propostas relevantes e alterações de status.

2. Identificação de Mudanças:

◾Comparação entre o estado atual e o estado anterior das propostas para detectar mudanças significativas.

◾Uso de pandas para manipulação e análise dos dados.

3. Envio de Notificações:

◾ Envio de emails automáticos utilizando smtplib e email.message para notificar os responsáveis sobre a mudança de status das propostas.

◾ Diferentes templates de email são utilizados para cada tipo de status, garantindo uma comunicação clara e eficaz.

📚 Tecnologias Utilizadas:
◾ Python: Linguagem de programação principal.
◾ Google Sheets API: Para leitura dos dados das propostas.
◾ Pandas: Para manipulação e análise de dados.
◾ Smtplib e Email: Para envio de emails automáticos.
◾ Schedule: Para agendamento e execução periódica do script.

💡 Benefícios:
◾ Eficiência: Automatização do processo de acompanhamento de propostas, economizando tempo e esforço manual.

◾Precisão: Garantia de que as notificações sejam enviadas com informações atualizadas e corretas.

◾Personalização: Templates de email personalizados para diferentes status, melhorando a comunicação com os usuários.

hashtag#Python hashtag#Automação hashtag#GoogleSheetsAPI hashtag#EmailAutomation hashtag#DataAnalysis hashtag#Projetos
