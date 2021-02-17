from Tkinter import *
import RPi.GPIO as GPIO ## Import GPIO library
import time

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.setup(11, GPIO.OUT) ## Valve 1 - Palma
GPIO.setup(12, GPIO.OUT) ## Valve 2 - vizigyoker
GPIO.setup(13, GPIO.OUT) ## Valve 3 - Palma felso
GPIO.setup(15, GPIO.OUT) ## Valve 4 - Kukorica
GPIO.setup(16, GPIO.OUT) ## Valve 5 - Kaktusz
GPIO.setup(18, GPIO.OUT) ## Valve 6 - Pafrany

GPIO.output(7,1) ## Turn off Motor
GPIO.output(11,1) ## Turn off Valve1
GPIO.output(12,1) ## Turn off Valve2
GPIO.output(13,1) ## Turn off Valve3
GPIO.output(15,1) ## Turn off Valve4
GPIO.output(16,1) ## Turn off Valve5
GPIO.output(18,1) ## Turn off Valve6



root = Tk() #main window
root.title("Ontozes")

def locsolas():                          #function
       
        alma = (var1.get())
        korte = (ido1.get())
        if alma == 1 :
                GPIO.output(7,0) ## Turn on Motor
                print ("Szivattyu bekapcsol")
                time.sleep(2)
                GPIO.output(11,0) ## Turn on Valve 1 PALMA 10
                time.sleep(korte)
                GPIO.output(11,1) ## Turn on Valve 1 PALMA 10
                time.sleep(2)
                GPIO.output(7,1) ## Turn off Motor
                print ("Szivattyu kikapcsol")
        alma = (var2.get())
        korte = (ido2.get())
        if alma == 1 :
                GPIO.output(7,0) ## Turn on Motor
                print ("Szivattyu bekapcsol")
                time.sleep(2)
                GPIO.output(12,0) ## Turn on Valve 2
                time.sleep(korte)
                GPIO.output(12,1) ## Turn on Valve 2
                time.sleep(2)
                GPIO.output(7,1) ## Turn off Motor
                print ("Szivattyu kikapcsol")
        alma = (var3.get())
        korte = (ido3.get())
        if alma == 1 :
                GPIO.output(7,0) ## Turn on Motor
                print ("Szivattyu bekapcsol")
                time.sleep(2)
                GPIO.output(13,0) ## Turn on Valve 3
                time.sleep(korte)
                GPIO.output(13,1) ## Turn on Valve 3 
                time.sleep(2)
                GPIO.output(7,1) ## Turn off Motor
                print ("Szivattyu kikapcsol")
        alma = (var4.get())
        korte = (ido4.get())
        if alma == 1 :
                GPIO.output(7,0) ## Turn on Motor
                print ("Szivattyu bekapcsol")
                time.sleep(2)
                GPIO.output(15,0) ## Turn on Valve 4
                time.sleep(korte)
                GPIO.output(15,1) ## Turn on Valve 4 
                time.sleep(2)
                GPIO.output(7,1) ## Turn off Motor
                print ("Szivattyu kikapcsol")
        alma = (var5.get())
        korte = (ido5.get())
        if alma == 1 :
                GPIO.output(7,0) ## Turn on Motor
                print ("Szivattyu bekapcsol")
                time.sleep(2)
                GPIO.output(16,0) ## Turn on Valve 5
                time.sleep(korte)
                GPIO.output(16,1) ## Turn on Valve 5 
                time.sleep(2)
                GPIO.output(7,1) ## Turn off Motor
                print ("Szivattyu kikapcsol")
        alma = (var6.get())
        korte = (ido6.get())
        if alma == 1 :
                GPIO.output(7,0) ## Turn on Motor
                print ("Szivattyu bekapcsol")
                time.sleep(2)
                GPIO.output(18,0) ## Turn on Valve 3
                time.sleep(korte)
                GPIO.output(18,1) ## Turn on Valve 3 
                time.sleep(2)
                GPIO.output(7,1) ## Turn off Motor
                print ("Szivattyu kikapcsol")
        GPIO.output(16,1) ## Turn on Valve 1
        GPIO.output(11,1) ## Turn off Valve 1
        GPIO.output(12,1) ## Turn on Valve 1
        GPIO.output(13,1) ## Turn on Valve 1
        GPIO.output(15,1) ## Turn on Valve 1
        GPIO.output(18,1) ## Turn on Valve 1
        GPIO.output(7,1) ## Turn off Motor
        
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
ido1 = IntVar()
ido2 = IntVar()
ido3 = IntVar()
ido4 = IntVar()
ido5 = IntVar()
ido6 = IntVar()
Checkbutton(root, text="Palma", variable=var1).grid(row=0, column=0)
cs1 = Scale(root, from_=0, to=40,variable=ido1, orient=HORIZONTAL).grid(row=0, column=1) #Csuszk letrehozasa
Checkbutton(root, text="Buzoganyvirag", variable=var2).grid(row=1, column=0)
cs2 = Scale(root, from_=0, to=40,variable=ido2, orient=HORIZONTAL).grid(row=1, column=1) #Csuszk letrehozasa
Checkbutton(root, text="FelsoPalma", variable=var3).grid(row=2, column=0)
cs3 = Scale(root, from_=0, to=40,variable=ido3, orient=HORIZONTAL).grid(row=2, column=1) #Csuszk letrehozasa
Checkbutton(root, text="KukoricaVirag", variable=var4).grid(row=3, column=0)
cs4 = Scale(root, from_=0, to=40,variable=ido4, orient=HORIZONTAL).grid(row=3, column=1) #Csuszk letrehozasa
Checkbutton(root, text="Kaktusz", variable=var5).grid(row=4, column=0)
cs5 = Scale(root, from_=0, to=40,variable=ido5, orient=HORIZONTAL).grid(row=4, column=1) #Csuszk letrehozasa
Checkbutton(root, text="Pafrany", variable=var6).grid(row=5, column=0)
cs6 = Scale(root, from_=0, to=40,variable=ido6, orient=HORIZONTAL).grid(row=5, column=1) #Csuszk letrehozasa
ontozes = Button(root, text="ONTOZES", fg="green",command=locsolas).grid(row=6, column=0)
kilepes = Button(root, text="KILEPES", fg="red",command=root.quit).grid(row=6, column=1)
root.mainloop()
