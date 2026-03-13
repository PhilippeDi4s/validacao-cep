import pandas as pd
import re

def validar_cep(cep_input:str, cidade_input:str, df:pd.DataFrame):
    
    cep_regex = r'^[0-9]{5}[-]?[0-9]{3}$'
    
    cidade_regex = r'^[A-Za-zÀ-ÿ]+(?:\s[A-Za-zÀ-ÿ]+)*$'    
    
    if(not re.match(cep_regex, cep_input)):
        print('=' * 10)
        print('O formato do cep inserido está incorreto')
        print('=' * 10)
        return False
    
    try:
        normalized_cep = cep_input.replace('-', '')
        cep_int:int = int(normalized_cep)
        condicao_cep = (cep_int >= df['CEP_INICIAL']) & (cep_int <= df['CEP_FINAL'])

    
    except ValueError:
        print('=' * 10)
        print('O formato do cep inserido está incorreto')
        print('=' * 10)
        return False
        
        
        
    if(not re.match(cidade_regex, cidade_input)):
        print('=' * 10)
        print('Cidade inválida')
        print('=' * 10)
        return False
        
    if(condicao_cep.any()):
        df_linha = df.loc[condicao_cep]
        df_cidade = df_linha['LOCALIDADE'].iloc[0]
        if(cidade_input == df_cidade):
            print('=' * 10)
            print(f'Você digitou: {cidade_input} | E a localidade so CEP é: {df_cidade}')
            print('Cadastro feito, programa finalizado')
            print('=' * 10)
            return True
        else:
            return False
    else:
        print('=' * 10)
        print('O CEP inserido não está cadastrado no sistema!')
        print('=' * 10)
        return False



