import time
def ordem_servico(hospital):
    continuar = True

    while continuar == True:
        ir = int(input("DIGITE O LEITO:(101,102,103,104,105 ou 0 para sair) "))
        if ir == 0:
            continuar = False
            print("SEM ORDENS DE SERVIÇO!")
        else:
            leito_encontrado = False
            for leito in hospital:
                if ir == leito['numero']:
                    leito_encontrado = True
                    
                    if leito['ocupado']:
                        dados_paciente = leito['paciente']
                        
                        print(f"O leito {leito['numero']} está ocupado pelo {dados_paciente['nome']}!")
                        print(f"Idade: {dados_paciente['idade']} anos | Peso: {dados_paciente['peso']}")
                        print(f"Isolamento: {dados_paciente['isolamento']} | Deambula: {dados_paciente['deambula']}")
                        print(f"Procedimento: {dados_paciente['procedimento']}")
                        print("*"*30)
                        
                        higienizar_maos()
                        checar_isolamento(dados_paciente)
                        checar_equipamentos(dados_paciente)
                        if dados_paciente['procedimento'] == "Alta":
                            print(f"\n--- Alta efetuada ---")
                            print(f"O(A) {dados_paciente['nome']} deixou o leito {leito['numero']}!")
                            leito['ocupado'] = False
                            dados_paciente['nome']= "Ninguém "
                            dados_paciente['idade']= 0
                            dados_paciente['procedimento']= ""
                
                    else:
                        print(f"O leito {leito['numero']} está livre!")
                    
                    break
            
            if leito_encontrado == False:
                print("Leito inválido")
def ordem_centro_cirurgico(hospital):
    print("\n--- AVISO DO CENTRO CIRÚRGICO ---")
    print("Paciente: Seu Almir | Procedimento: Pós-Operatório | Destino: Leito 102")
    
    aceitar = input("Aceitar transporte? (sim/não): ").strip().lower()
    
    if aceitar == "sim":
        for leito in hospital:
            if leito['numero'] == 102:
                if leito['ocupado'] == False:
                    higienizar_maos()
                    
                    print(f"\n--- TRANSPORTE CONCLUÍDO ---")
                    print(f"Seu Almir foi transferido do CC para o Leito 102.")
                    leito['ocupado'] = True
                    leito['paciente'] = {
                        "nome": "Seu Almir",
                        "idade": 60,
                        "peso": "80 kg",
                        "isolamento": False,
                        "deambula": False,
                        "procedimento": "Recuperação"
                    }
                else:
                    print("\n!!! ERRO: O Leito 102 foi ocupado de última hora! Avisar a enfermagem.")
                break
    else:
        print("Transporte recusado ou em espera.")
        
def higienizar_maos():
    print("---HIGIENIZE AS MÃOS!---")
    for segundos in range(1,4):
        print(f"\n lavando as mãos {segundos}...")
        time.sleep(1)
    print("mãos limpas!")

def checar_isolamento(paciente):
    if paciente['isolamento']== True:
        resposta_epi = ""
        while resposta_epi != "sim":
            resposta_epi = input("Já colocou EPI? ").strip().lower()
            if resposta_epi != "sim":
                print("!!!EPI NECESSARIO!!!")
            else:
                print("--- PODE PROSSEGUIR!---")
    else:
        print (f"Paciente {paciente['nome']} não está em isolamento!")
            

def verificar_horario(nome, entrada, saida, atual):
    if atual == entrada:
        print("--- LIBERADO ---")
        return True
    elif atual == entrada + 1:
        print("--- ATRASADO / LIBERADO ---")
        return True
    elif atual > entrada and atual <= saida:
        print("---FORA DE HORÁRIO,FALAR COM A GERÊNCIA")
        return False
    else:
        print("--- FORA DE HORÁRIO ---")
        return False

def checar_equipamentos(paciente):
    print("\n--- CHECAGEM DE EQUIPAMENTOS ---")
    
    if paciente['procedimento'] == "Alta" and paciente['deambula'] == True:
        itens_obrigatorios = ["cadeira de rodas"]
        
    elif paciente['isolamento'] == True:
        itens_obrigatorios = ["maca", "lençol", "travessa", "kit isolamento"]
        
    else:
        itens_obrigatorios = ["maca", "lençol", "travessa"]

    for item in itens_obrigatorios:
        resposta = ""
        while resposta != "sim":
            resposta = input(f"O(A) {item} já está pronto(a)? (sim/não): ").strip().lower()
            if resposta != "sim":
                print(f"--- ATENÇÃO: Prepare o(a) {item}! ---")
        print(f"--- {item.upper()} OK,PODE PROSSEGUIR!---")

print("--- MAQUEIRO SIMULATOR v2.0 ---")

hospital = [
    {
        "numero" : 101,
        "ocupado" : True,
        "paciente" : {
            "nome" : "Seu Antônio",
            "idade": "65",
            "peso" : "55 kg",
            "isolamento": False,
            "deambula": True,
            "procedimento" : "Tomografia"
        }
    },
    {
        "numero" : 102,
        "ocupado" : False,
        "paciente" : {
            "nome" : "Ninguém",
            "idade": "0",
            "peso" : "0 kg",
            "isolamento": False,
            "deambula": False,
            "procedimento": ""
        }
    },
    {
        "numero" : 103,
        "ocupado" : True,
        "paciente" : {
            "nome" : "Margarida",
            "idade": "70",
            "peso" : "85 kg",
            "isolamento": True,
            "deambula": False,
            "procedimento": "Cirurgia"
        }
    },
    {
        "numero" : 104,
        "ocupado" : True,
        "paciente" : {
            "nome" : "Seu Nabi",
            "idade": "65",
            "peso" : "70 kg",
            "isolamento": False,
            "deambula": True,
            "procedimento": "Alta"
      }
    },
      {
        "numero" : 105,
        "ocupado" : True,
        "paciente" : {
            "nome" : "Dona Benta",
            "idade": 80,
            "peso" : "70 kg",
            "isolamento": False,
            "deambula": True,
            "procedimento": "Raio x"
      }
    }
            ]

funcionario = {}
funcionario["nome"] = input("Qual seu nome? : ").strip().lower()
funcionario["entrada"] = int(input("Horário de entrada: "))
funcionario["saida"] = int(input("Horário de saída: "))
horario_atual = int(input("Que horas são agora? "))

pode_trabalhar = verificar_horario(funcionario["nome"], funcionario["entrada"], funcionario["saida"], horario_atual)

if pode_trabalhar:
    print(f"\nOlá {funcionario['nome'].title()}! Bom plantão.")
    
    # MENU PRINCIPAL DO PLANTÃO
    planton_ativo = True
    while planton_ativo:
        print("\n=== CENTRAL DE MAQUEIROS ===")
        print("1 - Ver Leitos (Internação)")
        print("2 - Ver Ordens do Centro Cirúrgico (CC)")
        print("0 - Finalizar Plantão")
        
        opcao = input("Escolha o setor: ").strip()
        
        if opcao == "1":
            ordem_servico(hospital)
        elif opcao == "2":
            ordem_centro_cirurgico(hospital)
        elif opcao == "0":
            print("\n-- Plantão finalizado. Bom descanso! --")
            planton_ativo = False
        else:
            print("Opção inválida!")
