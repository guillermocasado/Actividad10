import statistics as st

class StatsData:

    def __init__(self, lista):
        self.l_data = lista
        self.media = st.mean(lista)
        self.mediana = st.median(lista)
        self.varianza = st.variance(lista)

