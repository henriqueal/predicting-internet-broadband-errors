# Predicting internet broadband errors

Neste trabalho eu dsenvolvi um sistema que analisa a correlação entre a quantidade de chuva na cidade de Uberlândia e a taxa de atenuação dos equipamentos que compõe a banda larga ADSL da cidade.

A figura 1 ilustra a arquitetura do trabalho:

![Arquitetura](images/arquitetura_solucao.png)

Nela, podemos observar que a solução de analytics precisa de dois inputs: uma lista com todos os IPs da cidade de Uberlândia e outra lista com a quantidade de chuva em Uberlândia por dia. A primeira lista pode ser extraída da nossa plataforma Ruby. Já o segundo parâmetro precisa ser extraído do site do inmet. O próximo passo que a solução realiza é consumir uma API passando os IPs e recebendo a lista de atenuação daqueles equipamentos. Depois disso, a solução determina qual a correlação da atenuação de cada equipamento com os dados metereológicos da chuva.

## Coletando os dados:
- Ips do Ruby: Neste trabalho, foi solicitado para a Camila Cerqueira Lott extrair a lista de IPs da cidade de Uberlândia.
- Dados metereológicos:

1) Para coletar os dados de precipitação de Uberlândia acesse o link: http://www.inmet.gov.br/sonabra/pg_dspDadosCodigo_sim.php?QTUwNw;

2) Insira as informações de “Data início” e “Data fim” nos campos correspondentes;

3) Digite o número apresentado ao lado para confirmação e clique em “OK”.

- Consumindo os dados da API:
Para acessar a API que contém os dados, você deve pedir uma regra de firewall para o servidor: 172.20.4.169. Depois que tiver acesso, basta consumir este serviço: http://172.20.4.169:8080/dslams-extractor/service/dslams/172.30.15.139?snapshotsNum=20

## Quantidade de dados:
- Ips em Uberlândia: a lista extraída do Ruby continha 540 IPs
- Quantidade de porta: é variado de equipamento para equipamento. Mas há equipamentos com mais de 100 portas.
- Dias coletados: houve um erro na coleta dos dados da API, com isso, todos os dados coletados antes do dia 14/12/2017 foram excluídos. Dessa forma, foram coletados os dados da atenuação e da chuva do dia 14/12 ao dia 29/12/2017, totalizando 16 dias.
- Tamanho da amostra: foi realizado 10 experimentos com 10 IPs e 10 portas aleatórias. Totalizando 1000 equipamentos analisados aleatoriamente.

## Solução:
Dada a entrada contendo a lista de ips de uberlandia e a quantidade de chuva também de uberândia, então deve-se sortear uma lista de IPs com 10 elementos. Para cada IP dessa lista deve-se sortear 10 portas e extrair a taxa de atenuação através da API extratora. Para cada porta o algoritmo deve dizer qual a correlação entre a chuva e a atenuação. O pseudo código abaixo abstrai a solução para o problema:

![pseudo](images/pseudo-codigo.png)

## Resultado e Conclusão:
Após analisar os dados obtidos, cheguei à conclusão que nem todos os equipamentos so sucetíveis à chuva. No entanto, alguns equipamentos parecem ter uma certa diferenciação na taxa de atenuação por meio da fator chuva. O que comprova esse argumento é a taxa média e mediana de correlação ser próxima de 0, ou seja, não apresentar correlação.

Os equipamentos que apresentaram altas taxas de correlação foram criados gráficos para observar o comportamento deles e da chuva, como é possível ver na imagem 3:

![corr](images/medicoes.png)

No gráfico da imagem 3 podemos observar que a taxa de atenuação em vermelho era constante em 90, no entanto, nas últimas 4 medições (26/12 até 29/12) podemos observar que não houve chuva e a taxa de atenuação caiu para 85.

Analisamos também que há equipamentos que não houveram alteração de acordo com a quantidade de chuva


Por fim, podemos analisar também que há equipamentos com a taxa de correlação inversamente proporcional à chuva como pode ser visto no gráfico da imagem tal.



Por essas razões, não é possível afirmar que a chuva interfere diretamente na taxa de atenuação. No entanto, fica para trabalhos futuros uma análise com um período maior para analisarmos melhor se há equipamentos que realmente possuem interferência na taxa de atenuação com a chuva.


## Trabalhos futuros:
- Analisar para um período maior;
- Fazer a correlação com outras variáveis metereológicas (chuva, vento, umidade, temperatura, etc)
- Fazer a correlação com outras variáveis do equipamento (taxa de upload, downoload, sinal rudo, etc).
- Analisar para outras cidade.
- Armazenar os dados metereolóficos em um BD
