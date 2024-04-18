class Schueler:
    def __init__(self, name):
        self.name = name
        self.received_messages = []

    def send_message(self, recipient, message):
        """Funktion zum Senden einer Nachricht"""
        recipient.receive_message(message, self.name)
        print(f"{self.name} hat '{message}' an {recipient.name} gesendet.")

    def receive_message(self, message, sender_name):
        self.received_messages.append(f"{sender_name}: {message}")

    def display_messages(self):
        print(f"Nachrichten für {self.name}:")
        for message in self.received_messages:
            print(message)

# Beispielverwendung
schueler1 = Schueler("Max")
schueler2 = Schueler("Lisa")


schueler1.send_message(schueler2, "Wie gehts?")
schueler2.send_message(schueler1, "Gut und dir?")

schueler2.display_messages()
schueler1.display_messages()