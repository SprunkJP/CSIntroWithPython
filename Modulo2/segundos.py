segundosTotais = int(input("Por favor, entre com o número de segundos que deseja converter: "))
horasTotais = segundosTotais // 3600
horasRestantes = horasTotais % 24
dias = horasTotais // 24
segundosRestantes = segundosTotais % 3600
minutos = segundosRestantes // 60
segundos = segundosRestantes % 60

print(dias, "dias,", horasRestantes, "horas,", minutos, "minutos e", segundos, "segundos.")
