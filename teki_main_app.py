#  -*- coding: utf-8 -*-

"""
####################################
#  Program Name
###################################

The name 'Teki' pronounced as /Tɛki/ comes from a phonetic transcription of the informal phrase  t'es qui' - 'Who are you'.
It is reminiscent of Stromae's 2013 song - Papoutai - Papa ou t'es - lit. Father, you are where?
It there contrasts with the more formal phrase "Qui es-tu". The spelling of the program is meant to represent this. 
This word order is a form of topicalization that is actually quite common in French even if it is not necessarily exclusive to the language itself.
The name was chosen to reflect the process of researching conceptual and medial literacy and orality within the French language.

####################################
#  Medial and Conceptual Literacy and Orality
###################################

Excluding other modes by which human communication can be realized such as via sign language, body language, and whistling,
human languages are generally expressed medially by using graphic symbols or audible sound (Bader, 2002).
Written language is mediated visually, using symbols, whereas spoken language can be understood as a process, which employs audible sounds to express meaning (Bader, 2002).
However, an aspect that is often overlooked is literate vs. oral discourse.
With these distinctions in mind, the concepts of written vs. spoken and literal vs. oral arise.
The former represents the medial aspect of language, whereas the latter represents conceptual literacy and orality.
In other words, is the message of the speaker conceptually representative of written or spoken language irrespective of the medium?
These two domains do not represent a natural dichotomy, as one might automatically assume,
but rather, they are two domains of language that regularly correlate (Koch & Oesterreicher, 1985).

This distinction is best explain by the following tables:
+--------+------------------+------------------+------------------------+
|        |                  | Konzeption       | Konzeption             |
+--------+------------------+------------------+------------------------+
|        |                  | Gesprochen       | Geschrieben            |
+--------+------------------+------------------+------------------------+
| Medium | Graphischer Kode | Faut pas le dire | Il ne faut pas le dire |
+--------+------------------+------------------+------------------------+
| Medium | Phonischer Kode  | fopaldiʀ         | ilnəfplalədiʀ          |
+--------+------------------+------------------+------------------------+
Fig. 1 (Koch & Oesterreicher, 1985, p. 17)

The medium is either the phonischer kode, i.e., phonic code or it is the graphischer kode, i.e., graphic code.
This means that a message like faut pas le dire is medially literal, but conceptually oral.
In this particular example, it is due to the omission of il and ne, which belong to standard French (Koch & Oesterreicher, 1985; Müller, 1975).
The opposite of this applies as well where il ne faut pas le dire is conceptually and medially literal
as it complies with the written norms set forth by the governing linguistic bodies of the French language (Müller, 1975).

Terms:
    Konzeption - concept
    Gesprochen - spoken
    Geschrieben - written
    Graphischer Kode - graphic code
    Phonischer Kode  -  phonetic code

####################################
#  Creating Training Data and Testing Naive B
###################################

By introducing parameters that are language-independent such as sentence length, abbreviations, average word length, contractions, etc.
It was possible to identify literacy and orality even within a written medium. This program was designed with the goal of accessing the nature
of non-standard French data gathered from various internet resources. The premise behind this research was that the internet
is a place where norms are often overlooked and therefore most of the data would be conceptually oral, but medially literal.

Since no training data could be found that was adequate for the scope of this program, training data had to be created. 
Using the aforementioned parameters, classification sets were created to automatically identify sentences that contained features of conceptual literacy and conceptual orality.
After having done so, a multinomial naïve Bayes was trained to statistically assign a feature to an unknown sentence based on sentences it had previously seen.
The program works using the tags LIT and ORAL: LIT refers to the conceptually literacy and  ORAL refers to conceptual orality.

####################################
#  Program Application
###################################

To examine this further, three corpora were chosen: eBay, SMS and Wikiconflicts,i,e, French Wikipedia discussions.
The working thesis was that the sentences of the documents in the SMS corpus would contain conceptual orality,
whereas those of the Wikipedia discussions would  contain conceptual literacy.
The intersection of this would be eBay: containing both conceptual literacy and orality.
The thinking behind this is that sellers would have to use a blend of both to attract buyers.
This is done by appealing to a more expressive side using conceptual orality,
but also using conceptual literacy in order to appeal to customers as this seems to be more professional.

When creating the training data, eBay and Wikipedia had high levels of literacy with SMS chats having a high level of orality.
Testing with the naïve Bayes, eBay and Wikipedia had levels of literacy like those of the classification phase.
However, SMS chats had a low level of orality due to difficulties in classifying the non-standard data.
"""

###########################
# Standard libraries
###########################
import csv
import logging
import os
import sys
import timeit
from datetime import datetime

