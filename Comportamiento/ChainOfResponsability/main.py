"""3. Implementa la lógica del ejemplo."""


from handler import LevelOneSupportHandler, LevelTwoSupportHandler
from request import Request


def main():
    level_two = LevelTwoSupportHandler(None)
    level_one = LevelOneSupportHandler(level_two)

    #request = Request(1)
    request = Request(2)
    level_one.handle_request(request)

if __name__ == "__main__":
    main()