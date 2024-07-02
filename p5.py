import csv
import random
import math
def main():
    filename = 'diabetes.csv'
    dataset = load_csv(filename)
    split_ratio = 0.87
    training_set,test_set = split_dataset(dataset,split_ratio)
    separated = separated_by_class(training_set)
    summaries = {class_value:summarize(row) for class_value,row in separated.items()}
    predictions = get_predictions(summaries,test_set)
    accuracy = get_accuracy(test_set,predictions)
    print(accuracy)

def load_csv(filename):
    with open(filename,'r') as file:
        lines = csv.reader(file)
        dataset = [list(map(float,row)) for row in lines]
    return dataset

def split_dataset(dataset,split_ratio):
    train_size = int(len(dataset)*split_ratio)
    train_set = random.sample(dataset,train_size)
    test_set = [row for row in dataset if row not in train_set]
    return train_set,test_set

def separated_by_class(dataset):
    separated = {}
    for row in dataset:
        class_value = row[-1]
        if class_value not in separated:
            separated[class_value] = []
        separated[class_value].append(row)
    return separated

def summarize(dataset):
    summaries = [(mean(col),stdev(col)) for col in zip(*dataset)]
    return summaries[:-1]

def mean(numbers):
    mean = sum(numbers)/float(len(numbers))
    return mean

def stdev(numbers):
    avg = mean(numbers)
    variance = sum((x-avg)**2/float(len(numbers)-1) for x in numbers)
    return math.sqrt(variance)

def get_predictions(summaries,test_set):
    return [predictions(summaries,row) for row in test_set]

def predictions(summaries,input_vector):
    probabilities = calculate_class_probabilities(summaries,input_vector)
    return max(probabilities,key=probabilities.get)

def calculate_class_probabilities(summaries,input_vector):
    probabilities = {}
    for class_value,class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            mean,stdev = class_summaries[i]
            x = input_vector[i]
            probabilities[class_value]*=calculate_probability(mean,stdev,x)
    return probabilities

def calculate_probability(mean,stdev,x):
    exponent = math.exp(-((x-mean)**2/(2*stdev**2)))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent

def get_accuracy(test_set,predictions):
    correct = sum(1 for i in range(len(test_set)) if test_set[i][-1]==predictions[i])
    return (correct/float(len(test_set)))*100.0

main()
    