if __name__ == "__main__":
    """
    Starting the program will take a bit of time due to the amount of libraries and modules being imported.
    In my testing, it should take around 3 (Mac Os 11) - 9 (Windows 10) seconds to load all of the necessary information.
    However, the speed will depend entirely on your local resources. 
    """

    # Variables for measuring loading time
    datetime_now = datetime.now()
    current_time = datetime_now.strftime("%H:%M:%S")
    start_time = timeit.default_timer()
    print(f"The current time is {current_time}.")
    print("Please wait while libraries, modules and corpora are being imported...")
    print("This should only take between 5 - 30 seconds depending on your system resources...\n")

###############################
# Program continuation function
###############################


def continue_program(*args):
    """
    This function acts as a prompt for the user. The user can choose to either continue with the program or to exit it.

    :param '*args'
        :type str
            It can take as many string arguments as necessary. These are displayed as the message prompts.

    :return
       :rtype None
    """

    # Error prompts
    for message in args:
        print(message)
    print("")

    options = "yes", "no"

    # The while-loop remains in place until the user provides an appropriate response.
    print("Please enter the number of your response:")
    while True:

        for number, choice in enumerate(options):
            print(number, choice)
        print("")
        user = input("Would you like to continue with the program? ").lower()
        if user == "0":  # Yes

            user = input("Are you sure ? Program stability cannot be guaranteed. ").lower()
            if user == "0":
                break
            else:
                sys.exit("The program will now be terminated.")

        elif user == "1":  # No answer
            sys.exit("The program will not be terminated.")

        else:  # Incorrect or invalid answer
            print(f"'{user}' is not a valid response. Please enter a valid response.\n")


def _rebuild_requirement_resources():
    """
        This function recreates the dependencies so that that the main script can run properly
        in the event that certain files were deleted. This is not intended to circumvent the checks, but rather to allow the program to run,
        even if in properly, without getting an error message at the beginning of the program.
        Recreating the file does not allow for code stability, but rather for the initial file check
        to be bypassed.

     :return
        :rtype None
        There is no object, but a file is created that is placed in the main directory.
    """

    with open("requirement_resources.txt", mode="w+", encoding="utf-8") as resources:
        for path, subdirs, files in os.walk("app_program_resources"):
            for name in files:
                resources.write(os.path.join(path, name)+"\n")
    print("The requirement_resources.txt file has been updated.")

# Uncomment the following line for dependencies to rebuilt. After having done so, comment it out again to deactivate it.
#_rebuild_requirement_resources()

#########################
# Pip libraries
#########################


"""
The program can be run without the pip  modules, but program stability will be effected.
"""

try:
    import bs4
    import spacy
    import lxml
    from spacy.lang.fr import French
    from spacy.tokenizer import Tokenizer
    from bs4 import BeautifulSoup
except ImportError as error:
    requirements = sorted(open("requirements.txt").readlines())
    print("Necessary modules are missing from the program.")
    print("All of the following libraries and modules must be installed for the program to function properly:\n ")
    for req in requirements:
        print(req.strip())
    print("")
    continue_program("Would you like to continue without these libraries and modules?")

###########################################
# Importing custom files and modules
###########################################

"""
A program-wide check is performed for the necessary files. 
The program can still be started if any of the necessary files are missing, 
but the program stability will be greatly compromised. 
Necessary file names stored as requirement_resources.txt
"""

core_file_missing = list()
if os.path.exists("app_program_resources"):
    with open("requirement_resources.txt", mode="r", encoding="utf-8") as resource:
        for line in resource:
            if not os.path.exists(line.strip()):
                core_file_missing.append(line)
    try:
        from app_program_resources.app_auxiliary_functions import (
            about_program,
            restore_default_database,
            clear_log,
            DiscourseAnalysis,
            end_program,
            evaluation,
            file_finder,
            sub_menu,
            write_sentences,
            sentence_tokenizer,
            write_to_database
        )

    except Exception as error:
        print(f"The following error has occurred:\n{error}\n")
        message = "Would you like to proceed despite this error?"
        continue_program(message)


#########################
# Main Program Functions
#########################

# message prompt
return_main_menu_msg = "Please press return to enter to the main menu..."
enter_valid_option = "Please press enter to be able to reenter a valid option."


def get_text(document):
    """
    This functions reads in a .txt, .xml or .csv.
    This file is either in /app_program_resources/app_corpora
    or it is a file that has been dynamically specified by the user.

    :param 'document':
       :type str
            A path to the desired document file.

    :return soup
        :rtype <class 'bs4.BeautifulSoup>
        If the user chooses an xml-file, then a beautiful object is returned.

    :return csv_data
        :rtype list
            If the user chooses csv file, the a list of that data is returned.

    :return text
        :rtype str
            If the user chooses a .txt file,  then a string object is returned.
    """

    name, extension = os.path.splitext(document)

    with open(document, mode="r", encoding="utf-8") as file:
        if extension == ".xml":
            soup = bs4.BeautifulSoup(file, "lxml")
            return soup

        elif extension == ".csv":
            csv_reader = csv.reader(file, delimiter=",")
            csv_data = [row for row in csv_reader]
            return csv_data

        elif extension == ".txt":
            text = ""
            for line in file:
                sentence = line.rstrip().split()
                for word in sentence:
                    text += f"{word} "

            return text


