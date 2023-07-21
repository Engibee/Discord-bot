import model
from control import MyClient

def do_something(com,argu):
    match(com):
        case "!rank":
            model.rank_check(argu)
        case "!rsge":
            model.ge_pricecheck(argu)
        case "!cot":
            model.cot(argu)
        case _:
            MyClient.message.channel.send("Comando inválido")