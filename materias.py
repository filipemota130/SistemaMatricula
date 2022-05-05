class Disciplina:
    def __init__(self, nome: str, pre_requisitos: list, horario: list):
        self.nome = nome
        self.pre_requisitos = pre_requisitos
        self.horario = horario
        self.limite = 10
        self.ocupado = 0 #quantos estão atualmente matriculados


grade_curricular = {
    #1º periodo
    "COMP359": Disciplina("Programação 1", [], ['SX07300910', 'SX09201100']),
    "COMP360": Disciplina("Lógica para Computação", [], ['SG11101250', 'QA11101250']),
    "COMP361": Disciplina("Computação, Sociedade e Ética", [], ['SE09201100', 'QA09201100']),
    "COMP362": Disciplina("Matemática Discreta", [], ['SG07300910', 'QI07300910']),
    "COMP363": Disciplina("Cálculo Diferencial e Integral", [], ['TE07201110', 'QI07201110']),
    #2º periodo
    "COMP364": Disciplina("Estrutura de Dados", ["COMP359"], ['SE13301510', 'QA13301510']),
    "COMP365": Disciplina("Banco de Dados", [], ['TE15201700', 'QI15201700']),
    "COMP366": Disciplina("Organização e Arquitetura de Computadores", [], ['SE17101850', 'QA17101850']),
    "COMP367": Disciplina("Geometria Analítica", [], ['SE15201700', 'QA15201700']),
    #3º periodo
    "COMP368": Disciplina("Redes de Computadores", ["COMP359"], []),
    "COMP369": Disciplina("Teoria dos Grafos", ["COMP364", "COMP362"], []),
    "COMP370": Disciplina("Probabilidade e Estatística", ["COMP363"], []),
    "COMP371": Disciplina("Álgebra Linear", ["COMP367"], []),
    
    #4º periodo
    "COMP372": Disciplina("Programação 2", ["COMP364", "COMP365", "COMP368"], []),
    "COMP373": Disciplina("Programação 3", ["COMP364", "COMP365", "COMP368"], []),
    "COMP374": Disciplina("Projeto e Análise de Algorítimos", ["COMP364", "COMP369"], []),
    "COMP376": Disciplina("Teoria da Computação", [], []),
    "COMP378": Disciplina("Sistemas Operacionais", ["COMP366"], []),
    "COMP379": Disciplina("Compiladores", ["COMP364", "COMP376"], []),
    "COMP380": Disciplina("Inteligencia Artificial", ["COMP360", "COMP364"], []),
    "COMP381": Disciplina("Computação Gráfica", [], []),
    "COMP382": Disciplina("Projeto e Desenvolvimento de Sistemas", ["COMP359", "COMP360", "COMP361", "COMP362", "COMP363", "COMP364", "COMP365", "COMP366", "COMP367", "COMP367", "COMP369", "COMP370", "COMP371", "COMP372", "COMP373", "COMP374", "COMP376", "COMP378", "COMP379", "COMP380", "COMP381"], []),
    "COMP386": Disciplina("Metodologia de Pesquisa e Trabalho Individual", [], ['SX07300910']),
    "COMP387": Disciplina("Noções de Direito", [], []),
    "COMP389": Disciplina("Conceitos de Linguagem de Programação", [], []),
    "COMP390": Disciplina("Aprendizagem de Máquina", ["COMP404"], []),
    "COMP391": Disciplina("Sistemas Digitais", ["COMP404"], []),
    "COMP392": Disciplina("Sistemas Distribuidos", [], []),
    "COMP393": Disciplina("Redes Neurais e Aprendizado Profundo", [], []),
    "COMP394": Disciplina("FPGA", [], []),
    "COMP395": Disciplina("Iteração Homem-Máquina", ["COMP373"], []),
    "COMP396": Disciplina("Processamento Digital de Imagens", ["COMP381"], []),
    "COMP397": Disciplina("Computação Evolucionária", [], []),
    "COMP398": Disciplina("Sistemas Embarcados", [], []),
    "COMP399": Disciplina("Gerencia de Projeto", ["COMP382"], []),
    "COMP400": Disciplina("Visão Computacional", [], []),
    "COMP401": Disciplina("Ciencia de Dados", ["COMP370"], []),
    "COMP402": Disciplina("Microcontroladores e Aplicações", [], []),
    "COMP403": Disciplina("Segurança de Sistemas Computacionais", ["COMP368"], []),
    "COMP404": Disciplina("Calculo 3", ["COMP363"], []),
    "COMP405": Disciplina("Tópicos em Ciência da Computação 1 ", [], []),
    "COMP406": Disciplina("Tópicos em Ciência da Computação 2", [], []),
    "COMP407": Disciplina("Tópicos em Ciência da Computação 3 ", [], []),
    "COMP409": Disciplina("Tópicos em Matemática para Computação 1 ", [], []),
    "COMP410": Disciplina("Tópicos em Matemática para Computação 2 ", [], []),
    "COMP411": Disciplina("Tópicos em Matemática para Computação 3 ", [], []),
    "COMP412": Disciplina("Tópicos em Física para Computação 1 ", [], []),
    "COMP413": Disciplina("Tópicos em Física para Computação 2 ", [], []),
    "COMP414": Disciplina("Tópicos em Física para Computação 3", [], []),

    "CC1941": Disciplina("Cálculo 4", [], []),
    "CC1942": Disciplina("Cálculo Numérico", [], []),
    "CC1943": Disciplina("Circuitos Digitais", [], []),
    "CC1944": Disciplina("Circuitos Impressos", [], []),
    "CC1945": Disciplina("Fundamentos de Libras", [], []),
    "CC1946": Disciplina("Geometria Computacional", [], []),
    "CC1947": Disciplina("Pesquisa Operacional", [], []),
    "CC1948": Disciplina("Programação para Sistemas Embarcados ", [], []),
    "CC1949": Disciplina("Projeto de Sistemas Embarcados", [], []),
    "CC1950": Disciplina("Tópicos em Arquitetura de Computadores ", [], []),
    "CC1951": Disciplina("Tópicos em Banco de Dados", [], []),
    "CC1952": Disciplina("Tópicos em Computação Científica ", [], []),
    "CC1953": Disciplina("Tópicos em Computação Paralela", [], []),
    "CC1954": Disciplina("Tópicos em Computação Visual", [], []),
    "CC1955": Disciplina("Tópicos em Comunicação de Dados ", [], []),
    "CC1956": Disciplina("Tópicos em Desenvolvimento de Sistemas ", [], []),
    "CC1957": Disciplina("Tópicos em Engenharia de Software", [], []),
    "CC1958": Disciplina("Tópicos em Humanidades ", [], []),
    "CC1959": Disciplina("Tópicos em Informática na Educação", [], []),
    "CC1960": Disciplina("Tópicos em Inteligência Artificial", [], []),
    "CC1961": Disciplina("Tópicos em Linguagens de Programação ", [], []),
    "CC1962": Disciplina("Tópicos em Programação ", [], []),
    "CC1963": Disciplina("Tópicos em Redes de Computadores ", [], []),
    "CC1964": Disciplina("Tópicos em Sistemas de Computação", [], []),
    "CC1965": Disciplina("Tópicos em Sistemas de Informação", [], []),
    "CC1966": Disciplina("Tópicos em Sistemas Distribuídos ", [], []),
    "CC1967": Disciplina("Tópicos em Sistemas Inteligentes", [], []),
    "CC1968": Disciplina("Tópicos em Software Básico ", [], []),
}


horarios = ['SG07300910', 'SG09201100', 'SG11101250', 'SG13301510',
            'SG15201700', 'SG17101850', 'SG09201200']
['TE07201110', 'TE07300910', 'TE09201200', 'TE09201100', 'TE11101250', 'TE13301510',
    'TE15201700', 'TE17101850']
['QA07300910', 'QA09201200', 'QA09201100', 'QA11101250', 'QA13301510',
    'QA15201700', 'QA17101850']
['QI07300910', 'QI09201200', 'QI09201100', 'QI11101250', 'QI13301510',
    'QI15201700', 'QI17101850']
['SX09201100', 'SX11101250', 'SX13301510',
    'SX15201700', 'SX17101850']