def get_database():
    """
    This function retrieves the designated database file that is saved in a .csv file.
    For the file to be properly processed, the database should have the following format:
    Word, POS, Dep, Sentence Number, Corpus Tag, Feature, Tag
    corrélés,VERB,acl:relcl,SEN:2,cmr-wiki-c001-a1,LIT

    The function retrieves the file by invoking the function file_finder from app_auxiliary_functions
    The databases are located in
        app_program_resources/default_files/databases
        or
        app_user_resources/user_databases

    :param
        There are no parameters.

    :return database
        :rtype str
            The path name of the database selected.
    """

    database = file_finder()
    return database


def content_analysis(text):
    """
    This function returns the sentence_results of the functions contained within this function.

    :param text
        :type str
            The data from the get_text function.

    :return menu
        :rtype dict
        The collective sentence_results of the user according to the respective function.
    """

    def process_save(sentence_count, collective_results):
        """
        This function gives the user the option of either continue with processing their sentence results or
        saving them in a designated file.

        :param sentence_count
            :type int
              The number of sentences in the selection.

        :param collective_results
            :type dict
              All of the sentences with their respective id markers.

        :return:
            if user continues with the tagging processing
                :rtype None
            else
                :return collective sentence_results
            :rtype dict
                the results of the sentence analysis so that they can be further processed.
        """

        while True:
            options = "process sentences", "save unprocessed sentences", "return to menu"
            for number, choice in enumerate(options, start=1):
                print(number, choice)

            user = input(f"\nThe text has been parsed into approx. {sentence_count} sentences. How would you like to proceed? ")
            if user == "1":
                input("The sentence results will now be processed. Please press enter to continue...")
                return collective_results
            elif user == "2":
                file_time_id = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
                unprocessed_sentences_file = f"app_user_resources/sentence_results/sen_results_{file_time_id}.csv"

                write_sentences(collective_results, unprocessed_sentences_file)
                print(f"\nThe sentences have been saved.")
                input(return_main_menu_msg)
                return False
            elif user == "3":
                print("\nThe sentences will neither be saved nor processed. ")
                input(return_main_menu_msg)
                break
            else:
                print(f"{user} is not a valid option.")
                input(enter_valid_option)

    def read_contents():
        """
        This function only reads in the text data.
        After the text data has been read to the user, the user will be returned to the main menu.
        """
        print(text)
        input(f"\n{return_main_menu_msg}")

    def xml_analysis():
        """
        The .xml files are located in app_program_resources/app_corpora

        This function automatically extracts textual information from
        the .xml file that was selected by the user.

        The respective directories are listed from which the user may select.
        The user must input a valid option that is in the range
        of the corpus length. Once done, the loop will be broken and the user can progress.

        If the user has entered a valid selection, then this range is extracted from the desired corpus.
        The sentences are then parsed using the sentence_tokenizer located in the app_auxiliary_functions.py.
        It returns the parsed sentences and they are saved together with their respective id in a dictionary.

        It is theoretically possible for it to work with any file that has
        a corresponding .xml format. However, since the function was written with those files in mind specifically,
        the respective lines would have to be changed in order for it to accommodate other .xml files.

        :param
            There are no parameters.

        :return collective sentence_results
            if user decides to continue with processing the sentences.
                :rtype dict
            else
                :rtype None
                    the user is brought back to the main menu.
        """

        # Relevant for BeautifulSoup
        soup, xml_tag_id = text, list()

        while True:
            while True:
                corpora = "eBay", "SMS", "Wikipedia"
                for number, corpus in enumerate(corpora, start=1):
                    print(number, corpus)
                corpus_choice = input("\nFrom which corpus are you extracting the information? ")
                if corpus_choice.isdigit():
                    check_choice = int(corpus_choice)
                    if check_choice in list(range(1, 4)):
                        corpus_choice = int(corpus_choice)
                        break
                    else:
                        print(f"{corpus_choice} is not a valid option.")
                        input(enter_valid_option)

            if corpus_choice == 1:  # eBay listing
                for tag in soup.select("div[id]"):
                    xml_tag_id.append(tag["id"])
            elif corpus_choice == 2 or 3:  # SMS, wikipedia
                for tag in soup.select("post"):
                    xml_tag_id.append(tag["xml:id"])
            else:
                print(f"{corpus_choice} is not a valid option.")
                input(enter_valid_option)

            while True:
                print(f"There are {len(xml_tag_id)} tags. Please enter a selection range from 0 - {len(xml_tag_id)}.")
                print("A range should be specified as follows with a single space between both numbers: start stop.\n")
                corpus_range_choice = input("Please enter a valid range: ")
                print("")

                try:
                    corpus_range_choice = corpus_range_choice.split()
                    start, stop = int(corpus_range_choice[0]), int(corpus_range_choice[1])
                    collective_results = dict()
                    sentence_count = 0

                    for i in range(start, stop):
                        if corpus_choice == 1:
                            corpus_text = soup.find("div", id=xml_tag_id[i]).getText().strip().split()
                            results = sentence_tokenizer(corpus_text)
                            collective_results[xml_tag_id[i]] = results

                        elif corpus_choice == 2 or 3:
                            corpus_text = soup.find("post", {"xml:id": xml_tag_id[i]}).getText().strip().split()
                            results = sentence_tokenizer(corpus_text)
                            collective_results[xml_tag_id[i]] = results

                    for sentence in collective_results:  # Sentence calculation
                        sentence_count += len(collective_results[sentence])
                    return process_save(sentence_count, collective_results)

                except Exception as error:
                    print(f"{corpus_range_choice} is not a valid range.")
                    input("Please press enter to be able to reenter a valid range.")
                    logging.exception(f"xml_analysis error due to: {error}.")

    def txt_analysis():
        """
        This function tokenizes any text that is saved in .txt document.
        It first creates simplified tokens for the sake of creating sentence-level tokens are created in this functions.
        The real tokenization is done with Spacy.

        :return collective sentence_results
            if user decides to continue with processing the sentences.
                :rtype dict
            else
                :rtype None
                    the user is brought back to the main menu.
        """

        # Sentence tokenization
        user = input("Please enter a unique identifier ONLY using number of characters from (a-z, A-Z, 0-9) for this text: ")
        tokens = text.split()
        results = sentence_tokenizer(tokens)
        collective_results = dict()

        for number, sentence in enumerate(results):
            sentence_id = f"{user}_{number}"
            collective_results[sentence_id] = [sentence]
        return process_save(len(results), collective_results)

    # Dynamic submenu
    output_menu = {"read file contents": read_contents,
                   "analyze .XML data": xml_analysis,
                   "analyze .TXT data": txt_analysis,
                   "return to  main menu": lambda: False}

    # Submenu parameters
    menu_name = "\nContent Analysis"
    menu_information = "How would you like to proceed with the file?\n"
    menu = sub_menu(output_menu, menu_name, menu_information)

    # Value from one of the respective sub-functions
    return menu


