class Filme(object):

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano
    
    @property
    def avaliacao ( self ):
        return self . _avaliacao
    
    @avaliacao . setter
    def avaliacao ( self , avaliacao ):
        self._avaliacao = avaliacao
    
    @property
    def classificacao ( self ) :
        return self . _classificacao
    
    @classificacao . setter
    def classificacao ( self , classificacao ):
        self._classificacao = classificacao