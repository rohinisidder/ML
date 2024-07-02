import pandas as pd
data = pd.read_csv('sports.csv',header=None)
concepts = data.iloc[:,:-1].values
target = data.iloc[:,-1].values
n = len(concepts[0])
s = ['0']*n
g = ['?']*n
print("initialization os specific and general hypothesis:")
print("S0",s,"\nG0",g)
def learn(concepts,target):
    s = concepts[0].copy()
    g = [['?' for _ in range(len(s))]for _ in range(len(s))]
    for i,h in enumerate(concepts):
        if target[i]=='Yes':
            print("positive example",concepts[i])
            for x in range(len(s)):
                if h[x]!=s[x]:
                    s[x] = '?'
                    g[x][x] = '?'
        else:
            print("negative example",concepts[i])
            for x in range(len(s)):
                if h[x]!=s[x]:
                    g[x][x] = s[x]
                else:
                    g[x][x] = '?'
        print(s)
        print(g)
    g = [h for h in g if h!=['?' for _ in range(len(s))]]
    return s,g

s_final , g_final = learn(concepts,target)
print(s_final)
print("\nThe Final General Hypothesis:")
print(g_final)