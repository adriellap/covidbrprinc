from attr import attrs
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = 'https://covid.saude.gov.br/'
hearders = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"}
site = requests.get(url, headers=hearders)

html_dados = """<div _ngcontent-nyu-c7="" class="list-itens ct-itens-geral"><!--bindings={
  "ng-reflect-ng-for-of": "[object Object],[object Object"
}--><div _ngcontent-nyu-c7="" class="width-full"><div _ngcontent-nyu-c7="" class="display-flex justify-between item-line width-full" ng-reflect-klass="display-flex justify-between i" ng-reflect-ng-class="[object Object]"><div _ngcontent-nyu-c7="" class="lb-nome nome-cit nome-1" ng-reflect-klass="lb-nome nome-cit" ng-reflect-ng-class="[object Object]"><ion-button _ngcontent-nyu-c7="" class="btn-white btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated"><!--bindings={
  "ng-reflect-ng-if": "true"
}--><ion-icon _ngcontent-nyu-c7="" name="chevron-down-outline" slot="icon-only" ng-reflect-name="chevron-down-outline" role="img" class="md hydrated" aria-label="chevron down outline"></ion-icon><!--bindings={
  "ng-reflect-ng-if": "false"
}--></ion-button> Brasil </div><div _ngcontent-nyu-c7="" class="col-values"><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Casos</div><b _ngcontent-nyu-c7="">34.011.173</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Óbitos</div><b _ngcontent-nyu-c7="">679.939</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Incidência/100mil hab.</div><b _ngcontent-nyu-c7="">16184,5</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value "><div _ngcontent-nyu-c7="" class="header-list tp-aux">Mortalidade/100mil hab</div><b _ngcontent-nyu-c7="">323,6</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Atualização</div><b _ngcontent-nyu-c7="">06/08/2022 19:30</b></div></div></div><!--bindings={}--></div><div _ngcontent-nyu-c7="" class="width-full"><div _ngcontent-nyu-c7="" class="display-flex justify-between item-line width-full pd-left" ng-reflect-klass="display-flex justify-between i" ng-reflect-ng-class="[object Object]"><div _ngcontent-nyu-c7="" class="lb-nome nome-cit" ng-reflect-klass="lb-nome nome-cit" ng-reflect-ng-class="[object Object]"><ion-button _ngcontent-nyu-c7="" class="btn-white btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated"><!--bindings={
  "ng-reflect-ng-if": "false"
}--><!--bindings={
  "ng-reflect-ng-if": "true"
}--><ion-icon _ngcontent-nyu-c7="" name="chevron-forward-outline" slot="icon-only" ng-reflect-name="chevron-forward-outline" role="img" class="md hydrated" aria-label="chevron forward outline"></ion-icon></ion-button> Centro-Oeste </div><div _ngcontent-nyu-c7="" class="col-values"><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Casos</div><b _ngcontent-nyu-c7="">3.858.893</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Óbitos</div><b _ngcontent-nyu-c7="">64.644</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Incidência/100mil hab.</div><b _ngcontent-nyu-c7="">23678,4</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value "><div _ngcontent-nyu-c7="" class="header-list tp-aux">Mortalidade/100mil hab</div><b _ngcontent-nyu-c7="">396,7</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Atualização</div><b _ngcontent-nyu-c7="">06/08/2022 19:30</b></div></div></div><!--bindings={}--></div><div _ngcontent-nyu-c7="" class="width-full"><div _ngcontent-nyu-c7="" class="display-flex justify-between item-line width-full pd-left" ng-reflect-klass="display-flex justify-between i" ng-reflect-ng-class="[object Object]"><div _ngcontent-nyu-c7="" class="lb-nome nome-cit" ng-reflect-klass="lb-nome nome-cit" ng-reflect-ng-class="[object Object]"><ion-button _ngcontent-nyu-c7="" class="btn-white btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated"><!--bindings={
  "ng-reflect-ng-if": "false"
}--><!--bindings={
  "ng-reflect-ng-if": "true"
}--><ion-icon _ngcontent-nyu-c7="" name="chevron-forward-outline" slot="icon-only" ng-reflect-name="chevron-forward-outline" role="img" class="md hydrated" aria-label="chevron forward outline"></ion-icon></ion-button> Sul </div><div _ngcontent-nyu-c7="" class="col-values"><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Casos</div><b _ngcontent-nyu-c7="">7.214.157</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Óbitos</div><b _ngcontent-nyu-c7="">107.448</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Incidência/100mil hab.</div><b _ngcontent-nyu-c7="">24066,5</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value "><div _ngcontent-nyu-c7="" class="header-list tp-aux">Mortalidade/100mil hab</div><b _ngcontent-nyu-c7="">358,4</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Atualização</div><b _ngcontent-nyu-c7="">06/08/2022 19:30</b></div></div></div><!--bindings={}--></div><div _ngcontent-nyu-c7="" class="width-full"><div _ngcontent-nyu-c7="" class="display-flex justify-between item-line width-full pd-left" ng-reflect-klass="display-flex justify-between i" ng-reflect-ng-class="[object Object]"><div _ngcontent-nyu-c7="" class="lb-nome nome-cit" ng-reflect-klass="lb-nome nome-cit" ng-reflect-ng-class="[object Object]"><ion-button _ngcontent-nyu-c7="" class="btn-white btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated"><!--bindings={
  "ng-reflect-ng-if": "false"
}--><!--bindings={
  "ng-reflect-ng-if": "true"
}--><ion-icon _ngcontent-nyu-c7="" name="chevron-forward-outline" slot="icon-only" ng-reflect-name="chevron-forward-outline" role="img" class="md hydrated" aria-label="chevron forward outline"></ion-icon></ion-button> Norte </div><div _ngcontent-nyu-c7="" class="col-values"><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Casos</div><b _ngcontent-nyu-c7="">2.710.674</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Óbitos</div><b _ngcontent-nyu-c7="">50.647</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Incidência/100mil hab.</div><b _ngcontent-nyu-c7="">14707,2</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value "><div _ngcontent-nyu-c7="" class="header-list tp-aux">Mortalidade/100mil hab</div><b _ngcontent-nyu-c7="">274,8</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Atualização</div><b _ngcontent-nyu-c7="">06/08/2022 19:30</b></div></div></div><!--bindings={}--></div><div _ngcontent-nyu-c7="" class="width-full"><div _ngcontent-nyu-c7="" class="display-flex justify-between item-line width-full pd-left" ng-reflect-klass="display-flex justify-between i" ng-reflect-ng-class="[object Object]"><div _ngcontent-nyu-c7="" class="lb-nome nome-cit" ng-reflect-klass="lb-nome nome-cit" ng-reflect-ng-class="[object Object]"><ion-button _ngcontent-nyu-c7="" class="btn-white btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated"><!--bindings={
  "ng-reflect-ng-if": "false"
}--><!--bindings={
  "ng-reflect-ng-if": "true"
}--><ion-icon _ngcontent-nyu-c7="" name="chevron-forward-outline" slot="icon-only" ng-reflect-name="chevron-forward-outline" role="img" class="md hydrated" aria-label="chevron forward outline"></ion-icon></ion-button> Nordeste </div><div _ngcontent-nyu-c7="" class="col-values"><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Casos</div><b _ngcontent-nyu-c7="">6.779.708</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Óbitos</div><b _ngcontent-nyu-c7="">131.112</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Incidência/100mil hab.</div><b _ngcontent-nyu-c7="">11879,3</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value "><div _ngcontent-nyu-c7="" class="header-list tp-aux">Mortalidade/100mil hab</div><b _ngcontent-nyu-c7="">229,7</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Atualização</div><b _ngcontent-nyu-c7="">06/08/2022 19:30</b></div></div></div><!--bindings={}--></div><div _ngcontent-nyu-c7="" class="width-full"><div _ngcontent-nyu-c7="" class="display-flex justify-between item-line width-full pd-left" ng-reflect-klass="display-flex justify-between i" ng-reflect-ng-class="[object Object]"><div _ngcontent-nyu-c7="" class="lb-nome nome-cit" ng-reflect-klass="lb-nome nome-cit" ng-reflect-ng-class="[object Object]"><ion-button _ngcontent-nyu-c7="" class="btn-white btn-outline md button button-solid button-has-icon-only ion-activatable ion-focusable hydrated"><!--bindings={
  "ng-reflect-ng-if": "false"
}--><!--bindings={
  "ng-reflect-ng-if": "true"
}--><ion-icon _ngcontent-nyu-c7="" name="chevron-forward-outline" slot="icon-only" ng-reflect-name="chevron-forward-outline" role="img" class="md hydrated" aria-label="chevron forward outline"></ion-icon></ion-button> Sudeste </div><div _ngcontent-nyu-c7="" class="col-values"><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Casos</div><b _ngcontent-nyu-c7="">13.447.741</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Óbitos</div><b _ngcontent-nyu-c7="">326.088</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Incidência/100mil hab.</div><b _ngcontent-nyu-c7="">15217,3</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value "><div _ngcontent-nyu-c7="" class="header-list tp-aux">Mortalidade/100mil hab</div><b _ngcontent-nyu-c7="">369,0</b></div><div _ngcontent-nyu-c7="" class="lb-nome lb-value"><div _ngcontent-nyu-c7="" class="header-list tp-aux">Atualização</div><b _ngcontent-nyu-c7="">06/08/2022 19:30</b></div></div></div><!--bindings={}--></div></div>"""

