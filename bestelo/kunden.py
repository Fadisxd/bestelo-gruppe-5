"""Kunden von Bestelo.

Oben:  Kunde (Basisklasse) und Privatkunde       → Person 1 (Abschnitt 5.1)
Unten: Geschaeftskunde und Verein                → Person 2 (Abschnitt 5.2)

Bitte vor dem Arbeiten immer `git pull` – Person 1 und 2 teilen sich diese Datei.
"""

class Kunde:
    def __init__(self, kundennummer: int, name: str, email: str,):
        self.kundennummer = kundennummer
        self.name = name
        self.email = email

    @property
    def kundennummer(self) -> str:
        return self._kundennummer

    @kundennummer.setter
    def kundennummer(self, wert: int):
        if wert < 1000:
            raise ValueError (f"Kundennummer muss mindestes 1000 sein")
        self._kundennummer = wert

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, angabe: str):
        angabe = angabe.strip()
        if angabe == "":
            raise ValueError (f"Name darf nicht leer sein")
        self._name = angabe

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, wert: str) -> None:
        if not Kunde.ist_gueltige_email(wert):
            raise ValueError(f"email ist ungültig")
        self._email = wert

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        if "@" not in email:
            return False
        teile = email.split("@", 1)
        return "." in teile [1]

    
    def begruessung(self) -> str:
        return(f"Hallo {self.name}!")
    

    def rabattsatz(self) -> float:
        return 0.0
        

    def __str__ (self) -> str:
        return(f"Kunde {self.kundennummer}: {self.name} {self.email} ")

    def __repr__ (self) -> str:
        return f"{type(self).__name__}({self.kundennummer}, '{self.name}')"

    def __eq__ (self, other: object) -> bool:
        if not isinstance(other, Kunde):
            return NotImplemented
        return self.kundennummer == other.kundennummer
    



anna = Kunde(1001, " Anna Müller ", "anna@example.com")
print(anna)
print(repr(anna))
print(anna.begruessung(), anna.rabattsatz())
print(anna == Kunde(1001, "A. Müller", "a.mueller@example.com"))
print(Kunde.ist_gueltige_email("anna-at-example.com"))
try:
    anna.name = " "
except ValueError as fehler:
    print("Fehler:", fehler)

        