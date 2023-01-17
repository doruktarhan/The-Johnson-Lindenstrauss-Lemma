import numpy as np
import math

mean = 0
var = 1
n = 10




#returns a vector of gaussian
def gaussian_vector(mean,var,dim):
    return np.random.normal(mean, var, dim)



def create_dataset(dim, numpoints, mean, var):
    """
	This function creates numpoints vector created with create_vector.
	"""
    listvec = []
    [listvec.append(gaussian_vector(mean,var,dim)) for i in range(numpoints)]
    return listvec



for m in (10,100,1000):
    for k in (5,10,50,100):
        for e in (0.01,0.1):
            
             if m > k:   
    
                X = np.array(create_dataset(m,n,0,1)).T
                J_list = []
                v_list = []
                N = 0
                for a in range(10):
                    J = np.random.multivariate_normal(np.zeros(k),np.eye(k)/k,m).T
                    J_list.append(J)
                
                #for specific m,n,e,k check projection
                
                Sl = 0
                for j_index in range(10):
                    J = J_list[j_index]
                    for i in range (X.shape[1]):
                        for j in range (i,X.shape[1]):
                            if i != j:
                                x1 = X[:,i].reshape(X.shape[0],-1)
                                x2 = X[:,j].reshape(X.shape[0],-1)
                                distance = np.linalg.norm(J@x1 - J@x2)
                                distance_lower = np.linalg.norm(x1-x2)*(1-e)
                                distance_upper = np.linalg.norm(x1-x2)*(1+e)
                                if distance < distance_upper and distance > distance_lower:
                                    Sl += 1
                                N = N + 1
                    v = Sl / N
                    v_list.append(v)
                    
                print("The used parameters for this run are as follows: ")
                print("n: ",n)
                print("m: ",m)
                print("k: ",k)
                print("e: ",e)
                print("Mean of 10 random runs: ",np.mean(v_list)) 
                print()
                print()
    