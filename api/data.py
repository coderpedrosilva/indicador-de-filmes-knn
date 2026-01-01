import pandas as pd

movies = pd.DataFrame([
 ["Invocação do Mal",8,1,4,0,"Terror"],
 ["Floresta Maldita",9,0,5,1,"Terror"],
 ["Atividade Paranormal",7,0,3,0,"Terror"],
 ["O Exorcista",8,1,4,0,"Terror"],

 ["Se Beber Não Case",1,3,1,9,"Comédia"],
 ["As Branquelas",0,4,0,10,"Comédia"],
 ["Tirando o Atraso",0,2,2,8,"Comédia"],
 ["Minha Mãe é uma Peça",0,3,0,9,"Comédia"],

 ["Velozes e Furiosos",4,1,10,1,"Ação"],
 ["Mad Max",5,0,9,0,"Ação"],
 ["John Wick",7,0,10,0,"Ação"],
 ["Missão Impossível",4,2,9,1,"Ação"],

 ["Diário de uma Paixão",0,9,0,6,"Drama"],
 ["Titanic",2,10,2,5,"Drama"],
 ["Simplesmente Acontece",0,8,0,6,"Drama"],
 ["Como Eu Era Antes de Você",0,9,0,5,"Drama"],
], columns=["filme","violencia","romance","acao","comedia","classe"])
