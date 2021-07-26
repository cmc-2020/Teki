#  -*- coding: utf-8 -*-

#########################
# Importing standard python libraries
#########################
import csv
import json
import importlib
import logging
import os
import sys
import timeit
from datetime import datetime

if __name__ == "__main__":
    # Starting the program will take a bit of time  due to the amount of libraries being imported.
    # This is to measure the loading time of the program. It should take around 3 - 8 seconds to load everything.

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    start = timeit.default_timer()
    print(f"The current time is {current_time}.")
    print("Please wait while libraries and files are being imported...")
    print("This could take a while depending on your system resources.\n")

#########################
#  Program description
#########################
"""
This program's function is to access the literacy and orality 
of French chat data by using markers that can identify said features.
"""


#########################
# Program continuation function
#########################


def continue_program(*args):
    """
    This function acts as a prompt for the user.
    They can choose to either continue with the program or exit.

    :param
        :type str
            '*args': It can take as many string arguments as necessary.

    :return
       :rtype None
    """

    # Displays the error prompt messages.
    for message in args:
        print(message)
    print("")

    while True:
        # The while-loop remains in place until the user provides an appropriate response.
        user = input("Would you still like to continue with the program (y/n) ?: ").lower()

        # Yes
        if user == "y":
            user = input("Are you sure? Program stability cannot be guaranteed (y/n)?: ").lower()

            #  Yes
            if user == "y":
                """
                This will cause the loop to be broken. 
                This will therefore also allow the main program to continue running. 
                However, stability cannot be guaranteed. 
                """
                break
            else:
                # The entire program will be shut down
                sys.exit("The program will now be terminated.")

        # No answer
        elif user == "n":
            sys.exit("The program will not be terminated.")

        # Incorrect answer
        else:
            print(f"'{user}' is not a valid response. Please enter a valid response.\n")


def missing_files(file_list, path):
    """
    This checks to see if all of the necessary files
    are available so that the program can start and be stable.

    :param
        :type str
            'file_list': list of the files which should be available

        :type str
            'path': name of the folder from which the file names are retrieved.

    :return
        :rtype list
            'missing':  a list of the missing files

        :rtype  False
            This means that no files are missing.

    """
    # the missing files are stored here
    missing = list()

    # This checks the respective directly for the desired files.
    for root in os.listdir(path):
        if root not in file_list:
            missing.append(root)

    # If not all files are available, then a list of said files are returned.
    if missing:
        return missing

    # False is the desired result. This means that all files are available i.e. not missing.
    else:
        return False


#########################
# Importing pip libraries
#########################
"""
The libraries are iteratively imported. 
The libraries that are missing will be saved in a list 
that will be referenced against later.
"""

missing_libraries = []
pip_lib = "bs4", "spacy", "lxml"

for lib in pip_lib:
    # Iteratively loads the libraries using importlib
    try:
        globals()[lib] = importlib.import_module(lib)
    except ModuleNotFoundError as error:
        logging.exception(f" pip module import': is due to '{error})'")
        missing_libraries.append(lib)

"""
Libraries from the modules are imported. 
If they cannot be imported, then the program will shut down. 
"""

try:
    from spacy.lang.fr import French
    from spacy.tokenizer import Tokenizer
    from bs4 import BeautifulSoup
except Exception as error:
    print("It seems that some pip modules could not be imported. Please check the log file.")
    logging.exception(f" pip library import': is due to '{error})'")
    sys.exit()

#########################
# Importing custom files and modules
#########################
"""
A program-wide check is performed for the necessary files . 
The program can still be started if any of the necessary files are missing, 
but the program stability will be greatly compromised. 
"""

# Necessary file names stored in json format in the main  app directory
data = open("app_resource_files.json", mode="r", encoding="utf-8")
necessary_files = json.load(data)

if os.path.exists("app_resources"):

    # This checks for the existence of the app resource directory and the contents therein.
    doc_files = missing_files(necessary_files["docs"], "app_resources/app_content_docs")
    dev_files = missing_files(necessary_files["dev"], "app_resources/app_dev/dev_files")
    test_files = missing_files(necessary_files["test"], "app_resources/app_test/test_files")
    compressed_repository = missing_files(necessary_files["compressed"], "app_resources/app_compressed_data")

    #  This lets the program know if files are missing.
    core_files = dev_files, doc_files, test_files, compressed_repository
    core_file_missing = sum([bool(i) for i in core_files])

    try:
        # importing custom modules from the auxiliary functions file
        from app_resources.auxiliary_functions import (
            about_program,
            clear_log,
            end_program,
            file_finder,
            sub_menu,
            save_sentences,
            sentence_tokenizer,
            write_to_database)

    except Exception as error:
        print("It seems that not all custom modules could be imported. Please check the log file")
        logging.exception(f" custom module import': is due to '{error})'")

