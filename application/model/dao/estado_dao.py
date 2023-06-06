from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

class EstadoDAO:
    def __init__(self):
        noticia1 = Noticia(1, "O Rio de Janeiro registrou aumento de internações por covid-19. Segundo a Secretaria Municipal de Saúde, nesta sexta, 49 pessoas estavam internadas com covid na cidade.", "img/rj_noticia_1.png", "video/rj_noticia1.mp4", "O Rio de Janeiro registrou aumento de internações por covid-19. Segundo a Secretaria Municipal de Saúde, nesta sexta, 49 pessoas estavam internadas com covid na cidade.", "29/04/2021", 250, 400)
        noticia2 = Noticia(2, "Os indicadores de covid-19 apresentam tendência de queda no estado do rio de janeiro.", "img/rj_noticia_2.png", "video/rj_noticia2.mp4", "Os indicadores de covid-19 apresentam tendência de queda no estado do rio de janeiro.", "26/04/2021", 300, 445)
        noticia3 = Noticia(3, "A circulação da nova subvariante da Covid-19, descendente da Ômicron, vem impulsionando o número de casos positivos de coronavírus em Minas Gerais.", "img/mg_noticia_1.png", "video/mg_noticia1.mp4", "A circulação da nova subvariante da Covid-19, descendente da Ômicron, vem impulsionando o número de casos positivos de coronavírus em Minas Gerais.", "26/04/2021", 320, 650)
        noticia4 = Noticia(4, "A Universidade Federal de Uberlândia (MG) está trabalhando em uma tecnologia para testagem rápida de casos de coronavírus com resultados em até 2 minutos.", "img/mg_noticia_2.png", "video/mg_noticia2.mp4", "A Universidade Federal de Uberlândia (MG) está trabalhando em uma tecnologia para testagem rápida de casos de coronavírus com resultados em até 2 minutos.", "28/04/2021", 120, 300)
        noticia5 = Noticia(5, "Alta de casos: internações por casos de Covid-19 dobram no Estado de São Paulo.", "img/sp_noticia_1.png", "video/sp_noticia1.mp4", "Alta de casos: internações por casos de Covid-19 dobram no Estado de São Paulo.", "27/04/2021", 222, 540)
        estado1 = Estado(1, "Rio de Janeiro", "RJ", "img/bandeira-rj.png", [noticia1, noticia2])
        estado2 = Estado(2, "Minas Gerais", "MG", "img/bandeira-mg.png", [noticia3, noticia4])
        estado3 = Estado(3, "São Paulo", "SP", "img/bandeira_sp.jpg", [noticia5])
        self._estados = [estado1, estado2, estado3]

    def findAll(self):
        return self._estados

    def findNoticiaById(self, id:int):
        for estado in self._estados:
            for noticia in estado.getNoticiaList():
                if noticia.getId() == id:
                    return noticia
        return None