soup = BeautifulSoup(html_dados, 'html.parser')
dados = soup.find_all("div", attrs={"class": "display-flex justify-between item-line width-full pd-left"})
dados2 = soup.find_all("div", attrs={"class": "lb-nome lb-value"})

covid = []
covid1 = []
covid2 = []

for dado in dados:
    lista_dados1 = []
    lista_dados1.append(dado.find("div", class_="lb-nome nome-cit").get_text().strip())
    covid1.append(lista_dados1)
a = np.array(covid1)
covid1 = a

for i in range(5,30):
    lista_dados2 = []
    dado2 = dados2[i]
    lista_dados2.append(dado2.find("b").get_text().strip())
    covid2.append(lista_dados2)
b= np.array(covid2)
c= b.reshape(5,5)
covid2 = c

covid1_df = pd.DataFrame(covid1, columns=['Região'])
covid2_df = pd.DataFrame(covid2, columns=['Casos', 'Óbitos', 'Incidência/100mil hab.', 'Mortalidade/100mil hab', 'Atualização'])
covid_df = pd.concat([covid1_df,covid2_df], axis=1)
covid_df = covid_df.replace({
    "\.": "",
    ",": "."}, regex=True)

print(covid_df)
covid_df.to_csv('covid_brasil.csv', index=False)