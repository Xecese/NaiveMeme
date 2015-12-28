from textblob.classifiers import NaiveBayesClassifier
import pickle

if __name__ == "__main__":
    with open('trainer.json', 'r') as fp:
        classifier = NaiveBayesClassifier(fp, format="json")

    with open('classifier.obj', 'w') as fp:
        pickle.dump(classifier, fp)
