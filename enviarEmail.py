import smtplib
import email.message

def enviar_email(destinatario, nome_cliente, cpf_cliente, status_atual, id_cliente, codigo_card, nome_consultor, valor_liberado, parcela,
    data_vencimento, motivos, ):
    if int(id_cliente) < 4760:
        print(f"ID do cliente ({id_cliente}) não atende ao critério para envio de e-mails.")
        return
    if status_atual == "Em atuação":
        print(f"O status da proposta ID {codigo_card} está 'Em atuação'. Nenhum e-mail será enviado.")
        return
    
    numero_whatsapp = "+5,...."
    assinatura = f"""
    <hr style="border-top: 1px solid #000;">
    <p style="text-align: center; font-weight: bold;">ATENÇÃO ESSE É UM EMAIL AUTOMÁTICO. NÃO RESPONDA.</p>
    <p style="text-align: center; font-style: italic;">Caso precise de mais informações entre em contato com o nosso suporte. 
    <a href="https://wa.me/{numero_whatsapp}" target="_blank"><img src="https://img.icons8.com/?size=100&id=7OeRNqg6S7Vf&format=png&color=000000/icons8-whatsapp.gif" alt="WhatsApp" style="width: 20px; height: 20px; vertical-align: middle;"></a></p>
    """
    
    assunto = f"DITTO | Acompanhamento automático - Empréstimo Gov - {nome_cliente} - ID {codigo_card}"
    
    link_material_apoio = "..."
    
    if status_atual == "Andamento":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Valor liberado: {valor_liberado}<br>
        Parcela: {parcela}<br>
        Data do 1° vencimento: {data_vencimento}<br>
        Status atual: {status_atual}</p>
        """ + assinatura 
        
    elif status_atual == "Cancelado":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Status atual: {status_atual}<br>
        Motivo: {motivos}</p>
        
        <p><a href="{link_material_apoio}">Clique aqui</a> para acessar o material de apoio.</p>

        """ + assinatura
    elif status_atual == "Aguardando formalização":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
         <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Valor liberado: {valor_liberado}<br>
        Parcela: {parcela}<br>
        Data do 1° vencimento: {data_vencimento}<br>
        Status atual: {status_atual}</p>
        
        <p>Sua proposta está <strong>Aguardando a formalização do cliente</strong>. 
        Caso o cliente tenha recebido um SMS da Crefisa é só ele seguir o link para fazer a formalização pela <strong>Cris - WhatsApp Oficial de formalização da Crefisa.</strong> 
        Caso ele não tenha recebido é só pedir para ele chamar o número <strong>(11) 98806-0603</strong>
        Após a formalização você receberá outro email informando sobre a atualização dos status dessa proposta.</p>
        """ + assinatura
    elif status_atual == "Pendente":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Valor liberado: {valor_liberado}<br>
        Parcela: {parcela}<br>
        Data do 1° vencimento: {data_vencimento}
        Status atual: {status_atual}<br>
        Motivo da pendência: {motivos}</p>
        
        <p>Entre em contato com o nosso suporte com os documentos e informações necessárias para corrigirmos a pendendência.<p> 
        <p>Atenção: A proposta será cancelada em 48h caso não tenha atuação!</p>
        <p>Você receberá outro email informando sobre a atualização dos status dessa proposta.</p>
        """ + assinatura
    elif status_atual == "Reanálise":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Status atual: {status_atual}</p>
        """ + assinatura
    elif status_atual == "Pago":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Valor liberado: {valor_liberado}<br>
        Parcela: {parcela}<br>
        Data do 1° vencimento: {data_vencimento}<br>
        Status atual: {status_atual}</p>
        
        <p>Parabéns sua proposta foi <strong>paga</strong> ao cliente!!</p>
        """ + assinatura
    elif status_atual == "Aprovado":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Status atual: {status_atual}</p>
        
        <p>Sua proposta foi aprovada e está na esteira de pagamento, o pagamento é feito via TED em até 48h úteis.</p>
        <p>Você receberá outro email informando sobre a atualização dos status dessa proposta.</p><br><br>
        
        """ + assinatura
        
    elif status_atual == "Em atuação":
        corpo_email = f"""
        <p>Olá {nome_consultor} , tudo bem?</p>
        <p>A sua proposta de Empréstimo Gov ID {codigo_card} mudou de fase, segue informações abaixo:</p>
        
        <p>Nome do cliente: {nome_cliente}<br>
        CPF: {cpf_cliente}<br>
        Status atual: {status_atual}</p>
        
        <p>Sua proposta foi aprovada e está na esteira de pagamento, o pagamento é feito via TED em até 48h úteis.</p>
        <p>Você receberá outro email informando sobre a atualização dos status dessa proposta.</p><br><br>
        
        """ + assinatura
        
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = 'naoresponda@sejaditto.com.br'
    msg['To'] = destinatario
    password = 'ldchfwzhctqqkquf' 
    msg.add_header('Content-Type', 'text/html; charset=utf-8')
    msg.set_payload(corpo_email.encode('utf-8')) 

    try:
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login('iago.almeida@sejaditto.com.br', password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        s.quit()
        print('Email enviado')
    except Exception as e:
        print(f"Falha ao enviar email: {e}")
