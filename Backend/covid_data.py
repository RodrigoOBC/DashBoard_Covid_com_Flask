import pandas as pd


class Gerenciador_Dataset:
    def __init__(self, link):
        self.link = link

    def gerar_datset(self):
        self.df = pd.read_csv(self.link)

    def get_datset(self):
        return self.df

    def remover_colunas(self, columns):
        self.df.drop(columns=columns, inplace=True)

    def subistituir_nulos(self):
        self.df.fillna("", inplace=True)

    def renomear_coluna(self, colunas):
        self.df.rename(columns=colunas, inplace=True)

    def criar_ID(self):
        self.df["ID"] = self.df['Country'].str.lower().replace(' ', '_', regex=True) + "_" + self.df[
            'State'].str.lower().replace(' ', '_', regex=True)
        for index, row in self.df.iterrows():
            if str(row["ID"])[len(str(row["ID"])) - 1:] == "_":
                self.df[index, "ID"] = str(row["ID"])[:-1]

    def tratamento_datas(self, coluna_name,tipo="confirmado"):
        if tipo == "confirmado":
            self.df = self.df.melt(id_vars=["ID", "Country", "State"], var_name="date", value_name=coluna_name)
        else:
            self.df = self.df.melt(id_vars=["ID"], var_name="date", value_name=coluna_name)

class Gerenciador_Dataframe:
    def __init__(self, ID):
        self.ID = ID

    def mergear_data_frame(self, df_casos, df_mortes):
        df_covid = pd.merge(df_casos, df_mortes, how="left", on=['ID', "date"])
        return df_covid


if __name__ == '__main__':
    GDC = Gerenciador_Dataset('Data/Casos/Casos_confirmados_covid_global.csv')
    GDC.gerar_datset()
    GDC.remover_colunas(['Lat', 'Long'])
    GDC.subistituir_nulos()
    GDC.renomear_coluna({'Province/State': "State", 'Country/Region': "Country"})
    GDC.criar_ID()
    GDC.tratamento_datas('confirmed')

    GDD = Gerenciador_Dataset('Data/Casos/Casos_confirmados_covid_global.csv')
    GDD.gerar_datset()
    GDD.remover_colunas(['Lat', 'Long'])
    GDD.subistituir_nulos()
    GDD.renomear_coluna({'Province/State': "State", 'Country/Region': "Country"})
    GDD.criar_ID()
    GDD.tratamento_datas('deaths', tipo="mortes")

    GDR = Gerenciador_Dataset('Data/Casos/Casos_confirmados_covid_global.csv')
    GDR.gerar_datset()
    GDR.remover_colunas(['Lat', 'Long'])
    GDR.subistituir_nulos()
    GDR.renomear_coluna({'Province/State': "State", 'Country/Region': "Country"})
    GDR.criar_ID()
    GDR.tratamento_datas('recover', tipo="mortes")
