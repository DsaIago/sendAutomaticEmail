import os
import pickle
import schedule
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import time
from enviarEmail import enviar_email

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SPREADSHEET_ID = "link_planilha"
RANGE_NAME = "Digitação!A1:BC"
ID_COLUMN = "ID"  # Nome da coluna de ID
STATUS_COLUMN = "Status1"  # Nome da coluna de status
EMAIL_COLUMN = "Seu email"  # Nome da coluna de email
ID_THRESHOLD = 4761
parcela = "12x de R$ 159,00"
def obter_dados_google_sheets():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        valores = result.get("values", [])
        if not valores:
            print("Nenhum dado encontrado.")
            return None
        else:
            colunas = valores[0]
            dados = valores[1:]
            df = pd.DataFrame(dados, columns=colunas)
            return df
    except HttpError as err:
        print(err)
        return None

def verificar_mudancas(df_antigo, df_novo):
    mudancas = pd.DataFrame()
    if df_antigo is not None:
        df_antigo[ID_COLUMN] = df_antigo[ID_COLUMN].astype(int)
        df_novo[ID_COLUMN] = df_novo[ID_COLUMN].astype(int)
        merged = df_novo.merge(df_antigo, on=ID_COLUMN, suffixes=('', '_old'))
        mudancas = merged[merged[STATUS_COLUMN] != merged[f"{STATUS_COLUMN}_old"]]
    return mudancas

def main():
    print("Iniciando o script...")
    
    df_antigo = None
    if os.path.exists("estado_antigo.pkl"):
        with open("estado_antigo.pkl", "rb") as f:
            df_antigo = pickle.load(f)
    
    df_novo = obter_dados_google_sheets()
    if df_novo is not None:
        print(f"Dados obtidos: {df_novo.shape[0]} registros antes da filtragem.")
        
        df_novo = df_novo[pd.to_numeric(df_novo[ID_COLUMN], errors='coerce').notna()]
        df_novo[ID_COLUMN] = df_novo[ID_COLUMN].astype(int)
        df_novo = df_novo[df_novo[ID_COLUMN] >= ID_THRESHOLD]
        
        print(f"Dados obtidos: {df_novo.shape[0]} registros após filtragem.")

        mudancas = verificar_mudancas(df_antigo, df_novo)
        print(f"Encontradas {mudancas.shape[0]} mudanças.")

        for _, linha in mudancas.iterrows():
            email = linha[EMAIL_COLUMN]
            status_novo = linha[STATUS_COLUMN]  
            nome_cliente = linha["Nome Completo"]
            cpf_cliente = linha["CPF"]
            id_cliente = linha[ID_COLUMN]
            codigo_card = linha["Código"] 
            nome_consultor = linha["Seu nome completo"]
            valor_liberado = linha["Valor liberado"]
            data_vencimento = linha["Data 1 vencimento"]
            motivos = linha["Observação 2"]
            enviar_email(email, nome_cliente, cpf_cliente, status_novo, id_cliente, codigo_card, 
            nome_consultor,valor_liberado, parcela, data_vencimento, motivos)
            print(f"Email enviado para {email} sobre a mudança de status.")
        with open("estado_antigo.pkl", "wb") as f:
            pickle.dump(df_novo, f)
schedule.every(10).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(5)