def spacy_tagger(corpus_content):
    """
    This function takes in the information as determined by content analysis, which contains the parsed sentences.
    The relevant elements are then determined by Spacy which are:
        Token
        Part-of-speech
        Dependencies
        Morphology

    a unique sentence id is also added to each token and sentence so that it can identified in the database.

    :param corpus_content
       :type dict
        The sentence_results from the content analysis function

    :return collective_spacy_results
        :type dict
            The tagged and tokenized sentence_results of the corpus content from the content analysis.
    """
    print("The individual sentences are now being processed.")
    print("The duration will depend on your system resources and the number of sentences being processed.")
    print("Please wait...\n")

    nlp = spacy.load("fr_core_news_sm")
    collective_spacy_results = dict()
    for sen_id in corpus_content:
        corpus_sentence = corpus_content[sen_id]
        processed_sentence = list()

        for number, sentence in enumerate(corpus_sentence):
            doc = nlp(sentence)  # Spacy doc object
            for token in doc:
                # token, part-of-speech, dependencies, sentence id, morphology
                processed_sentence.append(
                                    (token.text,
                                     token.pos_,
                                     token.dep_,
                                     f"SEN:{number}",
                                     str(token.morph))
                                    )
            #  Unique sentence identifier
            processed_sentence_key = f"{sen_id}-{number}"
            collective_spacy_results[processed_sentence_key] = processed_sentence

            # overwriting the old with a new list so that the new sentence_results can be saved.
            processed_sentence = list()

    input(f"The sentences have been successfully processed. {return_main_menu_msg}")
    return collective_spacy_results


def save_results(feat, sentence_info, corpus_sentence_id, sub_sentences, sentence_file, database_file=False):
    """
    This saves the results from the analysis to the appropriate file and database.
    """
    sentence = sentence_info.sentence_reconstruction()[1]
    sen_num = sentence_info.sentence_reconstruction()[2]

    write_sentences(sentence, results_file=sentence_file, sen_num=sen_num,
                    sen_id=corpus_sentence_id, feat=feat, feat_save=True)

    if database_file:
        write_to_database(feat, corpus_sentence_id, sub_sentences, database_file)