else:
    message = "The app resource directory is either missing or has been renamed."
    continue_program(message)


#########################
# Main Program Functions
#########################


def get_text(document):
    """
    This functions reads in a text file. This file is either the default file
    or it is the file that has been dynamically specified by the user.
    The check is done by looking for the .xml ending in the program file.

    :param
       :type str 'document':
            a path to the desired document file.

    :return
        :rtype <class 'bs4.BeautifulSoup>
        'soup': if the user chooses an xml-file, then a beautiful object is returned

        :rtype str
            'text': if the user chooses anything else other than .xml file

    Returns
    """

    if ".xml" in document:
        with open(document, mode="r", encoding="utf-8") as file:
            soup = bs4.BeautifulSoup(file, "lxml")
            return soup

    else:
        with open(document, mode="r", encoding="utf-8") as file:
            text = file.read()
            return text


def get_database():
    """
    This function retrieves the designated database file that is saved in an .csv file
    The database should have the following format for it to be properly processed.
    Word, POS, Dep, Sentence number, Corpus Tag, Feature, Tag
    corrélés,VERB,acl:relcl,SEN:2,cmr-wiki-c001-a1,LIT

    :param
        There are no parameters.

    :return
        :rtype str
            'database' is  the path name of the database.
    """

    # It retrieves the file by invoking the function file_finder from auxiliary_functions.py
    database = file_finder()

    return database


