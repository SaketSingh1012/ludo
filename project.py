from tkinter import*
from PIL import ImageTk,Image
import os
import random
mm=""
rr=Tk()
class ludo:
    def __init__(self,r):
        self.val=554
        self.val2=280
        self.vall=0
        self.val22=0
        self.valll=0
        self.val222=0
        self.vallll=0
        self.val2222=0
        self.blue1=0
        self.bluee1=0
        self.blue11=0
        self.bluee11=0
        self.blue111=0
        self.bluee111=0
        self.blue1111=0
        self.bluee1111=0
        self.turn=1
        self.open1=0
        self.open2=0
        self.open3=0
        self.open4=0
        self.openn1=0
        self.openn2=0
        self.openn3=0
        self.openn4=0
        self.f=Frame(r,height=800,width=800,bg="white")
        self.f.pack()
        self.f.propagate(0)
        self.c=Canvas(self.f,height=250,width=300,bg="red")
        self.c.place(x=0,y=0)
        self.c1=Canvas(self.f,height=250,width=300,bg="blue")
        self.c1.place(x=500,y=0)
        self.c2=Canvas(self.f,height=250,width=300,bg="yellow")
        self.c2.place(x=0,y=450)
        self.c3=Canvas(self.f,height=250,width=300,bg="green")
        self.c3.place(x=500,y=450)
        self.m=Canvas(self.f,height=63,width=50,bg="white")
        self.m.place(x=0,y=252)
        self.m1=Canvas(self.f,height=63,width=50,bg="white")
        self.m1.place(x=0,y=318)
        self.m2=Canvas(self.f,height=63,width=50,bg="white")
        self.m2.place(x=0,y=382)
        self.m3=Canvas(self.f,height=63,width=50,bg="red")
        self.m3.place(x=50,y=252)
        self.m4=Canvas(self.f,height=63,width=50,bg="red")
        self.m4.place(x=50,y=318)
        self.m5=Canvas(self.f,height=63,width=50,bg="white")
        self.m5.place(x=50,y=382)
        self.m6=Canvas(self.f,height=63,width=50,bg="white")
        self.m6.place(x=100,y=252)
        self.m7=Canvas(self.f,height=63,width=50,bg="red")
        self.m7.place(x=100,y=318)
        self.m8=Canvas(self.f,height=63,width=50,bg="red")
        self.m8.place(x=100,y=382)
        self.m9=Canvas(self.f,height=63,width=50,bg="white")
        self.m9.place(x=150,y=252)
        self.m10=Canvas(self.f,height=63,width=50,bg="red")
        self.m10.place(x=150,y=318)
        self.m11=Canvas(self.f,height=63,width=50,bg="white")
        self.m11.place(x=150,y=382)
        self.m12=Canvas(self.f,height=63,width=50,bg="white")
        self.m12.place(x=200,y=252)
        self.m13=Canvas(self.f,height=63,width=50,bg="red")
        self.m13.place(x=200,y=318)
        self.m14=Canvas(self.f,height=63,width=50,bg="white")
        self.m14.place(x=200,y=382)
        self.m9=Canvas(self.f,height=63,width=50,bg="white")
        self.m9.place(x=250,y=252)
        self.m10=Canvas(self.f,height=63,width=50,bg="red")
        self.m10.place(x=250,y=318)
        self.m11=Canvas(self.f,height=63,width=50,bg="white")
        self.m11.place(x=250,y=382)
        self.q=Canvas(self.f,height=63,width=50,bg="white")
        self.q.place(x=746,y=252)
        self.q1=Canvas(self.f,height=63,width=50,bg="white")
        self.q1.place(x=746,y=318)
        self.q2=Canvas(self.f,height=63,width=50,bg="white")
        self.q2.place(x=746,y=382)
        self.q3=Canvas(self.f,height=63,width=50,bg="white")
        self.q3.place(x=696,y=252)
        self.q4=Canvas(self.f,height=63,width=50,bg="green")
        self.q4.place(x=696,y=318)
        self.q5=Canvas(self.f,height=63,width=50,bg="green")
        self.q5.place(x=696,y=382)
        self.q6=Canvas(self.f,height=63,width=50,bg="green")
        self.q6.place(x=646,y=252)
        self.q7=Canvas(self.f,height=63,width=50,bg="green")
        self.q7.place(x=646,y=318)
        self.q8=Canvas(self.f,height=63,width=50,bg="white")
        self.q8.place(x=646,y=382)
        self.q6=Canvas(self.f,height=63,width=50,bg="white")
        self.q6.place(x=596,y=252)
        self.q7=Canvas(self.f,height=63,width=50,bg="green")
        self.q7.place(x=596,y=318)
        self.q8=Canvas(self.f,height=63,width=50,bg="white")
        self.q8.place(x=596,y=382)
        self.q9=Canvas(self.f,height=63,width=50,bg="white")
        self.q9.place(x=546,y=252)
        self.q10=Canvas(self.f,height=63,width=50,bg="green")
        self.q10.place(x=546,y=318)
        self.q11=Canvas(self.f,height=63,width=50,bg="white")
        self.q11.place(x=546,y=382)
        self.q12=Canvas(self.f,height=63,width=50,bg="white")
        self.q12.place(x=500,y=252)
        self.q13=Canvas(self.f,height=63,width=50,bg="green")
        self.q13.place(x=500,y=318)
        self.q14=Canvas(self.f,height=63,width=50,bg="white")
        self.q14.place(x=500,y=382)
        self.w1=Canvas(self.f,height=40,width=64,bg="white")
        self.w1.place(x=302,y=0)
        self.w2=Canvas(self.f,height=40,width=64,bg="white")
        self.w2.place(x=369,y=0)
        self.w3=Canvas(self.f,height=40,width=64,bg="white")
        self.w3.place(x=434,y=0)
        self.w4=Canvas(self.f,height=40,width=64,bg="white")
        self.w4.place(x=302,y=40)
        self.w5=Canvas(self.f,height=40,width=64,bg="blue")
        self.w5.place(x=369,y=40)
        self.w6=Canvas(self.f,height=40,width=64,bg="blue")
        self.w6.place(x=434,y=40)
        self.w7=Canvas(self.f,height=40,width=64,bg="blue")
        self.w7.place(x=302,y=80)
        self.w8=Canvas(self.f,height=40,width=64,bg="blue")
        self.w8.place(x=369,y=80)
        self.w9=Canvas(self.f,height=40,width=64,bg="white")
        self.w9.place(x=434,y=80)
        self.w10=Canvas(self.f,height=40,width=64,bg="white")
        self.w10.place(x=302,y=120)
        self.w11=Canvas(self.f,height=40,width=64,bg="blue")
        self.w11.place(x=369,y=120)
        self.w12=Canvas(self.f,height=40,width=64,bg="white")
        self.w12.place(x=434,y=120)
        self.w13=Canvas(self.f,height=42,width=64,bg="white")
        self.w13.place(x=302,y=160)
        self.w14=Canvas(self.f,height=42,width=64,bg="blue")
        self.w14.place(x=369,y=160)
        self.w15=Canvas(self.f,height=42,width=64,bg="white")
        self.w15.place(x=434,y=160)
        self.w16=Canvas(self.f,height=45,width=64,bg="white")
        self.w16.place(x=302,y=204)
        self.w17=Canvas(self.f,height=45,width=64,bg="blue")
        self.w17.place(x=369,y=204)
        self.w18=Canvas(self.f,height=45,width=64,bg="white")
        self.w18.place(x=434,y=204)
        self.e1=Canvas(self.f,height=40,width=64,bg="white")
        self.e1.place(x=302,y=660)
        self.e2=Canvas(self.f,height=40,width=64,bg="white")
        self.e2.place(x=369,y=660)
        self.e3=Canvas(self.f,height=40,width=64,bg="white")
        self.e3.place(x=434,y=660)
        self.e4=Canvas(self.f,height=40,width=64,bg="yellow")
        self.e4.place(x=302,y=620)
        self.e5=Canvas(self.f,height=40,width=64,bg="yellow")
        self.e5.place(x=369,y=620)
        self.e6=Canvas(self.f,height=40,width=64,bg="white")
        self.e6.place(x=434,y=620)
        self.e7=Canvas(self.f,height=40,width=64,bg="white")
        self.e7.place(x=302,y=580)
        self.e8=Canvas(self.f,height=40,width=64,bg="yellow")
        self.e8.place(x=369,y=580)
        self.e9=Canvas(self.f,height=40,width=64,bg="yellow")
        self.e9.place(x=434,y=580)
        self.e10=Canvas(self.f,height=40,width=64,bg="white")
        self.e10.place(x=302,y=540)
        self.e11=Canvas(self.f,height=40,width=64,bg="yellow")
        self.e11.place(x=369,y=540)
        self.e12=Canvas(self.f,height=40,width=64,bg="white")
        self.e12.place(x=434,y=540)
        self.e13=Canvas(self.f,height=44,width=64,bg="white")
        self.e13.place(x=302,y=494)
        self.e14=Canvas(self.f,height=44,width=64,bg="yellow")
        self.e14.place(x=369,y=494)
        self.e15=Canvas(self.f,height=44,width=64,bg="white")
        self.e15.place(x=434,y=494)
        self.e16=Canvas(self.f,height=45,width=64,bg="white")
        self.e16.place(x=302,y=450)
        self.e17=Canvas(self.f,height=45,width=64,bg="yellow")
        self.e17.place(x=369,y=450)
        self.e18=Canvas(self.f,height=45,width=64,bg="white")
        self.e18.place(x=434,y=450)
        self.cn=Canvas(self.f,height=200,width=196,bg="grey")
        self.cn.create_polygon(100,100,0,0,0,205,fill="red")
        self.cn.create_polygon(100,100,0,0,205,0,fill="blue")
        self.cn.create_polygon(100,100,205,0,205,208,fill="green")
        self.cn.create_polygon(100,100,0,205,205,205,fill="yellow")
        self.cn.place(x=302,y=250)
        self.r=Canvas(self.f,height=180,width=240)
        self.r1=Canvas(self.f,height=55,width=65,bg="red")
        self.r1.place(x=60,y=50)
        self.r2=Canvas(self.f,height=55,width=65,bg="red")
        self.r2.place(x=170,y=50)
        self.r3=Canvas(self.f,height=55,width=65,bg="red")
        self.r3.place(x=60,y=140)
        self.r1=Canvas(self.f,height=55,width=65,bg="red")
        self.r1.place(x=170,y=140)
        self.r.place(x=30,y=30)
        self.b=Canvas(self.f,height=180,width=240)
        self.b1=Canvas(self.f,height=55,width=65,bg="blue")
        self.b1.place(x=560,y=50)
        self.b2=Canvas(self.f,height=55,width=65,bg="blue")
        self.b2.place(x=670,y=50)
        self.b3=Canvas(self.f,height=55,width=65,bg="blue")
        self.b3.place(x=560,y=140)
        self.b4=Canvas(self.f,height=55,width=65,bg="blue")
        self.b4.place(x=670,y=140)
        self.b.place(x=530,y=30)
        self.y=Canvas(self.f,height=180,width=240)
        self.y1=Canvas(self.f,height=55,width=65,bg="yellow")
        self.y1.place(x=60,y=500)
        self.y2=Canvas(self.f,height=55,width=65,bg="yellow")
        self.y2.place(x=170,y=500)
        self.y3=Canvas(self.f,height=55,width=65,bg="yellow")
        self.y3.place(x=60,y=600)
        self.y4=Canvas(self.f,height=55,width=65,bg="yellow")
        self.y4.place(x=170,y=600)
        self.y.place(x=30,y=490)
        self.g=Canvas(self.f,height=180,width=240)
        self.g1=Canvas(self.f,height=55,width=65,bg="green")
        self.g1.place(x=560,y=500)
        self.g2=Canvas(self.f,height=55,width=65,bg="green")
        self.g2.place(x=670,y=500)
        self.g3=Canvas(self.f,height=55,width=65,bg="green")
        self.g3.place(x=560,y=600)
        self.g4=Canvas(self.f,height=55,width=65,bg="green")
        self.g4.place(x=670,y=600)
        self.g.place(x=530,y=490)
        self.yy1=Button(self.f,text='1',width=1,height=1,bg="yellow")
        self.yy1.place(x=80,y=610)
        self.yy2=Button(self.f,text='2',width=1,height=1,bg="yellow")
        self.yy2.place(x=190,y=610)
        self.yy3=Button(self.f,text='3',width=1,height=1,bg="yellow")
        self.yy3.place(x=80,y=510)
        self.yy4=Button(self.f,text='4',width=1,height=1,bg="yellow")
        self.yy4.place(x=190,y=510)
        self.bb1=Button(self.f,text='1',width=1,height=1,bg="blue")
        self.bb1.place(x=580,y=70)
        self.bb2=Button(self.f,text='2',width=1,height=1,bg="blue")
        self.bb2.place(x=690,y=70)
        self.bb3=Button(self.f,text='3',width=1,height=1,bg="blue")
        self.bb3.place(x=580,y=150)
        self.bb4=Button(self.f,text='4',width=1,height=1,bg="blue")
        self.bb4.place(x=690,y=150)
        self.d=Button(self.f,height=2,width=5,text="dice",command=self.dice)
        self.d.place(x=380,y=325)
        print("1st palyer turn press dice")
    def game(self):
        self.yy1.destroy()
        self.yy1=Button(self.f,text='1',width=1,height=1,bg="yellow")
        self.yy1.place(x=self.val,y=self.val2)
        
    def game1(self):
        self.yy2.destroy()
        self.yy2=Button(self.f,text='2',width=1,height=1,bg="yellow")
        self.yy2.place(x=self.vall,y=self.val22)
    
    def game2(self):
        self.yy3.destroy()
        self.yy3=Button(self.f,text='3',width=1,height=1,bg="yellow")
        self.yy3.place(x=self.valll,y=self.val222)
        
    def game3(self):
        self.yy4.destroy()
        self.yy4=Button(self.f,text='4',width=1,height=1,bg="yellow")
        self.yy4.place(x=self.vallll,y=self.val2222)
    
    def game4(self):
        self.bb1.destroy()
        self.bb1=Button(self.f,text='1',width=1,height=1,bg="blue")
        self.bb1.place(x=self.blue1,y=self.bluee1)
        self.ct=self.turn+1
        
    def game5(self):
        self.bb2.destroy()
        self.bb2=Button(self.f,text='2',width=1,height=1,bg="blue")
        self.bb2.place(x=self.blue11,y=self.bluee11)
       
    def game6(self):
        self.bb3.destroy()
        self.bb3=Button(self.f,text='3',width=1,height=1,bg="blue")
        self.bb3.place(x=self.blue111,y=self.bluee111)
       
    def game7(self):
        self.bb4.destroy()
        self.bb4=Button(self.f,text='4',width=1,height=1,bg="blue")
        self.bb4.place(x=self.blue1111,y=self.bluee1111)
             
    def dice(self):
        l=random.randint(1,6)
        if self.turn%2!=0:
         if l==6 or self.open1==1 or self.open2==1 or self.open3==1 or self.open4==1:
           print("Number is",l)
           print("press 1 to move 1st token")
           print("press 2 to move 2nd token")
           print("press 3 to move 3rd token")
           print("press 4 to move 4th token")
           ch=eval(input("enter your choice"))
           if ch==1:
            if l==6 and self.open1==0:
              self.open1=1
              self.val=325
              self.val2=630
              self.game()

            elif self.open1==1:    
               if self.val==325:
                  self.val2=self.val2-(l*40)      
                  if self.val2<470:
                      s=(470-self.val2)//40
                      self.val2=400
                      self.val=270
                      self.val=self.val-((s-1)*50)
                  self.game()

             
               elif self.val2==470 and self.val<=270:
                        self.val=270
                        self.val2=400
                        self.val=self.val-((l-1)*50)
                        self.game()
           


               elif self.val2<470 and self.val2!=280 and self.val<=270:
                      self.val=self.val-(l*50)
                      if self.val<20:
                          s=(20-self.val)//50
                          self.val2=self.val2-(s*60)
                          self.val=20
               
                          if self.val2<280 and self.val2!=280:
                             s=(280-self.val2)//60
                             self.val2=280
                             self.val=self.val+(s*50)
                    
                          elif self.val2==280:
                            self.val=20
                
                      self.game()
            
               elif self.val2==280 and self.val<=270:
                      self.val=self.val+(l*50)
                      if self.val>270:
                           s=(self.val-270)//50
                           self.val=324
                           self.val2=220
                           self.val2=self.val2-((s-1)*43)  
                      self.game()
            
               elif self.val==324 or self.val==384:
                     self.val2=self.val2-(l*43)
                     if self.val2<5:
                         s=(5-self.val2)//43
                         self.val2=5
                         self.val=self.val+(s*60)
                
                         if self.val>444:
                            s=(self.val-444)//60
                            self.val=444
                            self.val2=self.val2+(s*43)
                         elif self.val==444:
                            self.val2=5    
                     self.game()
        
               elif self.val==444:
                    self.val2=self.val2+(l*43)
                    if self.val2>220:
                         s=(self.val2-220)//43
                         self.val2=280
                         self.val=504
                         self.val=self.val+((s-1)*50)  
                    self.game()
            
               elif self.val2==280 and self.val>=504 or self.val2==340 and self.val>=504:
                      self.val=self.val+(l*50)
                      if self.val>754:
                          s=(self.val-754)//50
                          self.val=754
                          self.val2=self.val2+(s*60)
                          if self.val2>400:
                              s=(self.val2-400)//60
                              self.val2=400
                              self.val=self.val-(s*50)     
                      self.game()

               elif self.val2==400:
                     self.val=self.val-(l*50)
                     if self.val<504:
                        s=(504-self.val)//50
                        self.val=443
                        self.val2=470
                        self.val2=self.val2+((s-1)*40)
                     self.game()

            
               elif self.val==443:
                     self.val2=self.val2+(l*40)
    
                     if self.val2>670:
                            s=(self.val2-670)//40
                            self.val=self.val-(s*40)
                            self.val2=670
                      
                            if self.val<403 and self.val!=403:
                                      s=(403-self.val)//40
                                      self.val2=self.val2-((s-1)*40)
                                      self.val=403
                    
                     self.game()

               elif self.val==403 and self.val2<=670:
                        m=self.val2
                        self.val2=self.val2-(l*40)
                        if self.val2==430:
                            self.val2=530
                            self.val=5
                        elif self.val2<430:
                            self.val2=m
                        self.game()
        
        
           if ch==2:
            if l==6 and self.open2==0:
              self.open2=1
              self.vall=325
              self.val22=630
              self.game1()

            elif self.open2==1:
               if self.vall==325:
                  self.val22=self.val22-(l*40)
                  if self.val22<470:
                      s=(470-self.val22)//40
                      self.val22=400
                      self.vall=270
                      self.vall=self.vall-((s-1)*50)
                  self.game1()

             
               elif self.val22==470 and self.vall<=270:
                        self.vall=270
                        self.val22=400
                        self.vall=self.vall-((l-1)*50)
                        self.game1()
           


               elif self.val22<470 and self.val22!=280 and self.vall<=270:
                      self.vall=self.vall-(l*50)
                      if self.vall<20:
                          s=(20-self.vall)//50
                          self.val22=self.val22-(s*60)
                          self.vall=20
               
                          if self.val22<280 and self.val22!=280:
                             s=(280-self.val22)//60
                             self.val22=280
                             self.vall=self.vall+(s*50)
                    
                          elif self.val22==280:
                            self.vall=20
                
                      self.game1()
            
               elif self.val22==280 and self.vall<=270:
                      self.vall=self.vall+(l*50)
                      if self.vall>270:
                           s=(self.vall-270)//50
                           self.vall=324
                           self.val22=220
                           self.val22=self.val22-((s-1)*43)  
                      self.game1()
            
               elif self.vall==324 or self.vall==384:
                     self.val22=self.val22-(l*43)
                     if self.val22<5:
                         s=(5-self.val22)//43
                         self.val22=5
                         self.vall=self.vall+(s*60)
                
                         if self.vall>444:
                            s=(self.vall-444)//60
                            self.vall=444
                            self.val22=self.val22+(s*43)
                         elif self.vall==444:
                            self.val22=5    
                     self.game1()
        
               elif self.vall==444:
                    self.val22=self.val22+(l*43)
                    if self.val22>220:
                         s=(self.val22-220)//43
                         self.val22=280
                         self.vall=504
                         self.vall=self.vall+((s-1)*50)  
                    self.game1()
            
               elif self.val22==280 and self.vall>=504 or self.val22==340 and self.vall>=504:
                      self.vall=self.vall+(l*50)
                      if self.vall>754:
                          s=(self.vall-754)//50
                          self.vall=754
                          self.val22=self.val22+(s*60)
                          if self.val22>400:
                              s=(self.val22-400)//60
                              self.val22=400
                              self.vall=self.vall-(s*50)     
                      self.game1()

               elif self.val22==400:
                     self.vall=self.vall-(l*50)
                     if self.vall<504:
                        s=(504-self.vall)//50
                        self.vall=443
                        self.val22=470
                        self.val22=self.val22+((s-1)*40)
                     self.game1()

            
               elif self.vall==443:
                     self.val22=self.val22+(l*40)
    
                     if self.val22>670:
                            s=(self.val22-670)//40
                            self.vall=self.vall-(s*40)
                            self.val22=670
                      
                            if self.vall<403 and self.vall!=403:
                                      s=(403-self.vall)//40
                                      self.val22=self.val22-((s-1)*40)
                                      self.vall=403
                    
                     self.game1()

               elif self.vall==403 and self.val22<=670:
                        m=self.val22
                        self.val22=self.val22-(l*40)
                        if self.val22==430:
                            self.val22=570
                            self.vall=5
                        elif self.val22<430:
                            self.val22=m 
                        self.game1()    
        
        
         
           if ch==3:
            if l==6 and self.open3==0:
              self.open3=1
              self.valll=325
              self.val222=630
              self.game2()

            elif self.open3==1:    
               if self.valll==325:
                  self.val222=self.val222-(l*40)      
                  if self.val222<470:
                      s=(470-self.val222)//40
                      self.val222=400
                      self.valll=270
                      self.valll=self.valll-((s-1)*50)
                  self.game2()

             
               elif self.val222==470 and self.valll<=270:
                        self.valll=270
                        self.val222=400
                        self.valll=self.valll-((l-1)*50)
                        self.game2()
           


               elif self.val222<470 and self.val222!=280 and self.valll<=270:
                      self.valll=self.valll-(l*50)
                      if self.valll<20:
                          s=(20-self.valll)//50
                          self.val222=self.val222-(s*60)
                          self.valll=20
               
                          if self.val222<280 and self.val222!=280:
                             s=(280-self.val222)//60
                             self.val222=280
                             self.valll=self.valll+(s*50)
                    
                          elif self.val222==280:
                            self.valll=20
                
                      self.game2()
            
               elif self.val222==280 and self.valll<=270:
                      self.valll=self.valll+(l*50)
                      if self.valll>270:
                           s=(self.valll-270)//50
                           self.valll=324
                           self.val222=220
                           self.val222=self.val222-((s-1)*43)  
                      self.game2()
            
               elif self.valll==324 or self.valll==384:
                     self.val222=self.val222-(l*43)
                     if self.val222<5:
                         s=(5-self.val222)//43
                         self.val222=5
                         self.valll=self.valll+(s*60)
                
                         if self.valll>444:
                            s=(self.valll-444)//60
                            self.valll=444
                            self.val222=self.val222+(s*43)
                         elif self.valll==444:
                            self.val222=5    
                     self.game2()
        
               elif self.valll==444:
                    self.val222=self.val222+(l*43)
                    if self.val222>220:
                         s=(self.val222-220)//43
                         self.val222=280
                         self.valll=504
                         self.valll=self.valll+((s-1)*50)  
                    self.game2()
            
               elif self.val222==280 and self.valll>=504 or self.val222==340 and self.valll>=504:
                      self.valll=self.valll+(l*50)
                      if self.valll>754:
                          s=(self.valll-754)//50
                          self.valll=754
                          self.val222=self.val222+(s*60)
                          if self.val222>400:
                              s=(self.val222-400)//60
                              self.val222=400
                              self.valll=self.valll-(s*50)     
                      self.game2()

               elif self.val222==400:
                     self.valll=self.valll-(l*50)
                     if self.valll<504:
                        s=(504-self.valll)//50
                        self.valll=443
                        self.val222=470
                        self.val222=self.val222+((s-1)*40)
                     self.game2()

            
               elif self.valll==443:
                     self.val222=self.val222+(l*40)
    
                     if self.val222>670:
                            s=(self.val222-670)//40
                            self.valll=self.valll-(s*40)
                            self.val222=670
                      
                            if self.valll<403 and self.valll!=403:
                                      s=(403-self.valll)//40
                                      self.val222=self.val222-((s-1)*40)
                                      self.valll=403
                    
                     self.game2()

               elif self.valll==403 and self.val222<=670:
                        m=self.val222
                        self.val222=self.val222-(l*40)
                        if self.val222==430:
                            self.val222=610
                            self.valll=5
                        elif self.val222<430:
                            self.val222=m
                        self.game2()
           if ch==4:
            if l==6 and self.open4==0:
              self.open4=1
              self.vallll=325
              self.val2222=630
              self.game3()

            elif self.open4==1:    
               if self.vallll==325:
                  self.val2222=self.val2222-(l*40)      
                  if self.val2222<470:
                      s=(470-self.val2222)//40
                      self.val2222=400
                      self.vallll=270
                      self.vallll=self.vallll-((s-1)*50)
                  self.game3()

             
               elif self.val2222==470 and self.vallll<=270:
                        self.vallll=270
                        self.val2222=400
                        self.vallll=self.vallll-((l-1)*50)
                        self.game3()
           


               elif self.val2222<470 and self.val2222!=280 and self.vallll<=270:
                      self.vallll=self.vallll-(l*50)
                      if self.vallll<20:
                          s=(20-self.vallll)//50
                          self.val2222=self.val2222-(s*60)
                          self.vallll=20
               
                          if self.val2222<280 and self.val2222!=280:
                             s=(280-self.val2222)//60
                             self.val2222=280
                             self.vallll=self.vallll+(s*50)
                    
                          elif self.val2222==280:
                            self.vallll=20
                
                      self.game3()
            
               elif self.val2222==280 and self.vallll<=270:
                      self.vallll=self.vallll+(l*50)
                      if self.vallll>270:
                           s=(self.vallll-270)//50
                           self.vallll=324
                           self.val2222=220
                           self.val2222=self.val2222-((s-1)*43)  
                      self.game3()
            
               elif self.vallll==324 or self.vallll==384:
                     self.val2222=self.val2222-(l*43)
                     if self.val2222<5:
                         s=(5-self.val2222)//43
                         self.val2222=5
                         self.vallll=self.vallll+(s*60)
                
                         if self.vallll>444:
                            s=(self.vallll-444)//60
                            self.vallll=444
                            self.val2222=self.val2222+(s*43)
                         elif self.vallll==444:
                            self.val2222=5    
                     self.game3()
        
               elif self.vallll==444:
                    self.val2222=self.val2222+(l*43)
                    if self.val2222>220:
                         s=(self.val2222-220)//43
                         self.val2222=280
                         self.vallll=504
                         self.vallll=self.vallll+((s-1)*50)  
                    self.game3()
            
               elif self.val2222==280 and self.vallll>=504 or self.val2222==340 and self.vallll>=504:
                      self.vallll=self.vallll+(l*50)
                      if self.vallll>754:
                          s=(self.vallll-754)//50
                          self.vallll=754
                          self.val2222=self.val2222+(s*60)
                          if self.val2222>400:
                              s=(self.val2222-400)//60
                              self.val2222=400
                              self.vallll=self.vallll-(s*50)     
                      self.game3()

               elif self.val2222==400:
                     self.vallll=self.vallll-(l*50)
                     if self.vallll<504:
                        s=(504-self.vallll)//50
                        self.vallll=443
                        self.val2222=470
                        self.val2222=self.val2222+((s-1)*40)
                     self.game3()

            
               elif self.vallll==443:
                     self.val2222=self.val2222+(l*40)
    
                     if self.val2222>670:
                            s=(self.val2222-670)//40
                            self.vallll=self.vallll-(s*40)
                            self.val2222=670
                      
                            if self.vallll<403 and self.vallll!=403:
                                      s=(403-self.vallll)//40
                                      self.val2222=self.val2222-((s-1)*40)
                                      self.vallll=403
                    
                     self.game3()

               elif self.vallll==403 and self.val2222<=670:
                        m=self.val2222
                        self.val2222=self.val2222-(l*40)
                        if self.val2222==430:
                            self.val2222=650
                            self.vallll=5
                        elif self.val2222<430:
                            self.val2222=m  
                        self.game3()
         else:
              print("None of the token is open and number is also not 6..try again!!!")
         self.turn=self.turn+1
         print("2nd player turn..Roll the dice")
        else:
          if l==6 or self.openn1==1 or self.openn2==1 or self.openn3==1 or self.openn4==1:
            print("Number is",l)
            print("press 1 to move 1st token")
            print("press 2 to move 2nd token")
            print("press 3 to move 3rd token")
            print("press 4 to move 4th token")
            ch=eval(input("enter your choice"))
            if ch==1:
                if l==6 and self.openn1==0:
                      self.openn1=1
                      self.blue1=444
                      self.bluee1=48
                      self.game4()
                elif self.openn1==1:
                    if self.blue1==444:
                        self.bluee1=self.bluee1+(l*43)
                        if self.bluee1>220 and self.bluee1!=220:
                            s=(self.bluee1-220)//43
                            self.blue1=504
                            self.bluee1=280
                            self.blue1=self.blue1+((s-1)*50)
                        self.game4()

                    
                    elif self.bluee1==280 and self.blue1>=504 or self.bluee1==340 and self.blue1>=504:
                        self.blue1=self.blue1+(l*50)
                        if self.blue1>754:
                             s=(self.blue1-754)//50
                             self.blue1=754
                             self.bluee1=self.bluee1+(s*60)
                             if self.bluee1>400:
                                 s=(self.bluee1-400)//60
                                 self.bluee1=400
                                 self.blue1=self.blue1-(s*50)     
                        self.game4()

                    elif self.bluee1==400 and self.blue1>=504:
                          self.blue1=self.blue1-(l*50)
                          if self.blue1<504:
                               s=(504-self.blue1)//50
                               self.blue1=443
                               self.bluee1=470
                               self.bluee1=self.bluee1+((s-1)*40)
                          self.game4()

                    elif self.blue1==443 :
                       self.bluee1=self.bluee1+(l*40)
                      
                       if self.bluee1>670:
                            s=(self.bluee1-670)//40
                            self.blue1=self.blue1-(s*60)
                            self.bluee1=670

                      
                            if self.blue1<323 and self.bluee1==670:
                                      s=(363-self.blue1)//40
                                      self.blue1=323
                                      self.bluee1=670
                                      self.bluee1=self.bluee1-(s-1)*40
                            
                       self.game4()

                    elif self.blue1==383:
                        self.blue1=self.blue1-(l*60)
                        if self.blue1<323:
                            s=(323-self.blue1)//60
                            self.blue1=323
                            self.bluee1=self.bluee1-(s*40)
                                                     
                        self.game4()
                            

                    elif self.blue1==323 and self.bluee1>=470:
                        self.bluee1=self.bluee1-(l*40)
                        if self.bluee1<470:
                             s=(470-self.bluee1)//40
                             self.bluee1=400
                             self.blue1=270
                             self.blue1=self.blue1-((s-1)*50)
                          
                        self.game4()

                    elif self.bluee1<470 and self.bluee1!=280 and self.blue1<=270:
                      self.blue1=self.blue1-(l*50)
                      if self.blue1<20:
                          s=(20-self.blue1)//50
                          self.bluee1=self.bluee1-(s*60)
                          self.blue1=20
               
                          if self.bluee1<280 and self.bluee1!=280:
                             s=(280-self.bluee1)//60
                             self.bluee1=280
                             self.blue1=self.blue1+(s*50)
                    
                          elif self.bluee1==280:
                            self.blue1=20
                      self.game4()


                    elif self.bluee1==280 and self.blue1<=270:
                      self.blue1=self.blue1+(l*50)
                      
                      if self.blue1>270:
                           s=(self.blue1-270)//50
                           self.blue1=324
                           self.bluee1=220
                           self.bluee1=self.bluee1-((s-1)*40)
                      self.game4()

                    elif self.blue1==324:
                        self.bluee1=self.bluee1-(l*43)
                        if self.bluee1<5:
                            s=(5-self.bluee1)//43
                            self.blue1=384
                            self.bluee1=5
                            self.bluee1=self.bluee1+((s-1)*43)
                        self.game4()

                    elif self.blue1==384:
                        m=self.bluee1
                        self.bluee1=self.bluee1+(l*43)
                        if self.bluee1==263:
                            self.bluee1=5
                            self.blue1=780
                        elif self.bluee1>263:
                            self.bluee1=m
                        self.game4()

                    

            if ch==2:
                if l==6 and self.openn2==0:
                      self.openn2=1
                      self.blue11=444
                      self.bluee11=48
                      self.game5()
                elif self.openn2==1:
                    if self.blue11==444:
                        self.bluee11=self.bluee11+(l*43)
                        if self.bluee11>220 and self.bluee11!=220:
                            s=(self.bluee11-220)//43
                            self.blue11=504
                            self.bluee11=280
                            self.blue11=self.blue11+((s-1)*50)
                        self.game5()

                    
                    elif self.bluee11==280 and self.blue11>=504 or self.bluee11==340 and self.blue11>=504:
                        self.blue11=self.blue11+(l*50)
                        if self.blue11>754:
                             s=(self.blue11-754)//50
                             self.blue11=754
                             self.bluee11=self.bluee11+(s*60)
                             if self.bluee11>400:
                                 s=(self.bluee11-400)//60
                                 self.bluee11=400
                                 self.blue11=self.blue11-(s*50)     
                        self.game5()

                    elif self.bluee11==400 and self.blue11>=504:
                          self.blue11=self.blue11-(l*50)
                          if self.blue11<504:
                               s=(504-self.blue11)//50
                               self.blue11=443
                               self.bluee11=470
                               self.bluee11=self.bluee11+((s-1)*40)
                          self.game5()

                    elif self.blue11==443:
                       self.bluee11=self.bluee11+(l*40)
                      
                       if self.bluee11>670:
                            s=(self.bluee11-670)//40
                            self.blue11=self.blue11-(s*60)
                            self.bluee11=670

                      
                            if self.blue11<323 and self.bluee11==670 and self.bluee11!=383:
                                      s=(363-self.blue11)//40
                                      self.blue11=323
                                      self.bluee11=670
                                      self.bluee11=self.bluee11-(s-1)*40
                            
                       self.game5()
                       
                    elif self.blue11==383:
                        self.blue11=self.blue11-(l*60)
                        if self.blue11<323:
                            s=(323-self.blue11)//60
                            self.blue11=323
                            self.bluee11=self.bluee11-(s*40)
                                                     
                        self.game5() 

                    elif self.blue11==323 and self.bluee11>=470:
                        self.bluee11=self.bluee11-(l*40)
                        if self.bluee11<470:
                             s=(470-self.bluee11)//40
                             self.bluee11=400
                             self.blue11=270
                             self.blue11=self.blue11-((s-1)*50)
                          
                        self.game5()

                    elif self.bluee11<470 and self.bluee11!=280 and self.blue11<=270:
                      self.blue11=self.blue11-(l*50)
                      if self.blue11<20:
                          s=(20-self.blue11)//50
                          self.bluee11=self.bluee11-(s*60)
                          self.blue11=20
               
                          if self.bluee11<280 and self.bluee11!=280:
                             s=(280-self.bluee11)//60
                             self.bluee11=280
                             self.blue11=self.blue11+(s*50)
                    
                          elif self.bluee11==280:
                            self.blue11=20
                      self.game5()


                    elif self.bluee11==280 and self.blue11<=270:
                      self.blue11=self.blue11+(l*50)
                      
                      if self.blue11>270:
                           s=(self.blue11-270)//50
                           self.blue11=324
                           self.bluee11=220
                           self.bluee11=self.bluee11-((s-1)*40)
                      self.game5()

                    elif self.blue11==324:
                        self.bluee11=self.bluee11-(l*43)
                        if self.bluee11<5:
                            s=(5-self.bluee11)//43
                            self.blue11=384
                            self.bluee11=5
                            self.bluee11=self.bluee11+((s-1)*43)
                        self.game5()

                    elif self.blue11==384:
                        m=self.bluee11
                        self.bluee11=self.bluee11+(l*43)
                        if self.bluee11==263:
                            self.bluee11=48
                            self.blue11=780
                        elif self.bluee11>263:
                            self.bluee1=m
                        self.game5()        

            if ch==3:
                if l==6 and self.openn3==0:
                      self.openn3=1
                      self.blue111=444
                      self.bluee111=48
                      self.game6()
                elif self.openn3==1:
                    if self.blue111==444:
                        self.bluee111=self.bluee111+(l*43)
                        if self.bluee111>220 and self.bluee111!=220:
                            s=(self.bluee111-220)//43
                            self.blue111=504
                            self.bluee111=280
                            self.blue111=self.blue111+((s-1)*50)
                        self.game6()

                    
                    elif self.bluee111==280 and self.blue111>=504 or self.bluee111==340 and self.blue111>=504:
                        self.blue111=self.blue111+(l*50)
                        if self.blue111>754:
                             s=(self.blue111-754)//50
                             self.blue111=754
                             self.bluee111=self.bluee111+(s*60)
                             if self.bluee111>400:
                                 s=(self.bluee111-400)//60
                                 self.bluee111=400
                                 self.blue111=self.blue111-(s*50)     
                        self.game6()

                    elif self.bluee111==400 and self.blue111>=504:
                          self.blue111=self.blue111-(l*50)
                          if self.blue111<504:
                               s=(504-self.blue111)//50
                               self.blue111=443
                               self.bluee111=470
                               self.bluee111=self.bluee111+((s-1)*40)
                          self.game6()

                    elif self.blue111==443:
                       self.bluee111=self.bluee111+(l*40)
                      
                       if self.bluee111>670:
                            s=(self.bluee111-670)//40
                            self.blue111=self.blue111-(s*60)
                            self.bluee111=670

                      
                            if self.blue111<323 and self.bluee111==670 and self.bluee111!=383:
                                      s=(363-self.blue111)//40
                                      self.blue111=323
                                      self.bluee111=670
                                      self.bluee111=self.bluee111-(s-1)*40
                            
                       self.game6()

                    elif self.blue111==383:
                        self.blue111=self.blue111-(l*60)
                        if self.blue111<323:
                            s=(323-self.blue111)//60
                            self.blue111=323
                            self.bluee111=self.bluee111-(s*40)
                                                     
                        self.game6()

                    elif self.blue111==323 and self.bluee111>=470:
                        self.bluee111=self.bluee111-(l*40)
                        if self.bluee111<470:
                             s=(470-self.bluee111)//40
                             self.bluee111=400
                             self.blue111=270
                             self.blue111=self.blue111-((s-1)*50)
                          
                        self.game6()

                    elif self.bluee111<470 and self.bluee111!=280 and self.blue111<=270:
                      self.blue111=self.blue111-(l*50)
                      if self.blue111<20:
                          s=(20-self.blue111)//50
                          self.bluee111=self.bluee111-(s*60)
                          self.blue111=20
               
                          if self.bluee111<280 and self.bluee111!=280:
                             s=(280-self.bluee111)//60
                             self.bluee111=280
                             self.blue111=self.blue111+(s*50)
                    
                          elif self.bluee111==280:
                            self.blue111=20
                      self.game6()


                    elif self.bluee111==280 and self.blue111<=270:
                      self.blue111=self.blue111+(l*50)
                      
                      if self.blue111>270:
                           s=(self.blue111-270)//50
                           self.blue111=324
                           self.bluee111=220
                           self.bluee111=self.bluee111-((s-1)*40)
                      self.game6()

                    elif self.blue111==324:
                        self.bluee111=self.bluee111-(l*43)
                        if self.bluee111<5:
                            s=(5-self.bluee111)//43
                            self.blue111=384
                            self.bluee111=5
                            self.bluee111=self.bluee111+((s-1)*43)
                        self.game6()

                    elif self.blue111==384:
                        m=self.bluee111
                        self.bluee111=self.bluee111+(l*43)
                        if self.bluee111==263:
                            self.bluee111=91
                            self.blue111=780
                        elif self.bluee111>263:
                            self.bluee111=m
                        self.game6()


            if ch==4:
                if l==6 and self.openn4==0:
                      self.openn4=1
                      self.blue1111=444
                      self.bluee1111=48
                      self.game7()
                elif self.openn4==1:
                    if self.blue1111==444:
                        self.bluee1111=self.bluee1111+(l*43)
                        if self.bluee1111>220 and self.bluee1111!=220:
                            s=(self.bluee1111-220)//43
                            self.blue1111=504
                            self.bluee1111=280
                            self.blue1111=self.blue1111+((s-1)*50)
                        self.game7()

                    
                    elif self.bluee1111==280 and self.blue1111>=504 or self.bluee1111==340 and self.blue1111>=504:
                        self.blue1111=self.blue1111+(l*50)
                        if self.blue1111>754:
                             s=(self.blue1111-754)//50
                             self.blue1111=754
                             self.bluee1111=self.bluee1111+(s*60)
                             if self.bluee1111>400:
                                 s=(self.bluee1111-400)//60
                                 self.bluee1111=400
                                 self.blue1111=self.blue1111-(s*50)     
                        self.game7()

                    elif self.bluee1111==400 and self.blue1111>=504:
                          self.blue1111=self.blue1111-(l*50)
                          if self.blue1111<504:
                               s=(504-self.blue1111)//50
                               self.blue1111=443
                               self.bluee1111=470
                               self.bluee1111=self.bluee1111+((s-1)*40)
                          self.game7()

                    elif self.blue1111==443 :
                       self.bluee1111=self.bluee1111+(l*40)
                      
                       if self.bluee1111>670:
                            s=(self.bluee1111-670)//40
                            self.blue1111=self.blue1111-(s*60)
                            self.bluee1111=670

                      
                            if self.blue1111<323 and self.bluee1111==670 and self.bluee1111!=383:
                                      s=(363-self.blue1111)//40
                                      self.blue1111=323
                                      self.bluee1111=670
                                      self.bluee1111=self.bluee1111-(s-1)*40
                            
                       self.game7()

                    elif self.blue1111==383:
                        self.blue1111=self.blue1111-(l*60)
                        if self.blue1111<323:
                            s=(323-self.blue1111)//60
                            self.blue1111=323
                            self.bluee1111=self.bluee1111-(s*40)
                                                     
                        self.game7()

                    elif self.blue1111==323 and self.bluee1111>=470:
                        self.bluee1111=self.bluee1111-(l*40)
                        if self.bluee1111<470:
                             s=(470-self.bluee1111)//40
                             self.bluee1111=400
                             self.blue1111=270
                             self.blue1111=self.blue1111-((s-1)*50)
                          
                        self.game7()

                    elif self.bluee1111<470 and self.bluee1111!=280 and self.blue1111<=270:
                      self.blue1111=self.blue1111-(l*50)
                      if self.blue1111<20:
                          s=(20-self.blue1111)//50
                          self.bluee1111=self.bluee1111-(s*60)
                          self.blue1111=20
               
                          if self.bluee1111<280 and self.bluee1111!=280:
                             s=(280-self.bluee1111)//60
                             self.bluee1111=280
                             self.blue1111=self.blue1111+(s*50)
                    
                          elif self.bluee1111==280:
                            self.blue1111=20
                      self.game7()


                    elif self.bluee1111==280 and self.blue1111<=270:
                      self.blue1111=self.blue1111+(l*50)
                      
                      if self.blue1111>270:
                           s=(self.blue1111-270)//50
                           self.blue1111=324
                           self.bluee1111=220
                           self.bluee1111=self.bluee1111-((s-1)*40)
                      self.game7()

                    elif self.blue1111==324:
                        self.bluee1111=self.bluee1111-(l*43)
                        if self.bluee1111<5:
                            s=(5-self.bluee1111)//43
                            self.blue1111=384
                            self.bluee1111=5
                            self.bluee1111=self.bluee1111+((s-1)*43)
                        self.game7()

                    elif self.blue1111==384:
                        m=self.bluee1111
                        self.bluee1111=self.bluee1111+(l*43)
                        if self.bluee1111==263:
                            self.bluee1111=134
                            self.blue1111=780
                        elif self.bluee1111>263:
                            self.bluee1111=m
                        self.game7()      
          else:
              print("None of the token is open and the number is also not 6 ..try again!!!") 
          self.turn=self.turn+1
          print("1st player turn..Roll the dice")
        if self.blue1==self.val and self.bluee1==self.val2:
              if (self.turn-1)%2==0:
                      self.val=80
                      self.val2=610
                      self.game()
              else:
                  self.blue1=580
                  self.bluee1=70
                  self.game4()
        elif self.blue1==self.vall and self.bluee1==self.val22:
              if self.turn%2==0:
                      self.vall=190
                      self.val22=610
                      self.game1()
              else:
                  self.blue1=580
                  self.bluee1=70
                  self.game4()
        elif self.blue1==self.valll and self.bluee1==self.val222:
              if (self.turn%2-1)==0:
                      self.valll=80
                      self.val222=510
                      self.game2()
              else:
                  self.blue1=580
                  self.bluee1=70
                  self.game4()
        elif self.blue1==self.vallll and self.bluee1==self.val2222:
              if (self.turn%2-1)==0:
                      self.vallll=190
                      self.val2222=510
                      self.game3()
              else:
                  self.blue1=580
                  self.bluee1=70
                  self.game4()
        elif self.blue11==self.val and self.bluee11==self.val2:
              if (self.turn-1)%2==0:
                      self.val=80
                      self.val2=610
                      self.game()
              else:
                  self.blue11=690
                  self.bluee11=70
                  self.game5()
        elif self.blue11==self.vall and self.bluee11==self.val22:
              if (self.turn%2-1)==0:
                      self.vall=190
                      self.val22=610
                      self.game1()
              else:
                  self.blue11=690
                  self.bluee11=70
                  self.game5()
        elif self.blue11==self.valll and self.bluee11==self.val222:
              if (self.turn%2-1)==0:
                      self.valll=80
                      self.val222=510
                      self.game2()
              else:
                  self.blue11=690
                  self.bluee11=70
                  self.game5()
        elif self.blue11==self.vallll and self.bluee11==self.val2222:
              if (self.turn%2-1)==0:
                      self.vallll=190
                      self.val2222=510
                      self.game3()
              else:
                  self.blue11=580
                  self.bluee11=70
                  self.game5()
        elif self.blue111==self.val and self.bluee111==self.val2:
              if (self.turn-1)%2==0:
                      self.val=80
                      self.val2=610
                      self.game()
              else:
                  self.blue111=690
                  self.bluee111=70
                  self.game6()
        elif self.blue111==self.vall and self.bluee111==self.val22:
              if (self.turn%2-1)==0:
                      self.vall=190
                      self.val22=610
                      self.game1()
              else:
                  self.blue111=580
                  self.bluee111=150
                  self.game6()
        elif self.blue111==self.valll and self.bluee111==self.val222:
              if (self.turn%2-1)==0:
                      self.valll=80
                      self.val222=510
                      self.game2()
              else:
                  self.blue111=580
                  self.bluee111=150
                  self.game6()
        elif self.blue1111==self.vallll and self.bluee1111==self.val2222:
              if (self.turn%2-1)==0:
                      self.vallll=190
                      self.val2222=510
                      self.game3()
              else:
                  self.blue1111=580
                  self.bluee1111=150
                  self.game7()
        elif self.blue1111==self.val and self.bluee1111==self.val2:
              if (self.turn-1)%2==0:
                      self.val=80
                      self.val2=610
                      self.game()
              else:
                  self.blue1111=580
                  self.bluee1111=150
                  self.game7()
        elif self.blue1111==self.vall and self.bluee1111==self.val22:
              if (self.turn%2-1)==0:
                      self.vall=190
                      self.val22=610
                      self.game1()
              else:
                  self.blue1111=690
                  self.bluee1111=150
                  self.game7()
        elif self.blue1111==self.valll and self.bluee1111==self.val222:
              if (self.turn%2-1)==0:
                      self.valll=80
                      self.val222=510
                      self.game2()
              else:
                  self.blue1111=690
                  self.bluee1111=150
                  self.game7()
        elif self.blue1111==self.vallll and self.bluee1111==self.val2222:
              if (self.turn%2-1)==0:
                      self.vallll=190
                      self.val2222=510
                      self.game3()
              else:
                  self.blue1111=690
                  self.bluee1111=150
                  self.game7()
        
          
         
        
