class Prescriptions:
    master_list = []
    count = 0
    def __init__(self, name, rx=None, date=None, duration=None, dose=None, doctor=None):
        self.name, self.rx, self.date, self.duration, self.dose, self.doctor = name, rx, date, duration, dose, doctor
        for i in range(len(Prescriptions.master_list)):
            if self.name not in Prescriptions.master_list[i]:
                Prescriptions.count += 1
    
    def unpack(self): # unpacking function to return tuple type with information on each medication
        return self.name, self.rx, self.date, self.duration, self.dose, self.doctor

    def load_name(self):
        Prescriptions.master_list.append(f'Name: {self.name}')
    
    def load_rx(self):
        Prescriptions.master_list.append(f'Rx: {self.rx}')

    def load_date(self):
        Prescriptions.master_list.append(f'Date: {self.date}')

    def load_duration(self):
        Prescriptions.master_list.append(f'Duration: {self.duration}')

    def load_dose(self):
        Prescriptions.master_list.append(f'Dose: {self.dose}')

    def load_doctor(self):
        Prescriptions.master_list.append(f'Doctor: {self.doctor}')

    def load_all(self):
        Prescriptions.master_list.append(f'Name: {self.name},Rx: {self.rx},Date: {self.date},Duration: {self.duration}, Dose: {self.dose},Doctor: {self.doctor}')