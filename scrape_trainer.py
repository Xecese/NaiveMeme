import praw
import json

if __name__ == "__main__":
    r = praw.Reddit('NaiveBayes Meme Classifier Scraper')
    #clearly don't put your credentials in a git repo
    r.login = ('username', 'password')

    training_text_file = open("trainer.json", "r+")
    training_sentences = json.load(training_text_file)
    training_text_file.close()

    #hacky way to append to the json object - just overwrite everything
    training_text_file = open("trainer.json", "w")

    subreddit = r.get_subreddit('all')

    meme = None
    while (meme != "end session"):
        comments = subreddit.get_comments(limit = 50)
        for comment in comments:
            print comment.body
            meme = raw_input("Classify as: ")
            print
            if meme == "end session":
                break
            labeled_sentence = dict()
            labeled_sentence["text"] = comment.body
            labeled_sentence["label"] = meme
            training_sentences.append(labeled_sentence)

    json.dump(training_sentences, training_text_file, indent=4, separators=(',', ':'))
    training_text_file.close()