f=Frame(rr,height=800,width=800,bg="#C70039")
class homepage:
    def __init__(self,rr,f):
       
        self.t=Text(f,width=36,height=10,font=('Verdana',14,'bold'),fg="blue",bg="#C70039",wrap=WORD)
        self.img=ImageTk.PhotoImage(Image.open("l.jpeg"))
        self.t.image_create(END,image=self.img)
        self.l=Label(f,text="Ludo Master",height=1,width=10,bg="#C70039",font=("Chiller",70,"bold","underline"),fg="yellow")
        self.l.place(x=220,y=80)
        self.l1=Label(f,text="Welcome to ludo Master",height=1,width=21,bg="#C70039",font=("Lucida handwriting",20),fg="yellow")
        self.l1.place(x=0,y=0)
        self.b=Button(f,text="Play",height=2,width=20,font=("ariel",),borderwidth=7,relief=RAISED,command=self.playy)
        self.b.place(x=435,y=450)
        self.b1=Button(f,text="Signup",height=2,width=20,font=("ariel"),borderwidth=7,relief=RAISED,command=self.signupp)
        self.b1.place(x=185,y=450)
        self.b2=Button(f,text="Rules",height=2,width=5,font=("ariel",),bg="yellow",command=self.rules)
        self.b2.place(x=720,y=10)
        self.t.place(x=150,y=200)
       
        f.propagate(0)
        f.pack()  
    def playy(self):
              r=Tk()
              r.title("Ludo")
              l=ludo(r)
              r.mainloop()
    def signupp(self):
          rrr=Tk()
          rrr.title("Signup Page")
          s=signup(rrr)
          rrr.mainloop()
    def rules(self):
        rrrr=Tk()
        ruless=rule(rrrr)
        rrrr.mainloop()
        
        