def analyze_content(text):
    """
    This function has the main function of returning the results of the sub-functions.
    it is therefore more of a container of sorts.

    :param
        :type str
            'text' is the the data from the get_text function.

    :return
        :rtype dict
        the collective results of the user

    """

    def tag_save(sentence_count, collective_results):
        """
        This function gives the user the option of either tagging their results or
        saving them in a designated file.

        :param
            :type int
             'sentence_count': the number of sentences in the selection

        :param
            :type dict
            'collective_results': all of the sentences with their respective id.s

        :return:
            if user tags
            :rtype None
            else
            :rtype
                returns the collective results back so that they can be tagged.
        """
        while True:
            user = input(
                f"The text has been parsed into {sentence_count} sentences. Would you like to tag or save the sentences (tag/save): ")

            if user == "tag":
                input("The results will now be tagged. Please press enter to continue with the tagging process.")
                return collective_results
            elif user == "save":
                print("Please select the directory:")
                path = file_finder()
                save_sentences(collective_results, path)
                input(f"The results have been saved in {path}. Press enter to the main menu.")
                return False
            else:
                print(f"{user} that is not a valid option.")

    def read_contents():

        """
        This function only reads the text data. After the text data has been read,
        the user will be forwarded to the main menu.

        :param
           There are no parameters as it has access to the necessary data which

        :return
            :rtype None
        """

        print(text)
        input("\nPlease press enter to continue to the main menu.")

    def xml_analysis():
        """
        This function automatically extracts textual information from
        the .xml files that are located in the app resource directory.
        It is theoretically possible for it to work with any file that has
        a corresponding .xml format.

        However, since the function has been written specifically with those files in mind,
        the respective lines would have to be changed in order for it to accommodate other .xml files


        :param:
            There are no parameters as it has access to the necessary data which
            is within the scope of this function.

        :return:
            if user tags
            :rtype collective results

            else
            :rtype
                None
                the user is brought back to the main menu
        """
        # renamed to  be consistent with beautiful soup terminology
        soup = text

        while True:

            while True:
                """
                The respective directories are listed from which the user may select.
                The user must input a valid option that is in the range
                of the corpus length. Once done, the loop will be broken and the user can progress.
                """
                corpora = "eBay", "SMS", "Wikiconflict"
                for num, corpus in enumerate(corpora, start=1):
                    print(num, corpus)

                corpus_choice = input("\nFrom which corpus are you extracting the information?")

                if corpus_choice.isdigit():
                    check_choice = int(corpus_choice)

                    if check_choice in list(range(1, 4)):
                        corpus_choice = int(corpus_choice)
                        break
                    else:
                        print(f"{corpus_choice} is not a valid option. Please select a valid option.")

            # xml id tags are only relevant for the .xml corpora as  .txt do not have xml tags.
            xml_tag_id = list()

            if corpus_choice == 1:  # eBay listing
                for tag in soup.select("div[id]"):
                    xml_tag_id.append(tag["id"])

            elif corpus_choice == 2 or 3:  # SMS, Wikiconflict
                for tag in soup.select("post"):
                    xml_tag_id.append(tag["xml:id"])
            else:
                print("You did not enter a valid corpus number.\n")

            while True:
                print(f"There are {len(xml_tag_id)} tags. Please enter a selection range from 0 - {len(xml_tag_id)}.")
                print("A range should be specified as follows with a single space between both numbers: start stop.\n")
                corpus_range_choice = input("Please enter a valid selection: ")
                print("")

                try:
                    """
                    If the user has entered a valid selection, 
                    then this range i.e. selection is extracted from the desired corpus. 
                    The sentences are then parsed using the sentence_tokenizer located in the auxiliary_functions.
                    It returns the parsed sentences and they are saved together with their respective id in a dictionary.
                    """

                    corpus_range_choice = corpus_range_choice.split()
                    start, stop = int(corpus_range_choice[0]), int(corpus_range_choice[1])
                    collective_results = dict()
                    sentence_count = 0

                    for i in range(start, stop):

                        # Extracting the selection and tokenizing it.
                        if corpus_choice == 1:
                            corpus_text = soup.find("div", id=xml_tag_id[i]).getText().strip().split()
                            results = sentence_tokenizer(corpus_text)
                            collective_results[xml_tag_id[i]] = results

                        elif corpus_choice == 2 or 3:
                            corpus_text = soup.find("post", {"xml:id": xml_tag_id[i]}).getText().strip().split()
                            results = sentence_tokenizer(corpus_text)
                            collective_results[xml_tag_id[i]] = results

                    #  Calculating the total amount of sentences
                    for sentence in collective_results:
                        sentence_count += len(collective_results[sentence])

                    return tag_save(sentence_count, collective_results)

                except Exception as error:
                    logging.exception(f"xml_analysis error due to: {error}")
                    print(f"{corpus_range_choice} is not a valid selection. Please enter a valid choice.\n")

    def txt_analysis():

        """
        This function tokenizes any text that is saved in .txt-style document.

        :param:
            There are no parameters as it has access to the necessary data which
            is within the scope of this function.

        :return:
            if user tags
            :rtype collective results

            else
            :rtype
                None
                the user is brought back to the main menu
        """

        """
        Creates simplified tokens for the sake of creating sentence-level tokens
        The real tokens will be down with spacy. 
        """

        tokens = text.split()

        user = input("Please enter a unique identifier using number of characters from (a-z, A-Z, 0-9) for this text: ")
        results = sentence_tokenizer(tokens)
        collective_results = dict()

        for num, sen in enumerate(results):
            path_id = f"{user}_{num}"
            collective_results[path_id] = [sen]

        return tag_save(len(results), collective_results)

    # This is the dynamic menu that the user has access during this function
    output_menu = {"read file contents": read_contents,
                   "analyze XML data": xml_analysis,
                   "analyze .TXT data": txt_analysis,
                   "return to menu": lambda: False
                   }

    # Submenu parameters
    menu_name = "Analysis Menu"
    menu_information = "How would you like to proceed with the file:"
    menu = sub_menu(output_menu, menu_name, menu_information)

    return menu


def spacy_tagger(corpus_content):
    """
    This function works with the spacy tagger. It has the goal of parsing the sentences into their respective tokens.

    The relevant elements from spacy are:
    Word
    Part-of-speech
    Dependencies

    :parameter:
       :type dict
        'corpus_content': the results from the extract functions are processed here

    :return
        :type dict
        'collective_results_tagged': the tagged and tokenized results of the corpus content.
    """
    print("The individual sentences are now being tagged.")
    print("The duration will depend on your system  resources and the number of sentences being tagged.")
    print("Please wait...\n")

    collective_results_tagged = dict()
    nlp = spacy.load("fr_core_news_sm")

    for sent in corpus_content:

        corpus_sentence = corpus_content[sent]
        new_sentence = list()

        for number, sentence in enumerate(corpus_sentence):
            # Creates a doc object with all lexical information using spacy
            doc = nlp(sentence)

            for token in doc:
                # the results of the analysis
                new_sentence.append((token.text, token.pos_, token.dep_, sent, f"SEN:{number}"))

            #  generates a unique identifier for the sentences
            new_key = f"{sent}-sen_no-{number}"
            collective_results_tagged[new_key] = new_sentence

            # overwriting the old with a new list so that the new results can be saved.
            new_sentence = list()

    input("The sentences have been successfully tagged. Please press enter to continue...")
    return collective_results_tagged


