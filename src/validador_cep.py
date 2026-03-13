import pandas as pd
import re

def validar_cep(cep_input:str, cidade_input:str, df:pd.DataFrame):
    
    cep_input = cep_input.strip()
    
    cidade_input = cidade_input.strip()
    
    cep_regex = r'^[0-9]{5}[-]?[0-9]{3}$'
    
    cidade_regex = r'^[A-Za-zÀ-ÿ]+(?:[ -][A-Za-zÀ-ÿ]+)*$'    
    
    if(not re.match(cep_regex, cep_input)):
        return False
    
    try:
        normalized_cep = cep_input.replace('-', '')
        cep_int:int = int(normalized_cep)
        condicao_cep = (cep_int >= df['CEP_INICIAL']) & (cep_int <= df['CEP_FINAL'])
    except ValueError:
        return False
        
        
    if(not re.match(cidade_regex, cidade_input)):
        return False
        
    
    if(not condicao_cep.any()):
        return False
        
    df_linha = df.loc[condicao_cep]
    df_cidade = df_linha['LOCALIDADE'].iloc[0].casefold()
    
    cidade_normalized = cidade_input.casefold()
    
    return cidade_normalized == df_cidade



