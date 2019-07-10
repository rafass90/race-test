CRIAÇÃO DA SOLUÇÃO
=======
Escolhi a linguagem Python por acreditar ser bastante aderente ao propósito do desafio. Um programa simples de ser executado, com necessidades de um rápido desenvolvimento, facilidade de leitura(para quem vai avaliar o código), performance adequada e alta disponibilidade de recursos nativos da linguagem para resolver os problemas.

Iniciei criando o core da aplicação, a leitura do Log. Para essa etapa, optei por usar regex, embora seja comumente considerado um anti pattern, com a regex, o mecanismo de leitura do arquivo ganha robustez por conseguir "se adaptar" a arqivos com ligeiras diferenças de espaçamento e formatação. Com fácil manutenção por se tratar poucas colunas a serem lidas e o resultado ficar separado por grupos. Entendo que foi a escolha mais eficaz para resolver a leitura do arquivo.

Após a criação do mecanismo de parser do documento, criei o VO equivalente a ele, no qual chamei de LAP, pois contém todos os registros de uma volta.
Não queria aumentar a complexidade e verbosidade mas avaliei que ficaria mais fácil de escrever e compreender o código criando o objeto PILOT, contendo apenas seu nome e código. Optei por essa abordagem porque ficaria fácil acrescentar posteriormente outras características ao piloto, por exemplo, idade, peso, etc..

A classe RACE, criei para que fosse o core da logica de negócio, o core da aplicação. Nela está a lógica do desafio.

Python versão 3.6.4
Como dependêmcia de código, utilizei apenas a biblioteca pathlib, o restante foi código nativo python.
As dependências estão no diretório requirements/


EXECUÇÃO
=======
Para executar, necessário ter o python, make e pip instalado na máquina.
```make run```

Neste caso, os arquivos default serão utilizados ( data/race.log e data/result.txt)

Opcional, passar os parâmetros de entrada(arquivo de log) e saida(arquivo txt com os resultados)
```make run ARGS="$MY_INPUTFILE_LOG $MY_RESULT_OUTPUT"```


MAKE
============
Use `make` para executar o projeto

```
check-python-import  Check python import
clean                Clean files
fix-python-import    Fix python import
help                 This help
lint                 Python lint
requirements-dev     Install requirements dev
run                  Run job
test                 Run all tests
```
