import time
from datetime import datetime
import threading


def set_reminder(reminder_time, message):
    current_time = datetime.now()
    delay = (reminder_time - current_time).total_seconds()

    if delay < 0:
        print("Вы не можете установить напоминание на прошлое время.")
        return

    def reminder_thread():
        time.sleep(delay)
        print(f"\nНапоминание: {message}")

    threading.Thread(target=reminder_thread).start()
    print(f"Напоминание установлено на {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")


print("Программа напоминаний запущена.")
print("Введите дату и время напоминания в формате YYYY-MM-DD HH:MM и текст напоминания.")

while True:
    user_input = input("Введите напоминание (или 'exit' для выхода): ")

    if user_input.lower() == "exit":
        print("Выход из программы.")
        break

    try:
        parts = user_input.split(" ", 2)
        if len(parts) < 3:
            print("Неверный формат. Используйте: YYYY-MM-DD HH:MM Сообщение")
            continue

        date_part = parts[0]
        time_part = parts[1]
        message = parts[2]

        reminder_time = datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H:%M")
        set_reminder(reminder_time, message)

    except ValueError:
        print("Неверный формат даты или времени. Попробуйте снова.")
