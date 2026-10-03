
from foremka.foremka import Foremka
from foremka.foremkaProstokatna import ForemkaProstokatna
from foremka.foremkaOkragla import ForemkaOkragla
from foremka.foremkaTrojkatna import ForemkaTrojkatna

if __name__ == '__main__':
    ob1 = Foremka("Metalowa", "Okrągła")
    print(Foremka.opis(ob1))

    print("\n")
    ob2 = ForemkaProstokatna(ob1.material, 5.0, 3.2)
    print(ForemkaProstokatna.opis(ob2))
    print(ForemkaProstokatna.pole(ob2))
    print(ForemkaProstokatna.obwod(ob2))

    print("\n")
    ob3 = ForemkaOkragla(ob2.material, 5.0)
    print(ForemkaOkragla.opis(ob3))
    print(ForemkaOkragla.pole(ob3))
    print(ForemkaOkragla.obwod(ob3))

    print("\n")
    ob3 = ForemkaTrojkatna(ob2.material, 5.0)
    print(ForemkaTrojkatna.opis(ob3))
    print(ForemkaTrojkatna.pole(ob3))
    print(ForemkaTrojkatna.obwod(ob3))