class signup:
     def __init__(self,rrr):
          self.f1=Frame(rrr,width=800,height=800,bg="#C70039")
          self.f1.pack()
          self.l5=Label(self.f1,text="Signup",height=1,width=10,bg="#C70039",font=("Bell MT",30,"bold","underline"))
          self.l5.place(x=260,y=100)
          self.l=Label(self.f1,text="Username",height=1,width=10,bg="yellow",font=("Bell MT",20,"bold","underline"))
          self.l.place(x=150,y=200)
          self.l1=Label(self.f1,text="Phone no",height=1,width=10,bg="yellow",font=("Bell MT",20,"bold","underline"))
          self.l1.place(x=150,y=300)
          self.e=Entry(self.f1,width=25,bg="white")
          self.e1=Entry(self.f1,width=25,bg="white")
          self.e.place(x=400,y=210)
          self.e1.place(x=400,y=310)
          self.l2=Label(self.f1,text="Gender",height=1,width=10,bg="yellow",font=("Bell MT",20,"bold","underline"))
          self.l2.place(x=150,y=400)
          self.v1=StringVar()
          self.s1=Spinbox(self.f1,width=25,values=("Male","Female"),textvariable=self.v1)
          self.s1.place(x=400,y=405)
          self.j=Button(self.f1,text="Submit",height=2,width=10,command=self.display,font=("Ariel",15))
          self.j.place(x=320,y=455)
          self.f1.propagate(0)
          
          
          
     def display(self):
         
          self.l4=Label(self.f1,text="Signup successfully Go back to homepage",height=1,width=35,bg="light blue",font=("Bell MT",20,"bold","underline"))
          self.l4.place(x=100,y=530)
          mm=self.e.get()
          self.l6=Label(f,text="Hello "+mm,height=1,width=32,bg="#C70039",font=("Lucida handwriting",20),fg="yellow")
          self.l6.place(x=-130,y=0)