def generate_training_data(collective_spacy_results, database_file, system_evaluation):
    """

    This function takes the sentence and its lexical information to determine the most appropriate feature to be assigned to said sentence.

    The batch analysis can be performed either automatically or manually.
    Automatically means that you would let the system choose the most appropriate feature for sentence
    based on the scoring system provided by the system. Manually means that you would like to personally assign the sentence features.

    'automatically' is the best option if you are not sure about which feature you should assign,
    'manually' is only useful if all of the sentences share the same feature as this option cannot
    differentiate between features whereas 'manually' can.

   Note to System _evaluation

    If the system is being run in evaluation mode, then a respective file is created i.e. a gold standard, against which the system sentence_results can be compared.
    However, this evaluation mode is experimental at best. It uses lexical information to determine if a sentence is LIT or ORAL. Due to the insufficient amount of
    data for this function, it is not intended to be used to create a reliable gold file. If one were to supply the files with more reliable training data,
    then it could be used to create more reliable results.

    :param collective_spacy_results
        :type dict
            The sentence_results that have been processed by Spacy.
    
    :param database_file
        :type str
        The path file to the respective database where the training data should be stored.

    :param system_evaluation
        :type bool
            Setting this to true puts the system in evaluation mode.

    :return
        :rtype None
            This function has no return, but saves the result to the specified database.
    """
    # import pickle
    # f = open("debug.pickle", "wb")
    # pickle.dump(collective_spacy_results, f)

    # Save directory and ID
    file_time_id = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    save_dir = "app_user_resources/evaluation_results"
    automatic_file = f"app_user_resources/sentence_results/automatic_feat_selection_{file_time_id}.csv"
    manual_file = f"app_user_resources/sentence_results/manual_feat_selection_{file_time_id}.csv"

    # Result files
    if system_evaluation:
        system_eval_file = f"{save_dir}/system_{file_time_id}.csv"
        gold_eval_file = f"{save_dir}/gold_{file_time_id}.csv"

        print("Note: This is an experimental function that might not deliver the best results.")
        input("The system is being evaluated. Please press enter to start the evaluation...")

        # System results
        redacted_corpus = DiscourseAnalysis(collective_spacy_results).redacted_corpus()
        for corpus_sentence_id in redacted_corpus:
            sub_sentences = collective_spacy_results[corpus_sentence_id]
            sentence_info = DiscourseAnalysis.LanguageIndependentAnalysis(sub_sentences)
            sentence_feature_info = sentence_info.feature_assignment()
            feat = sentence_feature_info[0]
            save_results(feat, sentence_info, corpus_sentence_id, sub_sentences, system_eval_file)

        # Gold results
        for corpus_sentence_id in collective_spacy_results:
            sub_sentences = collective_spacy_results[corpus_sentence_id]
            sentence_info = DiscourseAnalysis.LanguageIndependentAnalysis(sub_sentences)
            sentence_feature_info = sentence_info.feature_assignment()
            feat = sentence_feature_info[0]
            save_results(feat, sentence_info, corpus_sentence_id, sub_sentences, gold_eval_file)

        input(f"The system evaluation was completed without any errors. {return_main_menu_msg}")

    else:
        while True:
            options = "automatically", "manually"
            for number, choice in enumerate(options, start=1):
                print(number, choice)

            user = input("\nWould you like to have the features assigned automatically or manually? ")
            if user == "1":  # Automatic Assignment
                print("Please wait while the features are being assigned....")
                lit_count, oral_count, unk_count, sentence_count, token_count = 0, 0, 0, 0, 0
                lit_score, oral_score = {}, {}

                for corpus_sentence_id in collective_spacy_results:
                    sub_sentences = collective_spacy_results[corpus_sentence_id]
                    sentence_info = DiscourseAnalysis.LanguageIndependentAnalysis(sub_sentences)
                    sentence_feature_info = sentence_info.feature_assignment()
                    feat = sentence_feature_info[0]

                    save_results(feat, sentence_info, corpus_sentence_id,
                                 sub_sentences, automatic_file, database_file)

                    ##############################
                    # Determining sentence properties
                    ##############################
                    sentence = sentence_info.sentence_reconstruction()[1]
                    sentence_count += 1
                    token_count += len(sentence.split())

                    if feat == "LIT":
                        lit_count += 1
                        classification = sentence_feature_info[1]
                        for element in classification:
                            lit_score[element] = lit_score.get(element, 0) + classification[element]

                    elif feat == "ORAL":
                        oral_count += 1
                        classification = sentence_feature_info[1]
                        for element in classification:
                            oral_score[element] = oral_score.get(element, 0) + classification[element]
                    else:
                        unk_count += 1

                # Sentence property results
                count_results = {"Sentences": sentence_count,
                                 "Tokens": token_count,
                                 "LIT": lit_count,
                                 "ORAL": oral_count,
                                 "UNK": unk_count,
                                 }

                score_points = {
                    "LIT": [(key, value) for (key, value) in lit_score.items()],
                    "ORAL": [(key, value) for (key, value) in oral_score.items()],
                }

                print(f"\nAll of the sentences have been automatically assigned the most appropriate feature.\n")
                print("The sentence_results are as follows:")
                for score in count_results:
                    print(score, count_results[score])

                print("\nCombined total points of each class per feature\n")

                top_score_lit = sorted([number[1] for number in score_points["LIT"]], reverse=True)[:3]
                top_score_oral = sorted([number[1] for number in score_points["ORAL"]], reverse=True)[:3]

                for class_feat in score_points:
                    for score in score_points[class_feat]:
                        if class_feat == "LIT" and score[1] in top_score_lit:
                            print(class_feat, score)
                        elif class_feat == "ORAL" and score[1] in top_score_oral:
                            print(class_feat, score)

                input(f"\n{return_main_menu_msg}")
                break

            elif user == "2":
                options = "LIT", "ORAL"
                for number, choice in enumerate(options, start=1):
                    print(number, choice)
                print("")

                user = input("Please enter the number of the desired feature: ")
                if user == "1":
                    feat = "LIT"
                elif user == "2":
                    feat = "ORAL"
                input("Press enter to select the save location of the manual files....")

                for corpus_sentence_id in collective_spacy_results:
                    sub_sentences = collective_spacy_results[corpus_sentence_id]
                    sentence_info = DiscourseAnalysis.LanguageIndependentAnalysis(sub_sentences)
                    save_results(feat, sentence_info, corpus_sentence_id, sub_sentences, manual_file, database_file)

                print(f"\nAll of the sentences have been successfully assigned the feature {feat}.")
                input(return_main_menu_msg)
                break

            else:
                print(f"{user} is not a valid option.")
                input(enter_valid_option)


