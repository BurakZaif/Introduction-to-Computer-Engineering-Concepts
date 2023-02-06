def linear(X,weights):
    output = []
    for i in weights:
        b = 0
        a = 0
        toplam = 0
        while a<len(i):
            out = (X[b])*(i[a])
            a += 1
            b += 1
            toplam += out
        output.append(toplam)
    return output

def relu(X):
    output = []
    for i in X:
        if i <= 0:
            i = 0
            output.append(i)
        elif i > 0:
            output.append(i)
    return output

def sigmoid(X):
    output = []
    import math
    for i in X:
        if i <= -700:
            i = 0
            output.append(i)
        elif -700 < i < 700:
            i = 1/(1+math.exp(-i))
            output.append(i)
        else:
            i = 1
            output.append(i)
    return output

def forward_pass(Network,X):
    for layer in Network:
        if "linear" in layer[0]:
            X = linear(X,layer[1])
        elif "relu" in layer:
            X = relu(X)
        elif "sigmoid" in layer:
            X = sigmoid(X)
    return X

