# Assignment
# Cheong Wai Hong
# Python 3.7.3
# import module from library
import tkinter as tk 
import tkinter.font as tkFont
import random
import time

class App(tk.Tk):
    # Initiate 
    def __init__(self):
        super().__init__()
        # Set the program title and put the logo
        self.title('<EMLearn Math Learning Tool>')
        self.iconbitmap('math_icon.ico')

        # Set up the environment frame and give background color
        self.canvas = tk.Canvas(self,width=500, height=500)
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0),window=self.frame,anchor=tk.NW)
        self.canvas.grid(row = 0, column = 0, sticky="nswe")
        self.rowconfigure(0,weight= 1)
        self.columnconfigure(0,weight=1)
        self.update_idletasks()
        self.minsize(self.winfo_width(),self.winfo_height())
        self.active_bg_color()

        # Generelize the font size
        self.buttonFont = tkFont.Font(family = 'Jost',size=11,slant = 'italic',underline =1)
        self.labelFont = tkFont.Font(family = 'Jost',size=12)

        # Crest an active clock and put welcome words
        self.label_time = tk.Label(self.canvas,text = '',font = tkFont.Font(size=10))
        self.label_time.pack(pady=5)
        self.active_time_and_date()
        self.label_start = tk.Label(self.canvas,text = 'Welcome to EMLearn Math Learning Tool !!',font = tkFont.Font(family = 'Pangolin', size = 15))
        self.label_start.pack(pady = 20)
        self.name_start()

    # Backgrounf color active changing function
    def active_bg_color(self):
        color_bank = ['#52B2BF','#FFFF33','#FF99CC','#F9C2BC','#BFAD8A','#A1BF8A']
        color = random.choice(color_bank)
        self.canvas.config(bg = color)
        # 1000 means the milisecond unit
        self.after(1000,self.active_bg_color)
    
    # Active time function
    def active_time_and_date(self):
        self.label_time.config(text=time.asctime())
        self.after(500,self.active_time_and_date)

    # Start by entering the name
    def name_start(self):
        self.label_name = tk.Label(self.canvas, text = 'Enter your nick-name for this practice : ',font = self.labelFont)
        self.label_name.pack(pady = 20)
        self.name = tk.Entry(self.canvas,textvariable = tk.StringVar )
        self.name.pack(pady=20)
        self.btn_go = tk.Button(self.canvas, text = 'Go ==>',font = self.buttonFont, command = self.main_start)
        self.btn_go.pack(pady=20)
        self.btn_quit = tk.Button(self.canvas, text = 'Quit',font = self.buttonFont, command = self.quit)
        self.btn_quit.pack(pady = 30)   

    def main_start(self):
        self.label_showName = tk.Label(self.canvas,text = 'Welcome !  ' + self.name.get(),font = self.labelFont)
        self.label_showName.pack(pady=10)
        # Remove the provious widgets
        self.label_name.destroy()
        self.name.destroy()
        self.btn_go.destroy()
        self.btn_quit.destroy()
        # Perform to select level
        self.level_start()

    # Select Level function
    def level_start (self):
        self.btn_elementary = tk.Button(self.canvas, text = 'Elementary Level',font = self.buttonFont,command = self.start_elementary )
        self.btn_elementary.pack(pady = 25)
        self.btn_inter = tk.Button(self.canvas, text = 'Intermediate Level',font = self.buttonFont,command = self.start_intermediate )
        self.btn_inter.pack(pady = 25)
        self.btn_advance = tk.Button(self.canvas, text = 'Advance Level',font = self.buttonFont,command = self.start_advance )
        self.btn_advance.pack(pady = 25)
        self.btn_history = tk.Button(self.canvas, text = 'History Result',font = self.buttonFont,command = self.history_result )
        self.btn_history.pack(pady = 30)
        self.btn_quit = tk.Button(self.canvas, text = 'Quit',font = self.buttonFont,compound = tk.CENTER, command = self.quit)
        self.btn_quit.pack(pady = 25)        

    ################
    #Elementary Level
    def start_elementary(self):    
        # remove the previous function widgets
        self.label_start.destroy()
        self.btn_history.destroy()
        self.btn_elementary.destroy()
        self.btn_inter.destroy()
        self.btn_advance.destroy()
        self.btn_quit.destroy()

        # Display information
        self.label_level = tk.Label(self.canvas,text = 'Level   <Elementary>   [  +   -  ]',font = self.labelFont)
        self.label_level.pack(pady = 10)   
        self.label_round = tk.Label(self.canvas,text='Please input the number of round(s) :',font = self.labelFont)
        self.label_round.pack(pady = 20)

        # Initialize the variables
        self.question_bank = []
        self.correct = 0
        self.wrong = 0

        # Make data entry with Interger format
        self.var = tk.IntVar()
        self.rounds = tk.Entry(self.canvas,textvariable = self.var)
        self.rounds.pack(pady = 20)
        
        self.btn_getStart = tk.Button(self.canvas,text = "Get Started -- Elementary",font = self.buttonFont, command = self.elementary_check_round)
        self.btn_getStart.pack(pady = 20)
        self.btn_back = tk.Button(self.canvas,text = " <-- Back",font = self.buttonFont, command = self.back)
        self.btn_back.pack(pady = 20)
      
    # Input Validation of rounds
    def elementary_check_round(self):
        self.btn_getStart.destroy()
        self.btn_back.destroy()
        try :
            num = int(self.rounds.get())
        except ValueError:
            self.label_round.destroy()
            self.rounds.destroy()
            self.label_level.destroy()
            self.start_elementary()
        else :
            self.num = int(self.rounds.get())
            if self.num == 0 :
                self.label_round.destroy()
                self.rounds.destroy()
                self.label_level.destroy()
                self.start_elementary()
            else:
                self.label_round.destroy()
                self.elementary_1(self.num)
                self.rounds.destroy()
                
    # Generate Queations and ask for answer
    def elementary_1(self,times):
        if times > 0:
            self.var_1 = tk.IntVar()
            a = random.randint(0,10)
            b = random.randint(0,10)
            operator_list = ['+','-']
            operator = random.choice(operator_list)
            if operator == '+' :
                self.question = str(a) + operator + str(b)
                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                self.actual_number =int(a + b)
                self.label_1.pack(pady = 20)
                self.answer.pack(pady = 20)
            else :
                # change number position to do not lead negative question
                if a > b :
                    self.question = str(a) + operator + str(b)
                    self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                    self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                    self.actual_number =int(a - b)
                    self.label_1.pack(pady = 20)
                    self.answer.pack(pady = 20)
                else :
                    self.question = str(b) + operator + str(a)
                    self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                    self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                    self.actual_number =int(b - a)
                    self.label_1.pack(pady = 20)
                    self.answer.pack(pady = 20)
            
            self.btn_submit = tk.Button(self.canvas,text = "Submit",font = self.buttonFont, command = self.check_elementary)
            self.btn_submit.pack(pady = 20)
            self.round_count = int(times - 1)
        
    # Make as a bridge to repeat generating the question
    def elementary_2(self):
        self.btn_next.destroy()
        self.label_2.destroy()
        self.elementary_1(self.round_count)

    # Check Anaswer
    def check_elementary(self):
        self.btn_submit.destroy()
        self.label_1.destroy()
        # Input validation of input value
        try :
            a_1 = int(self.answer.get())
        except ValueError:
            self.answer.destroy()
            self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
            self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
            self.label_1.pack(pady = 20)
            self.answer.pack(pady = 20)
            self.btn_submit = tk.Button(self.canvas,text = "Submit",font = self.buttonFont, command = self.check_elementary)
            self.btn_submit.pack(pady = 20)
        else:
            a_1 = int(self.answer.get())
            b_1 = self.actual_number
            if a_1 == b_1:
                self.label_2 = tk.Label(self.canvas,text = 'Your answer is correct !!',font = self.labelFont)
                self.correct += 1
                self.question_bank.append(self.question + " = " + str(a_1) + "\t(Correct)")
                self.label_2.pack(pady = 20)
                if self.round_count > 0:
                    self.btn_next = tk.Button(self.canvas,text = "Next",font = self.buttonFont, command = self.elementary_2)
                    self.btn_next.pack(pady = 20)
            else:
                self.label_2 = tk.Label(self.canvas,text='sorry, you give the wrong answer \n The correct answer is ' + str(self.actual_number),font = self.labelFont)
                self.wrong += 1
                self.question_bank.append(self.question + " = " + str(a_1) + "\t(Incorrect)")
                self.label_2.pack(pady = 20)
                if self.round_count > 0:
                    self.btn_next = tk.Button(self.canvas,text = "Next",font = self.buttonFont, command = self.elementary_2)
                    self.btn_next.pack(pady = 20)
            # For the last question 
            if self.round_count == 0 :
                self.btn_checkResult = tk.Button(self.canvas,text = "Check Result",font = self.buttonFont, command = self.result)
                self.btn_checkResult.pack(pady = 20)
                # Save the result into local memory
                result_ele = open('historyRecord_ele.txt','a')
                result_ele.write('\n'+str(time.asctime())+'          '+ '{:.2f}'.format(eval(str((self.correct / self.num)*100))) + '%')
                result_ele.close()

            self.answer.destroy()     

    ################
    #Intermediate Level
    def start_intermediate(self):
        # remove the previous function widgets    
        self.label_start.destroy()
        self.btn_history.destroy()
        self.btn_elementary.destroy()
        self.btn_inter.destroy()
        self.btn_advance.destroy()
        self.btn_quit.destroy()

        # Display information
        self.label_level = tk.Label(self.canvas,text = 'Level   <Intermediate>  [  +  -  *  /  ]',font = self.labelFont)
        self.label_level.pack(pady = 10)                  
        self.label_round = tk.Label(self.canvas,text='Please input the number of round(s) :',font = self.labelFont)
        self.label_round.pack(pady = 20)

        # Initialize the variables
        self.question_bank = []
        self.correct = 0
        self.wrong = 0

        # Make data entry with Interger format
        self.var = tk.IntVar()
        self.rounds = tk.Entry(self.canvas,textvariable = self.var)
        self.rounds.pack(pady = 20)
        
        self.btn_getStart = tk.Button(self.canvas,text = "Get Started -- Intermediate",font = self.buttonFont, command = self.intermediate_check_round)
        self.btn_getStart.pack(pady = 20)
        self.btn_back = tk.Button(self.canvas,text = " <-- Back",font = self.buttonFont, command = self.back)
        self.btn_back.pack(pady = 20)
    
    # Input Validation of rounds
    def intermediate_check_round(self):
        self.btn_getStart.destroy()
        self.btn_back.destroy()
        try :
            num = int(self.rounds.get())
        except ValueError:
            self.label_round.destroy()
            self.rounds.destroy()
            self.label_level.destroy()
            self.start_intermediate()
        else :
            self.num = int(self.rounds.get())
            if num == 0 :
                self.label_round.destroy()
                self.rounds.destroy()
                self.label_level.destroy()
                self.start_intermediate()
            else:
                self.label_round.destroy()
                self.intermediate_1(num)
                self.rounds.destroy()

    # Generate Queations and ask for answer
    def intermediate_1(self,times):
        if times > 0:
            self.var_1 = tk.IntVar()
            # a, b for addition and subtraction question
            # c, d for multiplication and division question
            a = random.randint(0,30)
            b = random.randint(0,30)
            c = random.randint(0,12)
            d = random.randint(0,12)
            operator_list = ['+','-','*','/']
            operator = random.choice(operator_list)
            if operator == '+' :
                self.question = str(a) + operator + str(b)
                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                self.actual_number =int(a + b)
                self.label_1.pack(pady = 20)
                self.answer.pack(pady = 20)
            elif operator == '-':
                # change number position to do not lead negative question
                if a > b :
                    self.question = str(a) + operator + str(b)
                    self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                    self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                    self.actual_number =int(a - b)
                    self.label_1.pack(pady = 20)
                    self.answer.pack(pady = 20)
                else :
                    self.question = str(b) + operator + str(a)
                    self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                    self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                    self.actual_number =int(b - a)
                    self.label_1.pack(pady = 20)
                    self.answer.pack(pady = 20)
            elif operator == '*':
                self.question = str(c) + operator + str(d)
                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                self.actual_number =int(c * d)
                self.label_1.pack(pady = 20)
                self.answer.pack(pady = 20)
            else :
                while True:
                    # generate again if there is zero division error and appear fractional question
                    c = random.randint(0,12)
                    d = random.randint(0,12)
                    # change position and do not lead fractional question
                    if c > d :
                        # Check is there occur a Zero Division Error
                        try :
                            c % d
                        except ZeroDivisionError:
                            continue
                        else :
                            if c % d != 0:
                                continue
                            else :
                                self.question = str(c) + operator + str(d)
                                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                                self.actual_number =int(c / d)
                                self.label_1.pack(pady = 20)
                                self.answer.pack(pady = 20)
                                break
                    else:
                        try :
                            d % c
                        except ZeroDivisionError:
                            continue
                        else :
                            if d % c != 0:
                                continue
                            else :
                                self.question = str(d) + operator + str(c)
                                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                                self.actual_number =int(d / c)
                                self.label_1.pack(pady = 20)
                                self.answer.pack(pady = 20)
                                break
            self.btn_submit = tk.Button(self.canvas,text = "Submit",font = self.buttonFont, command = self.check_intermediate)
            self.btn_submit.pack(pady = 20)
            self.round_count = int(times - 1)
    
    # Make as a bridge to repeat generating the question
    def intermediate_2(self):
        self.btn_next.destroy()
        self.label_2.destroy()
        self.intermediate_1(self.round_count)

    # Check Anaswer
    def check_intermediate(self):
        self.btn_submit.destroy()
        self.label_1.destroy()
        # Input validation of input value
        try :
            a_1 = int(self.answer.get())
        except ValueError:
            self.answer.destroy()
            self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
            self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
            self.label_1.pack(pady = 20)
            self.answer.pack(pady = 20)
            self.btn_submit = tk.Button(self.canvas,text = "Submit",font = self.buttonFont, command = self.check_elementary)
            self.btn_submit.pack(pady = 20)
        else:
            a_1 = int(self.answer.get())
            b_1 = self.actual_number
            if a_1 == b_1:
                self.label_2 = tk.Label(self.canvas,text = 'Your answer is correct !!',font = self.labelFont)
                self.correct += 1
                self.question_bank.append(self.question + " = " + str(a_1) + "\t(Correct)")
                self.label_2.pack(pady = 20)
                if self.round_count > 0:
                    self.btn_next = tk.Button(self.canvas,text = "Next",font = self.buttonFont, command = self.intermediate_2)
                    self.btn_next.pack(pady = 20)
            else:
                self.label_2 = tk.Label(self.canvas,text='sorry, you give the wrong answer \n The correct answer is ' + str(self.actual_number),font = self.labelFont)
                self.wrong += 1
                self.question_bank.append(self.question + " = " + str(a_1) + "\t(Incorrect)")
                self.label_2.pack(pady = 20)
                if self.round_count > 0:
                    self.btn_next = tk.Button(self.canvas,text = "Next",font = self.buttonFont, command = self.intermediate_2)
                    self.btn_next.pack(pady = 20)
            # For the last question
            if self.round_count ==0 :
                self.btn_checkResult = tk.Button(self.canvas,text = "Check Result",font = self.buttonFont, command = self.result)
                self.btn_checkResult.pack(pady = 20)
                # Save the result into local memory
                result_inter = open('historyRecord_inter.txt','a')
                result_inter.write('\n'+str(time.asctime())+'          '+ '{:.2f}'.format(eval(str((self.correct / self.num)*100))) + '%')
                result_inter.close()
            self.answer.destroy()

    #################################
    # Advance Level
    def start_advance(self):
        # remove the previous function widgets 
        self.label_start.destroy()
        self.btn_history.destroy()
        self.btn_elementary.destroy()
        self.btn_inter.destroy()
        self.btn_advance.destroy()
        self.btn_quit.destroy()

        # Display information
        self.label_level = tk.Label(self.canvas,text = 'Level   <Advance>  [  +  -  *  /  ]',font = self.labelFont)
        self.label_level.pack(pady = 10)                  
        self.label_round = tk.Label(self.canvas,text='Please input the number of round(s) :',font = self.labelFont)
        self.label_round.pack(pady = 20)

        # Initialize the variables
        self.question_bank = []
        self.correct = 0
        self.wrong = 0

        # Make data entry with Interger format
        self.var = tk.IntVar()
        self.rounds = tk.Entry(self.canvas,textvariable = self.var)
        self.rounds.pack(pady = 20)
        
        self.btn_getStart = tk.Button(self.canvas,text = "Get Started -- Advance",font = self.buttonFont, command = self.advance_check_round)
        self.btn_getStart.pack(pady = 20)
        self.btn_back = tk.Button(self.canvas,text = " <-- Back",font = self.buttonFont, command = self.back)
        self.btn_back.pack(pady = 20)

    # Input Validation of rounds
    def advance_check_round(self):
        self.btn_getStart.destroy()
        self.btn_back.destroy()
        try :
            num = int(self.rounds.get())
        except ValueError:
            self.label_round.destroy()
            self.rounds.destroy()
            self.label_level.destroy()
            self.start_advance()
        else :
            self.num = int(self.rounds.get())
            if num == 0 :
                self.label_round.destroy()
                self.rounds.destroy()
                self.label_level.destroy()
                self.start_advance()
            else:
                self.label_round.destroy()
                self.advance_1(num)
                self.rounds.destroy()
    
    # Generate Queations and ask for answer
    def advance_1(self,times):
        if times > 0:
            self.var_1 = tk.IntVar()
            # a, b and c is used for additional and subtraction question
            # d and e is used for multiplication and division
            a = random.randint(0,50)
            b = random.randint(0,50)
            c = random.randint(0,50)
            d = random.randint(0,20)
            e = random.randint(0,20)
            operator_list = ['+','-','*','/']
            operator = random.choice(operator_list)
            if operator == '+' :
                self.question = str(a) + operator + str(b) + operator + str(c)
                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                self.actual_number =int(a + b + c)
                self.label_1.pack(pady = 20)
                self.answer.pack(pady = 20)
            elif operator == '-':
                # change number position to do not lead negative question
                if a > b :
                    self.question = str(a) + operator + str(b) + ' + ' + str(c)
                    self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                    self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                    self.actual_number =int(a - b + c)
                    self.label_1.pack(pady = 20)
                    self.answer.pack(pady = 20)
                else :
                    self.question = str(b) + operator + str(a) + ' + ' + str(c)
                    self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                    self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                    self.actual_number =int(b - a + c)
                    self.label_1.pack(pady = 20)
                    self.answer.pack(pady = 20)
            elif operator == '*':
                self.question = str(d) + operator + str(e)
                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                self.actual_number =int(d * e)
                self.label_1.pack(pady = 20)
                self.answer.pack(pady = 20)
            else :
                # Check is there occur a Zero Division Error
                while True:
                    # generate again if there is zero division error and appear fractional question
                    d = random.randint(0,20)
                    e = random.randint(0,20)
                    # change number position to do not lead fractional answer
                    if d > e :
                        try :
                            d % e
                        except ZeroDivisionError:
                            continue
                        else :
                            if d % e != 0:
                                continue
                            else :
                                self.question = str(d) + operator + str(e)
                                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                                self.actual_number =int(d / e)
                                self.label_1.pack(pady = 20)
                                self.answer.pack(pady = 20)
                                break
                    else:
                        try :
                            e % d
                        except ZeroDivisionError:
                            continue
                        else :
                            if e % d != 0:
                                continue
                            else :
                                self.question = str(e) + operator + str(d)
                                self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
                                self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
                                self.actual_number =int(e / d)
                                self.label_1.pack(pady = 20)
                                self.answer.pack(pady = 20)
                                break
            self.btn_submit = tk.Button(self.canvas,text = "Submit",font = self.buttonFont, command = self.check_advance)
            self.btn_submit.pack(pady = 20)
            self.round_count = int(times - 1)
    
    # Make as a bridge to repeat generating the question
    def advance_2(self):
        self.btn_next.destroy()
        self.label_2.destroy()
        self.advance_1(self.round_count)

    # Check Anaswer
    def check_advance(self):
        self.btn_submit.destroy()
        self.label_1.destroy()
        # Input validation of input value
        try :
            a_1 = int(self.answer.get())
        except ValueError:
            self.answer.destroy()
            self.label_1 = tk.Label(self.canvas,text = self.question + '\n Answer Now',font = self.labelFont)
            self.answer = tk.Entry(self.canvas, textvariable = self.var_1)
            self.label_1.pack(pady = 20)
            self.answer.pack(pady = 20)
            self.btn_submit = tk.Button(self.canvas,text = "Submit",font = self.buttonFont, command = self.check_advance)
            self.btn_submit.pack(pady = 20)
        else:
            a_1 = int(self.answer.get())
            b_1 = self.actual_number
            if a_1 == b_1:
                self.label_2 = tk.Label(self.canvas,text = 'Your answer is correct !!',font = self.labelFont)
                self.correct += 1
                self.question_bank.append(self.question + " = " + str(a_1) + "\t(Correct)")
                self.label_2.pack(pady = 20)
                if self.round_count > 0:
                    self.btn_next = tk.Button(self.canvas,text = "Next",font = self.buttonFont, command = self.advance_2)
                    self.btn_next.pack(pady = 20)
            else:
                self.label_2 = tk.Label(self.canvas,text='sorry, you give the wrong answer \n The correct answer is ' + str(self.actual_number),font = self.labelFont)
                self.wrong += 1
                self.question_bank.append(self.question + " = " + str(a_1) + "\t(Incorrect)")
                self.label_2.pack(pady = 20)
                if self.round_count > 0:
                    self.btn_next = tk.Button(self.canvas,text = "Next",font = self.buttonFont, command = self.advance_2)
                    self.btn_next.pack(pady = 20)
            # For the last question
            if self.round_count ==0 :
                self.btn_checkResult = tk.Button(self.canvas,text = "Check Result",font = self.buttonFont, command = self.result)
                self.btn_checkResult.pack(pady = 20)
                # Save the result into local memory
                result_adv = open('historyRecord_adv.txt','a')
                result_adv.write('\n'+str(time.asctime())+'          '+ '{:.2f}'.format(eval(str((self.correct / self.num)*100))) + '%')
                result_adv.close()

            self.answer.destroy()
    
    ####################
    # Display Result Function
    def result(self):
        self.btn_checkResult.destroy()
        self.label_2.destroy()
        self.label_num_rounds = tk.Label(self.canvas,text = 'You have answered  ' + str(len(self.question_bank))+'  questions.',font = self.labelFont)
        self.label_3 = tk.Label(self.canvas,text = 'Correct ==>' + str(self.correct),font = self.labelFont)
        self.label_4 = tk.Label(self.canvas,text = 'Wronged ==>' + str(self.wrong),font = self.labelFont)
        self.label_num_rounds.pack(pady = 5)  
        self.label_3.pack(pady = 5)
        self.label_4.pack(pady = 5) 
        
        self.label_5 = tk.Label(self.canvas,text = 'Play again ? ',font = self.labelFont)
        self.label_5.pack(pady = 5)
        # Play Again
        self.btn_again = tk.Button(self.canvas,text = 'Again', font = self.buttonFont, command = self.clear)
        self.btn_again.pack(pady = 5)
        # Quit
        self.btn_quit = tk.Button(self.canvas, text = 'Quit', font = self.buttonFont, command = self.quit)
        self.btn_quit.pack(pady = 5)
        # Check History Result
        self.btn_history = tk.Button(self.canvas, text = 'History Result',font = self.buttonFont,command = self.history_result )
        self.btn_history.pack(pady = 5)

        # Completed Question display by using listbox
        self.listNodes = tk.Listbox(self.canvas, width=30, height=30)
        self.listNodes.pack(side="left", fill='y',expand=True, padx = 100,pady=20)
        # adding scroll bar in case there are many questions
        self.scrollbar = tk.Scrollbar(self.canvas, orient="vertical")
        self.scrollbar.config(command=self.listNodes.yview)
        self.scrollbar.pack(side="right", fill=tk.BOTH,pady = 20)
        self.listNodes.config(yscrollcommand=self.scrollbar.set)
        # Insert the question into the listbox
        for x in self.question_bank:
            self.listNodes.insert(tk.END, str(x))
        
    # Check history result function
    def history_result(self):
        # create a pop out window
        self.popOut = tk.Toplevel()
        self.popOut.iconbitmap('math_icon.ico')
        
        clear_btn = tk.Button(self.popOut,text = 'Clear All',font = self.buttonFont,command = self.clear_history)
        clear_btn.pack(pady=5)
        exit_btn = tk.Button(self.popOut,text = 'Exit',font = self.buttonFont,command = self.exit_history)
        exit_btn.pack(pady=5)

        label_title = tk.Label(self.popOut,text='Elementary\t\t\tIntermediate\t\t\t\tAdvance',font = tkFont.Font(size=13))
        label_title.pack()
        # open the record file for elementary and read it
        historyEle = open('historyRecord_ele.txt','r')
        Ele = [line.rstrip() for line in historyEle]
        historyEle.close()
        # display it by using list box
        self.eleBox = tk.Listbox(self.popOut, width=50, height=30)
        self.eleBox.pack(side="left", fill='y',expand=True, padx = 10,pady=5)
        self.scrollbar = tk.Scrollbar(self.popOut, orient="vertical")
        self.scrollbar.config(command=self.eleBox.yview)
        self.scrollbar.pack(side="right", fill=tk.BOTH,pady = 20)
        self.eleBox.config(yscrollcommand=self.scrollbar.set)
        for x in Ele:
            self.eleBox.insert(tk.END, str(x))
        
        # open the record file for intermediate and read it
        historyInter = open('historyRecord_inter.txt','r')
        Inter = [line.rstrip() for line in historyInter]
        historyInter.close()
        # display it by using list box
        self.interBox = tk.Listbox(self.popOut, width=50, height=30)
        self.interBox.pack(side="left", fill='y',expand=True, padx = 10,pady=5)
        self.scrollbar = tk.Scrollbar(self.popOut, orient="vertical")
        self.scrollbar.config(command=self.interBox.yview)
        self.scrollbar.pack(side="right", fill=tk.BOTH,pady = 20)
        self.interBox.config(yscrollcommand=self.scrollbar.set)
        for x in Inter:
            self.interBox.insert(tk.END, str(x))

        # open the record file for advance and read it
        historyAdv = open('historyRecord_adv.txt','r')
        Adv = [line.rstrip() for line in historyAdv]
        historyAdv.close()
        # display it by using list box
        self.advBox = tk.Listbox(self.popOut, width=50, height=30)
        self.advBox.pack(side="left", fill='y',expand=True, padx = 10,pady=5)
        self.scrollbar = tk.Scrollbar(self.popOut, orient="vertical")
        self.scrollbar.config(command=self.advBox.yview)
        self.scrollbar.pack(side="right", fill=tk.BOTH,pady = 20)
        self.advBox.config(yscrollcommand=self.scrollbar.set)
        for x in Adv:
            self.advBox.insert(tk.END, str(x))


    # Remove all the result record function
    def clear_history(self):
        # open all the files and rewrite all
        historyEle = open('historyRecord_ele.txt','w')
        historyInter = open('historyRecord_inter.txt','w')
        historyAdv = open('historyRecord_adv.txt','w')
        historyEle.write('Date                                              Score')
        historyInter.write('Date                                              Score')
        historyAdv.write('Date                                              Score')
        historyEle.close()
        historyInter.close()
        historyAdv.close()
        self.popOut.destroy()
        self.history_result()
        
    # Exit the check history window
    def exit_history(self):
        self.popOut.destroy()

    # Re-run the program by clearing all the widget and forward to select level page
    def clear(self):
        self.label_3.destroy()
        self.listNodes.destroy()
        self.label_4.destroy()
        self.label_num_rounds.destroy()
        self.label_5.destroy()
        self.btn_again.destroy()
        self.btn_quit.destroy()
        self.scrollbar.destroy()
        self.label_level.destroy()
        self.btn_history.destroy()
        self.level_start()

    # Backward function
    def back(self):
        self.label_round.destroy()
        self.rounds.destroy()
        self.btn_getStart.destroy()
        self.btn_back.destroy()
        self.label_level.destroy()
        self.level_start()
               
    # End Program  function
    def quit(self):
        self.label_close = tk.Label(self.canvas,text = 'Goodbye ! The program will close soon ...',font = self.labelFont)
        self.label_close.pack(pady = 20)
        self.after(2000,self.destroy)

# Execute the program
if __name__ == "__main__":
    app = App()
    app.mainloop()