def get_feat_count(file):
    """
    This function retrieves the count of the features in the database.

    :param file
        :type str
             the path file of the database

    :return prior_prob
        :rtype dict
            The count of the database features

    :return training_data
        :rtype list
            The data from the .csv file saved in a list.
    """

    with open(file, mode="r", encoding="utf-8") as training_data:
        csv_reader = csv.reader(training_data, delimiter=",")
        training_data = [row for row in csv_reader]
        feat_count = {"LIT": 0, "ORAL": 0}
        sentence_collection = {(row[3], row[4], row[5]) for row in training_data}

        for sentence in sentence_collection:
            feat = sentence[2]
            feat_count[feat] = feat_count.get(feat, 0) + 1

        print("The database contains sentences with the following feature:")
        print("LIT:", feat_count.get("LIT", 0))
        print("ORAL:", feat_count.get("ORAL", 0))
        print("")

        return feat_count, training_data


def get_probs(freq_training_data):
    """
    This function calculates the probability of the features within database:

        P(s) = the probability of a sentence
        c = the count of a word
        s = meaning of word
        w = the word

    a-prior probability:
        Determine the proportions (= probabilities) of the different possible meanings s of a word w.
        P(s) = C(s,w)/C(w)

    individual feature probabilities:
        count how often each classification (oral) feature occurs with the different possible features
        p(Cj|S) = C(Cj,s)/C(s)

    For OOV (out of vocabulary) words:
            Smoothing the data using the method from Ng (1997)
                p(Cj|Sn) = P(Sn)/N = C(Sn)/N**2 for (Cj,Sn) = 0
                N is the training data.

    :return feat_count
        :rtype dict
            The count of said features.

    :return prob_results
        :rtype dict
            the probability of the each word having a certain feature.
    """

    feat_count, training_data = freq_training_data[0], freq_training_data[1]
    vocabulary, n_training_data = set(), sum(feat_count.values())
    prob_results = dict()
    oral_feat, lit_feat = dict(), dict()
    lit_tokens, oral_tokens = list(), list()

    for element in training_data:
        word, feat = element[0], element[5]
        vocabulary.add(word)

        if feat == "LIT":
            lit_tokens.append((word, feat))
            oral_feat[word] = oral_feat.get(word, 0) + 1

        elif feat == "ORAL":
            oral_tokens.append((word, feat))
            lit_feat[word] = lit_feat.get(word, 0) + 1

        # MLE probability of LIT
        if oral_feat.get(word, 0) > 0:
            feat_1_prob = oral_feat.get(word) / feat_count["LIT"]
        else:
            # Ng Smoothing
            feat_1_prob = feat_count["LIT"] / n_training_data ** 2

        # MLE probability of ORAL
        if lit_feat.get(word, 0) > 0:
            feat_2_prob = lit_feat.get(word) / feat_count["ORAL"]
        else:
            # Ng Smoothing
            feat_2_prob = feat_count["ORAL"] / n_training_data ** 2

        prob_results[word] = feat_1_prob, feat_2_prob

    return feat_count, prob_results


