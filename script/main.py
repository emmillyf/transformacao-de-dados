import pdfplumber
import pandas as pd
from zipfile import ZipFile
import os

def extrair_e_renomear(pdf_path, renomear):
   
    with pdfplumber.open(pdf_path) as pdf:
        tabelas = []
        for page in pdf.pages:
            tabelas.extend(page.extract_tables())  

    tabelas_renomeadas = [] 

    if tabelas:
        for tabela in tabelas:
            df = pd.DataFrame(tabela[1:], columns=tabela[0])

            # Verifica se a coluna existe nas tabelas e dá o nome novo à coluna atual(antiga) para cada coluna nova no dicionario "renomear"
            #  ele troca o valor de cada coluna "coluna_atual" das tabelas.
            colunas_atuais = {nome_antigo: nome_novo for nome_antigo, nome_novo in renomear.items() if nome_antigo in df.columns}
    
            if colunas_atuais:
                df.rename(columns=colunas_atuais, inplace=True)

            if "Procedimento" in df.columns:
                df.dropna(subset=["Procedimento"], inplace=True)  

            # Remover linhas completamente vazias
            df.dropna(how="all", inplace=True)

            tabelas_renomeadas.append(df)
        return tabelas_renomeadas

def salvar_csv(tabelas_renomeadas, diretorio_saida = "data/saida"):
   
    if tabelas_renomeadas:
        os.makedirs(diretorio_saida, exist_ok=True)
        
        tabelas_renomeadas_completas = pd.concat(tabelas_renomeadas, ignore_index=True)
        caminho_unico = os.path.join(diretorio_saida, "Anexo_I_Completo.csv")

        tabelas_renomeadas_completas.to_csv(caminho_unico, sep=';', index=False, encoding='utf-8-sig')
        return [caminho_unico]
    return []

def main():
    pdf_path = os.path.join(os.getcwd(), "data", "entrada", "Anexo_I.pdf")

    renomear = {
    "OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"
    }

    tabelas_renomeadas = extrair_e_renomear(pdf_path, renomear)
    salvar_csv(tabelas_renomeadas)
  

if __name__ == "__main__":
    main()