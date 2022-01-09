def main():
    #Import pyautogui to abort pyautogui
    from pyautogui import FailSafeException

    #Import threading to allow functions to run concurretly
    from threading import Thread

    #Run both functions concurrently unless PYAUTOGUI exception raised
    Thread(target= Turtle).start()
    Thread(target= automate_Clicking).start()

def Turtle():
    import turtle, random, pyautogui
    #This function opens a window that can safely be clicked on with no harmful effect for user. 
    def Change_Turtle_Color(x,y):
        #This function allows the opened to change color when clicked; just for fun.
        Color_List = ['red','green','white','blue','orange','pink']
        random_int = random.randint(0,5)
        screen = turtle.Screen()
        screen.bgcolor(Color_List[random_int])  

    #Opens window for user at full screen size preventing accidental clicking of other programs. 
    sc_Width, sc_Height = pyautogui.size()
    screen = turtle.Screen()
    screen.setup(sc_Width,sc_Height)

    #Adds message to window for user
    turtle.color('black')
    style = ('Arial', 30, 'italic')
    turtle.write('              Enjoy your day!\n Move mouse to corner to quit.', font=style, align='center')
    turtle.hideturtle()
    
    #Each time that the window is clicked it will change colors. 
    turtle.onscreenclick(Change_Turtle_Color)
    turtle.done()

def automate_Clicking():
        import pyautogui, time
        try:
            #Move mouse to middle of screen
            sc_Width, sc_Height = pyautogui.size()
            pyautogui.moveTo(x=sc_Width/2,y=sc_Height/2)
            pyautogui.click()
            time.sleep(2)
    
            for i in range (1, 0, -1):
                automate_Clicking()
        except:
            print(':)')

main()
