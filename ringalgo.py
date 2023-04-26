class Pro:
    def __init__(self, id):
        self.id = id
        self.act = True  # flag to indicate if the process is active or not

class GFG:
    def __init__(self):
        self.TotalProcess = 0  # number of processes in the system
        self.process = []  # list of process objects
  
    def initialiseGFG(self):
        print("No of processes: 7")
        self.TotalProcess = 7
        self.process = [Pro(i) for i in range(self.TotalProcess)]  # create Pro objects for each process
  
    def Election(self):
        print("Process no " + str(self.process[self.FetchMaximum()].id) + " fails")  # print the ID of the process with the highest ID (i.e., the one that "fails")
        self.process[self.FetchMaximum()].act = False  # set the flag of the failed process to False
        print("Election Initiated by 3")
        initializedProcess = 3  # the process that initiates the election

        old = initializedProcess
        newer = old + 1

        while (True):
            if (self.process[newer].act):
                print("Process " + str(self.process[old].id) + " pass Election(" + str(self.process[old].id) + ") to " + str(self.process[newer].id))  # print the message passed between processes
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if (newer == initializedProcess):
                break

        print("Process " + str(self.process[self.FetchMaximum()].id) + " becomes coordinator")  # print the ID of the new coordinator
        coord = self.process[self.FetchMaximum()].id

        old = coord
        newer = (old + 1) % self.TotalProcess
        while (True):
            if (self.process[newer].act):
                print("Process " + str(self.process[old].id) + " pass Coordinator(" + str(coord) + ") message to process " + str(self.process[newer].id))  # print the message passed between processes
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if (newer == coord):
                print("End Of Election ")
                break
  
    def FetchMaximum(self):
        maxId = -9999
        ind = 0
        for i in range(self.TotalProcess):
            if (self.process[i].act and self.process[i].id > maxId):
                maxId = self.process[i].id
                ind = i
        return ind

def main():
    obj = GFG()
    obj.initialiseGFG()
    obj.Election()

if __name__ == "__main__":
    main()