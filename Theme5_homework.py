from datetime import *
def analize_date(date_str):
    date_format = [
        ("%A, %B %d, %Y", "The Moscow Times"),
        ("%A, %d.%m.%y", "The Guardian"),
        ("%A, %d %B %Y", "Daily News")
    ]

    for fmt, newspaper in date_format:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            print(f"{newspaper}: {date_obj}")
            return
        except ValueError:
            continue

    print("Формат даты не соответствует ни одному известному формату")
def main():
    print("Введите дату в формате газеты или 'exit' для завершения")

    while True:
        user_input = input("Введите дату: ")
        if user_input.lower() == "exit":
            break
        analize_date(user_input)

if __name__ == "__main__":
    main()