def is_palindrome(text):
    # facem litere mici
    text_mic = text.lower()

    text_curat = text_mic.replace(" ", "")

    # inversarea textului
    text_invers = text_curat[::-1]

    # verificare palindrom
    if text_curat == text_invers:
        return True
    else:
        return False


print("Introdu textul:")
input_text = input()

if input_text == "":
    print("Nu ai introdus nimic.")
else:
    rezultat = is_palindrome(input_text)

    if rezultat == True:
        print("Este palindrom")
    else:
        print("Nu este palindrom")