def sentence_identification(collective_results_tagged, database):
    """
    This function takes the sentence and its lexical information to determine the most appropriate feature to be assigned to said sentence

    :parameter
        :type dict
            'collective_results_tagged': The results that have been tagged. The should be saved somewhere in the
            the programs directory

        :type str
        ' database': the path file to the respective directory

    :return
        :rtype None
            This function has no return, but saves the result to the specified database.
    """

    for sentences in collective_results_tagged:
        sub_sentences = collective_results_tagged[sentences]
        write_to_database("ORAL", sub_sentences, database)


def get_freq(file):
    """
    This function retrieves the count of ORAL,  LIT in the database.

    :param
        :type str
            'file'': the path file of the database

    :return
        :rtype dict
            'prior_prob': the frequency of  said features.

        :rtype list
            'training_data': the data from the csv file saved in a list.
    """

    with open(file, mode="r", encoding="utf-8") as training_data:
        csv_reader = csv.reader(training_data, delimiter=",")
        training_data = [row for row in csv_reader]

        # Features to be found in the text
        prior_prob = {"ORAL": 0, "LIT": 0}
        sentence_lex = {(row[3], row[4], row[5]) for row in training_data}

        for sentence in sentence_lex:
            entry = sentence[2]
            prior_prob[entry] = prior_prob.get(entry) + 1

        return prior_prob, training_data


def get_probs(freq_training_data):
    """
    This function calculates the probability of  the features

    :param
        :type tuple
            'csv_results': is a tuple which contains the frequency of the feature and the file_data

    :return
        :rtype dict
            'freq': the frequency of said features.

        :rtype dict
            'prob_results': the probability of the each word having a certain feature.
    """
    prior_prob, training_data = freq_training_data[0], freq_training_data[1]

    prob_results = dict()
    freq_feat_1, freq_feat_2 = dict(), dict()
    tokens_feat_1, tokens_feat_2 = list(), list()

    vocabulary = set()
    n_training_data = sum(prior_prob.values())

    for element in training_data:
        """
         smoothing the data using the method from Ng (1997)
         p(Cj|Sn) = P(Sn)/N = C(Sn)/N**2 for (Cj,Sn) = 0
         N is the training data
         """

        word, feat = element[0], element[5]
        vocabulary.add(word)

        if feat == "LIT":
            tokens_feat_1.append((word, feat))
            freq_feat_1[word] = freq_feat_1.get(word, 0) + 1

        elif feat == "ORAL":
            tokens_feat_2.append((word, feat))
            freq_feat_2[word] = freq_feat_2.get(word, 0) + 1

        # Calculating the MLE probability of Feat 1
        if freq_feat_1.get(word, 0) > 0:
            feat_1_prob = freq_feat_1.get(word) / prior_prob["LIT"]
        else:
            # Ng Smoothing
            feat_1_prob = prior_prob["LIT"] / n_training_data ** 2

        # Calculating the MLE probability of Feat 2
        if freq_feat_2.get(word, 0) > 0:
            feat_2_prob = freq_feat_2.get(word) / prior_prob["ORAL"]
        else:
            # Ng smooth
            feat_2_prob = prior_prob["ORAL"] / n_training_data ** 2

        prob_results[word] = feat_1_prob, feat_2_prob

    return prior_prob, prob_results


def classify_sentence(text, probabilities):
    """
    This function calculates the probability of  the features

    :param
        :type str
            the sentence to identified.

        :type tuple
            'probabilities': is a tuple which contains the frequency of the feature and the probability results

    :return
        :rtype dict
            'freq': the frequency of said features.

        :rtype dict
            'prob_results': the probability of the each word having a certain feature.
    """

    prior_prob, prob_results = probabilities[1], probabilities[0]

    feat_1_prob, feat_2_prob = prob_results["LIT"], prob_results["ORAL"]

    feat_1_total_prob = feat_1_prob / (feat_1_prob + feat_2_prob)
    feat_2_total_prob = feat_2_prob / (feat_1_prob + feat_2_prob)

    n_training_data = sum(prob_results.values()) ** 2
    orality_smooth = feat_1_prob / n_training_data
    literacy_smooth = feat_2_prob / n_training_data

    sentence_prob = dict()

    for word in text:
        if bool(prior_prob.get(word)):
            sentence_prob[word] = prior_prob.get(word)
        else:
            sentence_prob[word] = orality_smooth, literacy_smooth

    for word in sentence_prob:
        feat_1_total_prob *= sentence_prob[word][0]
        feat_2_total_prob *= sentence_prob[word][1]

    if feat_2_total_prob > feat_1_total_prob:
        print(f" '{text} 'is literal {feat_2_total_prob}")
    else:
        print(f" '{text}' is oral {feat_1_total_prob}")

    input("Please press enter to return to the main menu.")

