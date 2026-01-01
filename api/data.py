import pandas as pd

movies = pd.DataFrame([
    # AÇÃO
    ["John Wick",7,0,10,0,"Ação"],
    ["Mad Max: Fury Road",6,0,10,0,"Ação"],
    ["Velozes e Furiosos",4,1,10,1,"Ação"],
    ["Missão Impossível",4,2,9,1,"Ação"],
    ["Duro de Matar",6,1,8,0,"Ação"],
    ["Gladiador",6,2,7,0,"Ação"],
    ["Matrix",5,1,9,0,"Ação"],

    # TERROR
    ["Invocação do Mal",8,1,4,0,"Terror"],
    ["It: A Coisa",7,0,3,0,"Terror"],
    ["O Exorcista",8,1,4,0,"Terror"],
    ["Atividade Paranormal",7,0,3,0,"Terror"],
    ["Hereditário",6,0,2,0,"Terror"],
    ["Jogos Mortais",7,0,6,0,"Terror"],
    ["A Bruxa",5,0,1,0,"Terror"],

    # COMÉDIA
    ["As Branquelas",0,4,0,10,"Comédia"],
    ["Se Beber Não Case",1,3,1,9,"Comédia"],
    ["Todo Mundo em Pânico",2,0,3,9,"Comédia"],
    ["Minha Mãe é uma Peça",0,3,0,9,"Comédia"],
    ["American Pie",1,3,0,8,"Comédia"],
    ["Click",0,4,0,7,"Comédia"],
    ["Gente Grande",0,3,0,8,"Comédia"],

    # DRAMA
    ["Titanic",2,10,2,5,"Drama"],
    ["Diário de uma Paixão",0,9,0,6,"Drama"],
    ["Forrest Gump",1,5,1,5,"Drama"],
    ["À Procura da Felicidade",0,3,0,4,"Drama"],
    ["A Espera de um Milagre",2,1,0,2,"Drama"],
    ["O Pianista",4,0,1,0,"Drama"],
    ["Clube da Luta",6,0,5,0,"Drama"],

    # FICÇÃO CIENTÍFICA
    ["Interestelar",2,3,4,0,"Ficção"],
    ["Blade Runner",3,0,4,0,"Ficção"],
    ["Ex Machina",2,3,1,0,"Ficção"],
    ["Avatar",3,4,6,0,"Ficção"],
    ["Gravidade",1,2,3,0,"Ficção"],
    ["Distrito 9",4,0,5,0,"Ficção"],
    ["Duna",4,2,6,0,"Ficção"],

    # ANIMAÇÃO
    ["Toy Story",0,2,0,9,"Animação"],
    ["Shrek",0,3,0,9,"Animação"],
    ["Procurando Nemo",0,2,0,8,"Animação"],
    ["Up",0,3,0,7,"Animação"],
    ["Divertida Mente",0,2,0,8,"Animação"],
    ["Os Incríveis",2,1,7,6,"Animação"],
    ["Kung Fu Panda",2,1,6,6,"Animação"],
], columns=["filme","violencia","romance","acao","comedia","classe"])
