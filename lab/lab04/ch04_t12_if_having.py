def using_control_once() -> str:
    if "A" == "A":
        return "Success #1"


def using_control_again() -> str:
    if 10 == 10 :
        return "Success #2"


print(using_control_once())
print(using_control_again())
