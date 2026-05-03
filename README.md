Student Health Services: Patient Queue System
A command-line program that manages patient flow for a student health clinic. 
It supports regular appointment booking, a waitlist, emergency prioritization, and cancellations.


When prompted, enter the number of appointment slots available for the day. The clinic will open and wait for commands.

Commands
book() Registers a new patient and adds them into the queue 
If the clinic is full, adds them to the waitlist queue.
emergency() registers an emergency patient who will be seen before all others.
cancel() Cancels a booked appointment by patient ID. Automatically moves the first waitlisted patient into the open 
next() Calls the next patient. Emergencies are always seen first.
status() Displays the current booked queue, emergency list, and waitlist.
quit() Closes the program. 

Data Structures Used
Linked List (LinkedList)
Serves as the central log of all currently booked patients. Patients are added to the end when booked and removed by ID when seen or cancelled.
Patient Queue (PatientQueue)
Manages three lists internally:

queue: booked patients in arrival order (FIFO), capped at max_capacity
waitlist: patients who arrived when the clinic was full, also FIFO
emergency: emergency patients who are always seen first regardless of arrival order

Node
Each patient is wrapped in a Node object so they can be stored in the linked list.
