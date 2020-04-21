import os
import tkinter
window = tkinter.Tk()
window.title("System")
def shutdown():
    os.system("shutdown /s /t 1")
def restart():
    os.system("shutdown /r /t 1")
def leave():
    exit()

tkinter.Label(window, text= "Choose an option",font= ("Arial",30)).pack()


tkinter.Button(window, text = "Shutdown", command = shutdown).pack()
tkinter.Button(window, text = "Restart", command = restart).pack()
tkinter.Button(window, text = "exit", command = leave).pack()

window.geometry('480x540')

window.mainloop()


#print("1. Shutdown Computer")
#print("2. Restart Computer")
#print("3. Exit")
#choice = int(input("\nEnter your choice: "))
#if(choice>=1 and choice<=2):
#    if choice == 1:
#        os.system("shutdown /s /t 1")
#    else:
#        os.system("shutdown /r /t 1")
#else:
#    exit()