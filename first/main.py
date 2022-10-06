import pickle


with open('D:/file.pkl', 'rb') as inp_file:
    obj = pickle.load(inp_file)
    print(obj)