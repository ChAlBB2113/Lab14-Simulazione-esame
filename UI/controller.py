import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.creaGrafo()
        numeroNodi=self._model.getNumeroNodi()
        numeroArchi=self._model.getNumeroArchi()
        self._view.txt_result.controls.append(ft.Text(f"Il numero di nodi è {numeroNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Il numero di archi è {numeroArchi}"))
        self._view.txt_result.controls.append(ft.Text(f"Il peso minimo è {self._model.getPesiMinMax()[0]}"))
        self._view.txt_result.controls.append(ft.Text(f"Il peso massimo è {self._model.getPesiMinMax()[1]}"))
        self._view.update_page()

    def handle_countedges(self, e):
        pesoMinimo=self._model.getPesiMinMax()[0]
        pesoMassimo=self._model.getPesiMinMax()[1]
        valoreSoglia= self._view.txt_name.value
        if valoreSoglia is None:
            self._view.txt_result2.controls.append(ft.Text(f"Inserire un valore soglia"))
            self._view.update_page()
            return
        try:
            valoreSoglia=float(valoreSoglia)
        except ValueError:
            self._view.txt_result2.controls.append(ft.Text(f"Inserire un valore soglia numerico"))
            self._view.update_page()
            return
        if valoreSoglia<=pesoMinimo and valoreSoglia>=pesoMassimo:
            self._view.txt_result2.controls.append(ft.Text(f"valore soglia fuori da range di peso minimo e peso massimo"))
            self._view.update_page()
            return
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {self._model.getNumeroArchiMinoriMaggioriSoglia(valoreSoglia)[0]}"))
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {self._model.getNumeroArchiMinoriMaggioriSoglia(valoreSoglia)[1]}"))

        self._view.update_page()
        return




    def handle_search(self, e):
        pass