def sentence_classification(probabilities):
    """
    This function calculates the probability of the sentence.
    Using comparative product values, the biggest product with respect to feature 1 and feature 2 is chosen.
    The bigger value indicates that the sentence most likely belongs to this value as opposed to the other value

    This is based on bayes rule which is P(s|c) = P(c|s)·P(s)/P(c)
        * a-posterior = P(s|c)
        * feature = P(c|s)
        * a priori = P(s)

    The value is calculated using a variation of bayes called 'naive bayes'
       A naive bayes assumes that all individual features cj of context c used in classification (oral) are independent of each other.
       This contextual independence is therefore the nativity.

        s′ = argmaxs∈S  ( P(c|s) · P(s)/ P(c) ) = argmaxs∈S P(c|s) · P(s)

        The only relevant part is the maximum argument which is then:
            argmaxs∈S P(c|s) · P(s)
            P(c|s)= πCj∈cP(Cj|s)

        Result:
            The product of the probabilities (word count/feature count) are multiplied together and then with the a priori probability.
             if a value is not available, then it is smoothed according to Ng(1997)

            This product is the final value of the naive bayes.

    :param probabilities
        :type tuple
            The frequency of the feature and the probability sentence_results

    :return freq
        :rtype dict
            The frequency of said features.

    :return freq prob_results
        :rtype dict
            The probability of the each word having a certain feature.
    """

    def calculate(text):
        """
        This function calculates the probability of the sentence based on the information in the training data.

        :param text:
            :rtype str
                The sentence to be evaluated

        :return: feat
            :rtype str
                returns the most appropriate feature based on the probabilities available.
        """

        prior_prob, prob_results = probabilities[1], probabilities[0]
        lit_prob, oral_prob = prob_results["LIT"], prob_results["ORAL"]
        lit_prob_total = lit_prob / (lit_prob + oral_prob)
        oral_prob_total = oral_prob / (lit_prob + oral_prob)

        n_training_data = sum(prob_results.values()) ** 2
        lit_smooth = lit_prob / n_training_data
        oral_smooth = oral_prob / n_training_data
        word_feat_prob = dict()

        for word in text:
            if bool(prior_prob.get(word)):
                word_feat_prob[word] = prior_prob.get(word)
            else:
                word_feat_prob[word] = lit_smooth, oral_smooth

        for word in word_feat_prob:
            lit_prob_total *= word_feat_prob[word][0]
            oral_prob_total *= word_feat_prob[word][1]

        # a portion of the sentence is displayed
        sent_excerpt = " ".join(text[:7])

        # The results
        if lit_prob_total > oral_prob_total:
            print(f" The text '{sent_excerpt}...'is LIT.")
            return "LIT"
        elif oral_prob_total > lit_prob_total:
            print(f" The text '{sent_excerpt}...'is ORAL.")
            return "ORAL"
        else:
            print(f" The text '{sent_excerpt}...'is UNK.")
            return "UNK"

    while True:
        options = "analyze an individual sentence", "analyze sentences of a file", "return to main menu"
        for number, choice in enumerate(options, start=1):
            print(number, choice)

        user = input("\nWould you like to analyze a single sentence or all sentences from a corpus?\n")
        if user == "1":  # Sentence Analysis
            sentence = input("Please enter the sentence: ").split()
            calculate(sentence)
            input(return_main_menu_msg)

        elif user == "2":  # Collection of sentences from a document
            file_time_id = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
            bayes_file = f"app_user_resources/naive_bayes_results/naive_bayes_{file_time_id}.csv"

            collective_res = dict()
            text = get_text(file_finder())
            content = content_analysis(text)

            if content:
                tagger_results = spacy_tagger(content)
            else:
                # the user wants to return to the main menu
                break
            sentence_count, token_count, lit_count, oral_count, unk_count = 0, 0, 0, 0, 0

            for corpus_sentence_id in tagger_results:
                sub_sentences = tagger_results[corpus_sentence_id]
                sentence_info = DiscourseAnalysis.LanguageIndependentAnalysis(sub_sentences)
                sentence = sentence_info.sentence_reconstruction()[1]
                bayes = calculate(sentence.split())
                collective_res[bayes] = collective_res.get(bayes, 0) + 1
                save_results(bayes,  sentence_info, corpus_sentence_id, sub_sentences, bayes_file)

                sentence_count += 1
                token_count += len(sentence.split())
                if bayes == "LIT":
                    lit_count += 1
                elif bayes == "ORAL":
                    oral_count += 1
                else:
                    unk_count += 1

            res = {
                "Sentence count": sentence_count,
                "Token count": token_count,
                "LIT count": lit_count,
                "ORAL count": oral_count,
                "UNK count": unk_count
                }

            for entry in res:
                print(entry, res[entry])
        elif user == "3":
            input(return_main_menu_msg)
            break

        else:
            print(f"{user} is not a valid option.")
            input(enter_valid_option)


#########################
# Main program
#########################


