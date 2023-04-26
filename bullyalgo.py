# Importing the time module
import time

# Creating a class for the Bully Algorithm
class BullyAlgorithm:
    # Defining the constructor of the class
    def __init__(self, process_id, processes):
        self.process_id = process_id
        self.processes = processes
        self.coordinator = None

    # Defining a method to start an election
    def start_election(self):
        # Printing a message indicating that the process has started an election
        print(f"Process {self.process_id} starts an election")

        # Finding the maximum process ID
        max_id = max(self.processes)

        # If the process ID is the maximum, it becomes the coordinator
        if self.process_id == max_id:
            self.coordinator = self.process_id
            print(f"Process {self.process_id} is elected as the coordinator")
        else:
            # Finding the higher process IDs
            higher_processes = [p for p in self.processes if p > self.process_id]
            # Sending election messages to the higher processes
            for p in higher_processes:
                try:
                    # Printing a message indicating that an election message has been sent
                    print(f"Process {self.process_id} sends an election message to process {p}")
                    # Waiting for 1 second
                    time.sleep(1)
                    # Sending the election message and waiting for a response
                    response = self.send_message(p, "election")
                    # If the response is "ok", continue with the loop
                    if response == "ok":
                        print(f"Process {p} responded with ok")
                        continue
                    # If the response is not "ok", start a new election
                    else:
                        print(f"Process {p} did not respond, so Process {self.process_id} starts another election")
                        self.start_election()
                        return
                # If there is an error, start a new election
                except:
                    print(f"Process {p} did not respond, so Process {self.process_id} starts another election")
                    self.start_election()
                    return
            # If all the higher processes respond with "ok", the process with the highest ID becomes the coordinator
            self.coordinator = max(higher_processes)
            print(f"Process {self.process_id} recognizes Process {self.coordinator} as the coordinator")

    # Defining a method to send a message
    def send_message(self, process_id, message):
        # Checking if the process ID is valid
        if process_id not in self.processes:
            return "error"
        # Responding to the message based on its type
        if message == "election":
            return "ok"
        elif message == "ok":
            return "ok"
        elif message == "coordinator":
            self.coordinator = process_id
            return "ok"
        else:
            return "error"

# The main function of the program
if __name__ == '__main__':
    # Defining a list of processes
    processes = [1, 2, 3, 4, 5]
    # Asking the user to enter the process ID
    process_id = int(input(f"Enter process ID (from {processes}): "))
    # Creating an instance of the BullyAlgorithm class
    bully = BullyAlgorithm(process_id, processes)
    # Starting the election
    bully.start_election()