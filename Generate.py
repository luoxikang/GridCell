import numpy as np
import random 
import math

class Dataset():
    def __init__(self,NumTrain,NumTest):
        # About DataNUm
        self.NumTrain = NumTest
        self.NumTest = NumTest
        
        # About Time 
        self.Step = 100
        self.TimeStep = 0.1
       
        # About Single Data Size
        self.SizeIn = 2
        self.SizeOut = 2
        
        # About DataMatirx Size
        # If you want to get the datamatrix in the time t0, you can use like:
        # self.TrainIn[t0/self.TimeStep+1,:,:]
        self.TrainIn = np.zeros((self.Step,self.SizeIn,self.NumTrain))
        self.TrainOut = np.zeros((self.Step,self.SizeOut,self.NumTrain))
        self.TestIn = np.zeros((self.Step,self.SizeIn,self.NumTest))
        self.TestOut = np.zeros((self.Step,self.SizeOut,self.NumTest))

    def Gene(self,Bound,BoundSize = 10):
        # Generite the step by chance and check if the point are in the bound
        self.BoundSize = BoundSize
        self.Bound = Bound
        
        for i in range(NumTrain):
            for timei in range(Step):
                self.TrainIn[timei,0,i] = random.uniform(0,1)
                self.TrainIn[timei,1,i] = random.uniform(0,2*math.pi)

                # Do the Bound judge
                self.TrainOut[timei,0,i] = 


    def Return(Data,Minibitch):
        
        
        if Data == 'Train' 

class RNN():
    def __init__(self,N,dt=0.1):
        # Do Initialaziiton
        self.N = N
        self.W_Rec = 
        self.W_In = 
        self.W_Out =
        self.dt =  dt
        self.Recoder = 
    
    def Update(self):
        # Caculate the Update and dt+,The translate the information to Recoder


    def Casulate 
    

class RNNRun():
    def __init__(self,RNN,dt = 0.1):
        self.RNN = RNN
        self.dt = dt
        self.t = 0
    
    
    def GetIn(self,Data):
        # remeber to initial the recoder
        self.In = In
        self.
    
    def Caculate(self):
        # Caculate the result and others

    def UpdateRNN(self):

    