def run_program(default_doc, default_train, system_evaluation):
    """
    This function contains all other functions listed within this script. The functions can then be selected.
    It automatically loads the two standard files, but these can be changed dynamically by the user
    while the script is running. The menu loop is broken once the user has selected an option from the menu.
    after the desired function has been executed, the user is returned to the main menu
    unless the program has been terminated by the respective function.

    :param default_doc
        :type str
            the path file name for the default document

    :param default_train
        :type str
            the path file name for the default training file.

    :param system_evaluation
        :type bool
            this sets the program in evaluation mode and allows the automatic creation of a gold file.
    """
    stop = timeit.default_timer()
    execution_time = round(stop - start_time)
    print(f"All libraries were loaded {execution_time} seconds. The program can now start.\n")

    main_menu = {
        "load .xml or .txt file": get_text,
        "load training file": get_database,
        "analyze contents": content_analysis,
        "sentence classification": sentence_classification,
        "clear error log file": clear_log,
        "restore default database": restore_default_database,
        "evaluation": evaluation,
        "about program": about_program,
        "end program": end_program
        }

    # Default files
    doc = get_text(default_doc)
    database = default_train

    if system_evaluation:
        print("You are currently running the system in experimental evaluation mode.")
        print("To turn this process off, please set system_evaluation variable to 'False'.\n")

    print("You are currently using the app_common_default_docs files:\n")
    print(f"Default Text: '{default_doc}'")
    print(f"Default Training: '{default_train}'")
    print(" \nIf you wish to proceed with other files, please load them from respective directories.")

    while True:
        print("")
        # Text menu message prompt
        banner = "~ Teki - French Discourse Analyzer ~ ", "#### Main Menu ####\n"
        for word in banner:
            print(word.center(50))

        # Listing the menu options
        for menu_number, menu_item in enumerate(main_menu, start=1):
            print(f'{menu_number}: {menu_item}')

        # Standard message prompts
        choice_str = input('\nPlease enter the number of your entry: ')
        main_message = "Please press the enter key to return to the main menu.\n "

        # Executes the function as specified by the user via the number.
        if choice_str.isdigit():
            choice_num = int(choice_str)

            # Only menu options that are within the scope of the main menu are allowed.
            if 0 < choice_num <= len(main_menu):
                function_number = choice_num - 1
                function_values = list(main_menu.values())
                function_name = str(function_values[function_number]).split()[1]

                # Functions that require parameters are executed here.
                if function_number in list(range(5)):

                    if function_name == "get_text":
                        try:
                            path_name = file_finder()
                            doc = get_text(path_name)
                        except Exception as error:
                            input(f"You did not select a file. {main_message}")
                            logging.exception(f"No txt/xml selection: {error}")

                    elif function_name == "get_database":
                        try:
                            database = get_database()
                        except Exception as error:
                            input(f"You did not select a file. {main_message}")
                            logging.exception(f"No database selection: {error}")

                    elif function_name == "content_analysis":
                        try:
                            content = content_analysis(doc)
                            if content:
                                collective_results_tagged = spacy_tagger(content)
                                generate_training_data(collective_results_tagged,
                                                       database, system_evaluation)
                        except Exception as error:
                            print(f"An unknown error occurred. {main_message}")
                            logging.exception(f"Main Menu: {error}")

                    elif function_name == "sentence_classification":
                        try:
                            freq = get_feat_count(database)
                            probs = get_probs(freq)
                            sentence_classification(probs)
                        except:
                            pass

                    elif function_name == "clear_log":
                        clear_log('teki_error.log')
                else:
                    # executes functions that do not require parameters
                    function_values[function_number]()

if __name__ == "__main__":
    #########################
    # Error Logger
    #########################
    log_file = 'teki_error.log'
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format="""\n%(levelname)s_TIME: %(asctime)s\nFILE_NAME: %(filename)s\nMODULE: %(module)s
                        \nLINE_NO: %(lineno)d\nERROR_SCOPE %(message)s\n""")

    #########################
    # Program Execution
    #########################

    """
    The main program will only run if all of the necessary files are available and
    if all of the main libraries have been installed. This can be overridden by the user, 
    but it is not advised as it can lead to the program becoming unstable.  
    """

    system_evaluation = False
    missing_files_libares = bool(core_file_missing)
    default_doc = r"app_program_resources/default_files/muller_corpora/mueller_oral.txt"
    default_train = r"app_program_resources/default_files/databases/default_database.csv"
    defaults = os.path.exists(default_doc), os.path.exists(default_train)
    default_files = {"Default doc exists: ": os.path.exists(default_doc),
                     "Default train exist: ": os.path.exists(default_train)}

    try:
        if missing_files_libares == False and defaults[0] == defaults[1] == True:
            run_program(default_doc, default_train, system_evaluation)
        else:
            print("\nAn error has occurred probably because files, libraries or directories are missing:\n")
            for file in default_files:
                print(file, default_files[file])

            if core_file_missing:
                for entry in core_file_missing:
                    print(entry)
                print("")

            continue_program()
            run_program(default_doc, default_train, system_evaluation)

    except Exception as error:
        print("An unexpected error occurred. Please consult the error log.")
        logging.exception(f" 'if __name__ == __main__': is due to '{error})'")