import time
def ordem_servico(hospital):
    continuar = True
  
    while continuar == True:
        ir = int(input("Digite leito(101,102,103,104 ou 0 quando terminar): "))
        if ir == 0:
            continuar = False
            print ("SEM ORDENS DE SERVIÇO!")
        else:
            leito_encontrado=False 
            for leito in hospital:
                if ir == leito['numero']:
                    leito_encontrado= True
                    if leito['ocupado']:
                        print(f"o leito {leito['numero']} está ocupado pelo paciente {leito['paciente']}!")
                        higienizar_maos()
                        checar_equipamentos()
                    else:
                        print(f"o leito {leito['numero']} está livre!")
            if leito_encontrado==False:
                print ("Leito inválido")

def higienizar_maos():
    print("HIGIENIZE AS MÃOS!")
    for segundos in range(1,6):
        print(f"\n lavando as mãos {segundos}...")
        time.sleep(1)
    print("---MÃOS HIGIENIZADAS!---")

def verificar_horario(nome, entrada, saida, atual):
    if atual == entrada:
        print("--- LIBERADO ---")
        return True
    elif atual == entrada + 1:
        print("--- ATRASADO / LIBERADO ---")
        return True
    elif atual > entrada and atual <= saida:
        print("---ATRASADO,FALAR COM A GERENCIA!---")
        return False
    else:
        print("--- FORA DE HORÁRIO ---")
        return False

def checar_equipamentos():
    itens_obrigatorios = ["maca", "lençol", "travessa"]
    print("\n--- CHECAGEM DE EQUIPAMENTOS ---")
    for item in itens_obrigatorios:
        resposta = ""
        while resposta != "sim":
            resposta = input(f"O(A) {item} já está pronto(a)? (sim/não): ").strip().lower()
            if resposta != "sim":
                print(f"--- ATENÇÃO: Prepare o(a) {item}! ---")
        print(f"--- {item.upper()} OK ---")
    else:
        print(f"---tudo ok,pode prosseguir com o transporte do paciente!----")

#PROGRAMA PRINCIPAL---------------

print("--- MAQUEIRO SIMULATOR v2.0 ---")
hospital =[
    {"numero" : 101 ,"paciente" : "Carlos" , "ocupado" : True },
    {"numero" : 102 , "paciente" : "ninguem", "ocupado": False },
    {"numero" : 103 , "paciente" : "ninguém", "ocupado": False },
    {"numero" : 104 , "paciente" : "José", "ocupado": True }
]
funcionario = {}
funcionario["nome"] = input("Qual seu nome? : ").strip().lower()
funcionario["entrada"] = int(input("Horário de entrada: "))
funcionario["saida"] = int(input("Horário de saída: "))
horario_atual = int(input("Que horas são agora? "))

pode_trabalhar = verificar_horario(funcionario["nome"], funcionario["entrada"], funcionario["saida"], horario_atual)

if pode_trabalhar:
    print(f"\nOlá {funcionario['nome'].title(
)}! Bom plantão.")
    ordem_servico(hospital)
    print("-- 0 Ordens de serviço! --")
