





f=open("pagina.html", "r")
template = f.read()

titulo = input()
texto = input()
res = template.replace("TITULO",titulo)
res = res.replace("TEXTO",texto)

print(res)
