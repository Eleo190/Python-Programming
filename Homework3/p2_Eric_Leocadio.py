#PROBLEM 2
class ParkingPermit:
    def __init__(self, name:str, months:int, schedule:dict):
        """initialize a basic parking permit, recording the name, amount of months purchased and the fee schedule"""
        self._name = name
        self._months = months
        self._schedule = schedule
    def cost(self):
        pass
    def __str__(self) -> str:
        """string representation of class information"""
        return f"Permit info for {self._name}: {self._months} months, Price: ${self.cost()}"

    def __repr__(self) -> str:
        """Return technical representation of permit."""
        return f"ParkingPermit(name={self._name}, months={self._months}, schedule={self._schedule})"

class StudentPermit(ParkingPermit):
    def __init__(self, name:str, months:int, schedule:dict, vehicle_amt:int):
        """initialize a student parking permit, recording the name, amount of months purchased, the fee schedule, and the amount of vehicles registered"""
        super().__init__(name, months, schedule)
        self._vehicle_amt = vehicle_amt
    def cost(self)->float:
        """Returns the cost of the Student permit, based on $25/month with a one time fee of $10 per car over 1"""
        return self._months*self._schedule['student_monthly'] + self._schedule['vehicle_fee']*max(0, self._vehicle_amt-1)
    def __str__(self):
        """string representation of class information"""
        return f"Student permit for {self._name}: {self._months} months, {self._vehicle_amt} vehicle(s) registered, Price: ${self.cost()}"
    
    def __repr__(self) -> str:
            """Return technical representation of permit."""
            return f"StudentPermit(name={self._name}, months={self._months}, schedule={self._schedule}, vehicle_amt={self._vehicle_amt})"
    

class FacultyPermit(ParkingPermit):
    def __init__(self, name:str, months:int, schedule:dict, garage_access:bool):
        """initialize a basic parking permit, recording the name, amount of months purchased, the fee schedule, and if the permit includes garage access"""
        super().__init__(name, months, schedule)
        self._garage_access = garage_access
    def cost(self)->float:
        """Returns the cost of the Faculty permit, based on $40/month or $55/month with garage access"""
        if self._garage_access == True:
            return self._months*(self._schedule['faculty_monthly']+self._schedule['garage_monthly'])
        else: return self._months*self._schedule['faculty_monthly']

    def __str__(self):
        """string representation of class information"""
        return f"Faculty permit for {self._name}: {self._months} months, Has garage access: {self._garage_access}, Price: ${self.cost()}"
            
    def __repr__(self) -> str:
            """Return technical representation of permit."""
            return f"FacultyPermit(name={self._name}, months={self._months}, schedule={self._schedule}, garage_access={self._garage_access})"

def summarize_lists(permits:list) -> float:
    total = 0.0
    for permit in permits:
        print(permit)
        total += permit.cost()
    return total

def main():
    cost_schedule = {'student_monthly': 25, 'vehicle_fee': 10, 'faculty_monthly': 40, 'garage_monthly': 15}
    student_perm1 = StudentPermit('Austin', 3, cost_schedule, 2)
    student_perm2 = StudentPermit('Ally', 1, cost_schedule, 1)
    faculty_perm1 = FacultyPermit('Patricia', 2, cost_schedule, True)
    faculty_perm2 = FacultyPermit('Robert', 3, cost_schedule, False)

    print(summarize_lists([student_perm1, student_perm2, faculty_perm1, faculty_perm2]))

if __name__ == "__main__":
    main()