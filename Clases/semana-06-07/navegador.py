from PyQt5.QtCore import QObject, pyqtSignal


class Navegador(QObject):

    ir_a_url_signal = pyqtSignal(str)

    def __init__(self, url_inicial="google.com"):
        super().__init__()
        self.__stack_urls = []
        self.__url_actual = url_inicial

    def __cargar_url(self, url):
        """
        Carga la URL actual y emite la señal de.ir_a a dicha URL
        """
        self.__url_actual = url
        print(f"Cargando URL: {url}")
        self.ir_a_url_signal.emit(url)

    def ir_a(self, url):
        """
        Guarda la URL actual en el stack y carga la nueva
        """
        self.__stack_urls.append(self.__url_actual)
        print(f"Ir -> {url}")
        self.__cargar_url(url)

    def volver(self):
        """
        Saca la URL más reciente del stack y la carga
        """
        if len(self.__stack_urls) == 0:
            print("No hay más páginas")
        else:
            url = self.__stack_urls.pop()
            print(f"Volviendo a: {url} ")
            self.__cargar_url(url)

    def mostrar_pagina_actual(self):
        """
        Muestra y retorna la URL actual
        """
        print(f"Página actual: {self.__url_actual}")
        return self.__url_actual


if __name__ == '__main__':
    browser = Navegador()
    browser.ir_a('http://www.uc.cl')
    browser.ir_a('http://www.uc.cl/es/programas-de-estudio')
    browser.ir_a('http://www.uc.cl/es/doctorado')
    browser.mostrar_pagina_actual()
    browser.volver()
    browser.mostrar_pagina_actual()
    browser.ir_a('https://stackoverflow.com/')
    browser.ir_a('https://github.com/IIC2233/contenidos')
    browser.volver()
    browser.mostrar_pagina_actual()
