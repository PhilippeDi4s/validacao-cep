# Estrutura do DataFrame de Teste

Exemplo utilizado nos testes:

```python
df_test = pd.DataFrame({
    "CEP_INICIAL": [77470000],
    "CEP_FINAL": [77474999],
    "LOCALIDADE": ["Formoso do Araguaia"]
})
```

Isso significa que todos os CEPs entre:

```
77470000 até 77474999
```

pertencem à cidade:

```
Formoso do Araguaia
```

---

# Exemplos de CEPs válidos

| CEP       | Cidade              | Motivo                  |
| --------- | ------------------- | ----------------------- |
| 77470000  | Formoso do Araguaia | início do intervalo     |
| 77471234  | Formoso do Araguaia | CEP dentro do intervalo |
| 77474999  | Formoso do Araguaia | final do intervalo      |
| 77471-234 | Formoso do Araguaia | formato com hífen       |

---

# Exemplos de CEPs inválidos

| CEP      | Cidade              | Motivo                        |
| -------- | ------------------- | ----------------------------- |
| 77475000 | Formoso do Araguaia | fora do intervalo             |
| 77469999 | Formoso do Araguaia | abaixo do intervalo           |
| 77471234 | Palmas              | cidade não corresponde ao CEP |
| 7747-123 | Formoso do Araguaia | formato de CEP inválido       |
| ABCDEFGH | Formoso do Araguaia | CEP não numérico              |

---

# Executando os testes

Instale as dependências:

```
pip install pytest pandas
```

Execute os testes:

```
pytest
```

---

# Tecnologias utilizadas

* Python
* Pandas
* Pytest
* Regex

```
```
