import pandas as pd
import pytest
from src.validador_cep import validar_cep

df_test = pd.DataFrame({
    "CEP_INICIAL": [77470000],
    "CEP_FINAL": [ 77474999],
    "LOCALIDADE": ["Formoso do Araguaia"]
})

@pytest.mark.parametrize('cep, cidade, esperado',
                         [
                             ('77474999', 'São Paulo', False),
                             ('87474999', 'Formoso do Araguaia', False),
                             ('77470000', 'Formoso do Araguaia', True),
                         ])

def test_validacao_cep(cep, cidade, esperado):
    assert validar_cep(cep, cidade, df_test) == esperado