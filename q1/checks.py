def show_states_conf(state):
    print("\t{0} {1} {2}\n\t{3} {4} {5}\n\t{6} {7} {8}\n".format(
        state[0], state[1], state[2],
        state[3], state[4], state[5],
        state[6], state[7], state[8]
        )
        )

def check_solvable(state):
    acc = 0
    temp_state = state[:]
    temp_state.remove(0)
    for n1 in range(len(temp_state)):
        for n2 in range(n1, len(temp_state)):
            if temp_state[n1] > temp_state[n2]: acc += 1

    if acc % 2 == 1:
        print("[erro] configuração impossível de ser solucionada!")
        return False
    else:
        print("[info] solucionável, pode tentar!")
        return True

def check_state(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return state == goal_state

def check_is_state_valid(state):
    if len(state) != 9:
        print("[erro] estado inválido: tamanho {} não permitido.".format(len(state)))
        return False
    for i in range(9):
        if i not in state:
            print("[erro] estado inválido: pelo menos um valor no intervalo (0-8) faltando.")
            return False
    return True