class rule:
    def __init__(self,rrrr):
        self.fr=Frame(rrrr,height=800,width=800,bg="#C70039")
        self.fr.propagate(0)
        self.fr.pack()
        self.la2=Label(self.fr,text="Rules",font=("times new roman ", 45,"underline"),bg="#C70039")
        self.la2.place(x=320,y=80)
        self.m=Message(self.fr,text="->"+"A Ludo board is is square with a pattern on it in the shape of a cross, each arm being divided into three adjacent columns of eight squares. The middle squares form the home column for each colour and cannot be landed upon by other colours. The middle of the cross forms a large square which is the 'home' area and which is divided into 4 home triangles, one of each colour. At each corner, separate to the main circuit are coloured circles (or squares) where the pieces are placed to begin.",
                       width=780,font=("Times new roman",12),bg="#C70039",fg="yellow")                         
        self.m.place(x=0,y=200)
        self.la=Label(self.fr,text="Play:",font=("times new roman",25,"bold","underline"),bg="#C70039")
        self.m1=Message(self.fr,text="->"+"Players take turns in a clockwise order; highest throw of the die starts.Each throw, the player decides which piece to move. A piece simply moves in a clockwise direction around the track given by the number thrown. If no piece can legally move according to the number thrown, play passes to the next player.A throw of 6 gives another turn.A player must throw a 6 to move a piece from the starting circle onto the first square on the track. The piece moves 6 squares around the circuit beginning with the appropriately coloured start square (and the player then has another turn).If a piece lands on a piece of a different colour, the piece jumped upon is returned to its starting circle.If a piece lands upon a piece of the same colour, this forms a block. This block cannot be passed or landed on by any opposing piece.",
                       width=780,font=("Times new roman",12),bg="#C70039",fg="yellow")                         
        self.m1.place(x=0,y=350)
        self.la1=Label(self.fr,text="Winnings:",font=("times new roman",25,"bold","underline"),bg="#C70039")
        self.m2=Message(self.fr,text="->"+"When a piece has circumnavigated the board, it proceeds up the home column. A piece can only be moved onto the home triangle by an exact throw.The first person to move all 4 pieces into the home triangle wins.",
                        width=780,font=("times new roman",12),bg="#C70039",fg="yellow")
        self.m2.place(x=0,y=550)
        self.la.place(x=10,y=300)
        self.la1.place(x=10,y=500)
rr.title("Homepage")
h=homepage(rr,f)
rr.mainloop()
        
        
        
        
        
