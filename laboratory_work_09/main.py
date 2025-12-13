print("=" * 50)
print("СВИНАЯ ЛАТЫНЬ ИНТЕРПРЕТАТОР")
print("=" * 50)
print("\nКак писать:")
print("  intpray('текст на свиной латыни');")
print("  # комментарий")
print("  exit - выход")
print("\nПравила свиной латыни:")
print("  гласная вначале → +yay: apple → appleyay")
print("  согласная вначале → буква в конец +ay: hello → ellohay")
print("-" * 50)

while True:
    user_input = input("\n> ").strip()

    if user_input.lower() in ('exit', 'quit'):
        print("Oodbyegay!")
        break

    if user_input.startswith('#'):
        continue

    # Проверяем команду intpray
    if user_input.startswith('intpray("') and user_input.endswith('");'):
        # Извлекаем текст внутри кавычек
        text = user_input[9:-3]

        # Переводим из свиной латыни
        words = text.split()
        result = []
        for word in words:
            word_lower = word.lower()

            # Убираем знаки препинания в конце
            punctuation = ''
            while word and not word[-1].isalpha():
                punctuation = word[-1] + punctuation
                word = word[:-1]

            if word_lower.endswith('yay'):
                translated = word[:-3]
            elif word_lower.endswith('ay'):
                translated = word[-3] + word[:-3]
            else:
                translated = word

            result.append(translated + punctuation)

        print(' '.join(result))
    else:
        print("Только: intpray('текст');")