# Juntando listas (join). Serve para 'somar' (juntar) duas ou mais listas

ids_instrutores = [1,2,3]
ids_alunos_py = [10,9]
ids_alunos_csharp = [8,10]

ids_bylearners = ids_instrutores + ids_alunos_py
print(ids_bylearners)

ids_bylearners += ids_alunos_csharp
print(ids_bylearners)