#########################
# Main program
#########################


def run_program(default_doc, default_train):
    """
    This function contains all other functions listed within this script. The functions
    can be selected
    It automatically loads the two standard files, but these can be changed dynamically by the user
    while the script is running.

    :parameter
        :type str
        'default_doc' the path file name for the default document

        :type str,
        default_doc' the path file name for the default training file
    :return
        :type None
            This function has no return value
    """

    # The loading time here is assumed to be less than one minute i.e. less than 60 seconds.
    stop = timeit.default_timer()
    execution_time = round(stop - start)
    print(f"All libraries were loaded {execution_time} seconds. The program can now start.\n")

    # This is the menu from which the user can dynamically select an option by entering the respective menu option number.
    main_menu = {
        "load .xml or .txt file": get_text,
        "load training file": get_database,
        "analyze contents": analyze_content,
        "classify sentence": classify_sentence,
        "clear error log file": clear_log,
        "about program": about_program,
        "end program": end_program
        }

    # default data files
    doc = get_text(default_doc)
    database = default_train

    print("You are currently using the default files:\n")
    print(f"Default Text: '{default_doc}'")
    print(f"Default Training: '{default_train}'")
    print(" \nIf you wish to proceed with other files, please load them from respective directories.")

    while True:
        """
        The loop is broken once the user has selected an option from the menu. 
        after the desired function has been executed, the user is returned to the main menu 
        unless the program has been terminated by the respective function.
        """

        print("")
        # Text menu message prompt
        banner = "~ Teki - French Discourse Analyzer ~ ", "#### Main Menu ####"
        for word in banner:
            print(word.center(50))

        # Listing the menu options
        for menu_number, menu_item in enumerate(main_menu, start=1):
            print(f'{menu_number}: {menu_item}')

        # Standard message prompts
        choice_str = input('\nPlease enter the number of your entry: ')
        main_message = "Please the enter key to return to the main menu.\n"

        # Executes the function as specified by the user via the number
        if choice_str.isdigit():
            choice_num = int(choice_str)

            # Only menu options that are within the scope of the main menu are allowed
            if 0 < choice_num <= len(main_menu):
                function_values = list(main_menu.values())
                function_number = choice_num - 1
                function_name = str(function_values[function_number]).split()[1]

                # Functions that required parameters are executed here.
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

                    elif function_name == "analyze_content":
                        try:
                            content = analyze_content(doc)

                            if content:
                                #  Other functions will be carried out if bool(content) is True
                                collective_results_tagged = spacy_tagger(content)
                                sentence_identification(collective_results_tagged, database)

                        except Exception as error:
                            print(f"An unknown error occurred. {main_message}")
                            logging.exception(f"Main Menu: {error}")

                    elif function_name == "classify_sentence":

                        # text = input("Enter the sentence that you would like to classify: ")
                        text = "a seat at the bar which serves up surprisingly"
                        freq = get_freq(database)
                        probs = get_probs(freq)
                        classifier = classify_sentence(text.split(), probs)

                    elif function_name == "clear_log":
                        clear_log('app_resources/app_content_docs/error.log')
                else:
                    # executes functions that do not need argument
                    function_values[function_number]()


if __name__ == "__main__":

    #########################
    # Error Logger
    #########################
    log_file = 'app_resources/app_content_docs/error.log'
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format="""\n%(levelname)s_TIME: %(asctime)s\nFILE_NAME: %(filename)s\nMODULE: %(module)s
                        \nLINE_NO: %(lineno)d\nERROR_SCOPE %(message)s\n"""
                        )

    #########################
    # Program Execution
    #########################
    """
    The main program will only run if all of the necessary files are available and 
    if all of the main libraries have been installed.  This can be overridden by the user, 
    but it is not advised as it can lead to the program becoming unstable.  
    """
    try:
        default_doc = r"app_resources/app_dev/dev_files/french_text_1.txt"
        default_train = r"app_resources/app_databases/cl_2_updated.csv"
        if bool(core_file_missing) is False and bool(missing_libraries) is False:
            run_program(default_doc, default_train)
        else:
            message = "An error has occurred because either files or directories are missing."
            continue_program(message)
            run_program(default_doc, default_train)

    except Exception as error:
        print("An unexpected error occurred. Please check the error log.")
        logging.exception(f" 'if __name__ == __main__': is due to '{error})'")