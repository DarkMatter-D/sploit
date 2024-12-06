class main_prompt:
    def main_prompt():
        prompt = input("sploit:>")
        return (prompt)
class handlers:
    def main_handler(function):
        if function == "e":
            print("E")
            main_prompt.main_prompt()
    while True:
        main_handler(main_prompt.main_prompt())