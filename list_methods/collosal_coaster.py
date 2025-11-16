exp_q = ['tony', 'Bruce']
normal_q = ['Robotguy', 'WW']
ticket_type = 0
persona_name = "Hawkeye"




def add_me_to_the_q(exp_q, normal_q, ticket_type, persona_name):
    if ticket_type == 1:
        exp_q.append(persona_name)
        return exp_q
    else:
        normal_q.append(persona_name)
        return normal_q
    

print(add_me_to_the_q(exp_q, normal_q, ticket_type, persona_name))