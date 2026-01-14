def is_palindrome(cuvant):
    cuvant = cuvant.lower()

    # creez o variabila goala pentru cuvantul inversat
    cuvant_invers = ""

    # iau fiecare litera din cuvantul original
    for litera in cuvant:
        #inversez cuvantul
        cuvant_invers = litera + cuvant_invers

    # la final compar
    if cuvant == cuvant_invers:
        return True
    else:
        return False


text = input("Introdu un cuvant: ")

if text.isalpha():
    #apelare fucntie
    if is_palindrome(text):
        print("Este palindrom.")
    else:
        print("Nu este palindrom.")
else:
    print("Introdu doar litere.")