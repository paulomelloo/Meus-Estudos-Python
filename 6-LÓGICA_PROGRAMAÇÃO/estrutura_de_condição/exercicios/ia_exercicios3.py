"""
Simular um sistema de login simples.
Defina um login e uma senha corretos (por exemplo, login_correto = "admin" e senha_correta = "1234").
Peça ao usuário para digitar o login_digitado e a senha_digitada.
Se o login_digitado for igual ao login_correto E a senha_digitada for igual à senha_correta, mostre: "Acesso concedido. Bem-vindo!"
Senão, se (elif) a senha_digitada for diferente da senha_correta E o login_digitado for igual ao login_correto, mostre: "Senha incorreta."
Senão (se o login estiver incorreto), mostre: "Login inválido."
"""

login_digitado = input("Digite o login: ")
senha_digitado = input("Digite a senha: ")

if login_digitado == "admin":
    if senha_digitado == "1234":
        print(f"Acesso concedido. Bem vindo!")
    else:
        print(f"Senha incorreta.")
else:
    print(f"Login Invalido!")