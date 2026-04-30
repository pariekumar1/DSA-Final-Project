class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = newNode

    def delete(self, patient_id):
        if self.head is None:
            return False
        if self.head.data['id'] == patient_id:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.data['id'] == patient_id:
                current.next = current.next.next
                return True
            current = current.next
        return False


class PatientQueue:
    def __init__(self, max_capacity):
        self.queue = []
        self.waitlist = []
        self.emergency = []
        self.max_capacity = max_capacity
        self.pid = 1

    def book(self, name):
        patient = {'id': self.pid, 'name': name}
        self.pid += 1
        if len(self.queue) < self.max_capacity:
            self.queue.append(patient)
            print("Booked: " + name + " (ID " + str(patient['id']) + ")")
        else:
            self.waitlist.append(patient)
            print("Appointments full. Adding " + name + " to waitlist at position " + str(len(self.waitlist)) + ".")
        return patient

    def add_emergency(self, name):
        patient = {'id': self.pid, 'name': name}
        self.pid += 1
        self.emergency.append(patient)
        print("EMERGENCY: " + name + " (ID " + str(patient['id']) + ") added — will be seen first.")
        return patient

    def cancel(self, patient_id, appointments):
        for p in self.queue:
            if p['id'] == patient_id:
                self.queue.remove(p)
                appointments.delete(patient_id)
                print("Cancelled appointment for " + p['name'] + ".")
                if self.waitlist:
                    next_up = self.waitlist.pop(0)
                    self.queue.append(next_up)
                    appointments.insertEnd(Node(next_up))
                    print("Notifying " + next_up['name'] + ": a slot is now available!")
                return
        print("Patient ID " + str(patient_id) + " not found in booked appointments.")

    def see_next(self):
        if self.emergency:
            p = self.emergency.pop(0)
            print("Seeing EMERGENCY: " + p['name'] + " (ID " + str(p['id']) + ").")
        elif self.queue:
            p = self.queue.pop(0)
            print("Seeing: " + p['name'] + " (ID " + str(p['id']) + ").")
            if self.waitlist:
                next_up = self.waitlist.pop(0)
                self.queue.append(next_up)
                print("Notifying " + next_up['name'] + ": a slot is now available!")
        else:
            print("No patients remaining.")

    def status(self):
        print("\n--- Clinic Status ---")
        print("Booked (" + str(len(self.queue)) + "/" + str(self.max_capacity) + "): " +
              (", ".join(p['name'] + " #" + str(p['id']) for p in self.queue) if self.queue else "empty"))
        print("Emergency (" + str(len(self.emergency)) + "): " +
              (", ".join(p['name'] + " #" + str(p['id']) for p in self.emergency) if self.emergency else "empty"))
        print("Waitlist (" + str(len(self.waitlist)) + "): " +
              (", ".join(p['name'] + " #" + str(p['id']) for p in self.waitlist) if self.waitlist else "empty"))
        print("---------------------\n")


# --- Main loop ---
appointments = LinkedList()

capacity = int(input("How many appointments are available today? "))
clinic = PatientQueue(capacity)
print("Clinic open. Commands: book, emergency, cancel, next, status, quit\n")

while True:
    command = input("Command: ").strip().lower()

    if command == "book":
        name = input("Patient name: ").strip()
        patient = clinic.book(name)
        if patient in clinic.queue:
            appointments.insertEnd(Node(patient))

    elif command == "emergency":
        name = input("Patient name: ").strip()
        clinic.add_emergency(name)

    elif command == "cancel":
        pid = int(input("Patient ID to cancel: ").strip())
        clinic.cancel(pid, appointments)

    elif command == "next":
        clinic.see_next()

    elif command == "status":
        clinic.status()

    elif command == "quit":
        print("Clinic closed.")
        break

    else:
        print("Unknown command. Try: book, emergency, cancel, next, status, quit")