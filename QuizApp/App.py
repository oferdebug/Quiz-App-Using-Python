import tkinter as tk

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome To My Quiz About Pc's!")
        self.geometry("600x400")
        self.configure(background="black")
        
        self.current_question = 0
        self.score = 0
        
        self.questions = [
            {"question": "What does CPU stand for?",
             "options": ["Central Processing Unit", "Computer Processing Unit", "Central Processor Unit", "Computer Processor Unit"],
             "answer": "Central Processing Unit"},
            {"question": "Which programming language is widely used for web development and is known for its flexibility and simplicity?",
             "options": ["Java", "Python", "JavaScript", "C++"],
             "answer": "JavaScript"},
            {"question": "What does HTML stand for?",
             "options": ["Hyperlinks and Text Markup Language", "Hyper Text Markup Language", "High Text Markup Language", "Hyper Transfer Markup Language"],
             "answer": "Hyper Text Markup Language"},
            {"question": "What is the purpose of RAM in a computer?",
             "options": ["To store the operating system", "To store data permanently", "To store frequently accessed data and programs for quick access by the CPU", "To store files and documents"],
             "answer": "To store frequently accessed data and programs for quick access by the CPU"},
            {"question": "Which component of a computer connects all its parts together and allows data to be transferred between them?",
             "options": ["CPU", "RAM", "Motherboard", "Hard Drive"],
             "answer": "Motherboard"},
            {"question": "What does SSD stand for?",
             "options": ["Super Speed Drive", "Solid State Drive", "System Storage Device", "Secure Software Drive"],
             "answer": "Solid State Drive"},
            {"question": "Which networking protocol is commonly used for sending emails?",
             "options": ["HTTP", "SMTP", "FTP", "DHCP"],
             "answer": "SMTP"},
            {"question": "What does VPN stand for?",
             "options": ["Virtual Personal Network", "Virtual Private Network", "Verified Personal Network", "Very Private Network"],
             "answer": "Virtual Private Network"},
            {"question": "Which company developed the Windows operating system?",
             "options": ["Apple", "Microsoft", "IBM", "Google"],
             "answer": "Microsoft"},
            {"question": "What is the primary function of a firewall in computer security?",
             "options": ["To protect against physical theft of hardware", "To prevent unauthorized access to or from a private network", "To recover lost data", "To clean viruses from the system"],
             "answer": "To prevent unauthorized access to or from a private network"}
        ]
        
        self.label_question = tk.Label(self, text="", bg="black", fg="white")
        self.label_question.pack()
        
        self.radio_var = tk.StringVar()
        self.radio_var.set(None)
        
        self.radio_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self, text="", variable=self.radio_var, value=i, bg="black", fg="white")
            button.pack()
            self.radio_buttons.append(button)
        
        self.button_submit = tk.Button(self, text="Submit", command=self.submit_answer, bg="black", fg="white")
        self.button_submit.pack()
        
        self.label_result = tk.Label(self, text="", bg="black", fg="white")
        self.label_result.pack()
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.label_question.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option)
        else:
            self.show_result()
    
    def submit_answer(self):
        selected_option = self.radio_var.get()
        if selected_option is not None:
            question_data = self.questions[self.current_question]
            if question_data["options"][int(selected_option)] == question_data["answer"]:
                self.score += 1
                self.label_result.config(text="Correct!", fg="green")
            else:
                self.label_result.config(text="Incorrect!", fg="red")
            self.current_question += 1
            self.load_question()
    
    def show_result(self):
        self.label_question.config(text="")
        for button in self.radio_buttons:
            button.destroy()
        self.button_submit.destroy()
        self.label_result.config(text=f"Your score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
