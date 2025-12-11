#and , or, not

high_income = True
good_creadit = True

if high_income and good_creadit:
    print("eligiable")
else: 
    print("not eligiable")


if high_income or  good_creadit:
    print("eligiable")
else: 
    print("not eligiable")
    

    high_income = False 
    good_creadit = True
    student = True

    if high_income and good_creadit and not student:
        print("eligiable")
    else:
        print("not eligible")

