#!/usr/bin/env python3

# Author: Yao Yan
# Description: This script is used to evaluate the annotation by participants with
# gold standards, we will conduct the annotation based on subcategory: date, person name,
# physical address

import json
import argparse
import re

# take as input the location of


class DateEvaluation(object):
    # The evaluation of a prediction file.
    def __init__(self):
        self.gs_dict_seq = dict()
        self.sys_dict_seq = dict()
        self.gs_dict_token = dict()
        self.sys_dict_token = dict()
        self.date_loc_list = list()
        self.date_type_list = list()
    # load the json file and convert it to a dictionary with key

    def convert_dict(self, sys_file, gs_file):
        with open(gs_file) as f:
            gs = json.load(f)
            gs = gs['date_annotations']
        with open(sys_file) as f:
            sys = json.load(f)
            sys = sys['date_annotations']
        self.sys_dict_seq = self.json_dict_seq(sys)
        self.gs_dict_seq = self.json_dict_seq(gs)
        # print(self.sys_dict_seq)
        self.sys_dict_token = self.json_dict_token(sys)
        self.gs_dict_token = self.json_dict_token(gs)
        print(self.sys_dict_token)

    # load the json file and convert it to a untokenised dictionary
    # with key 'noteId-start-length'
    # with value ["text"(untokened),"dateFormat"]
    def json_dict_seq(self, input):
        json_dict = {}
        for anno in input:
            noteId = anno['noteId']
            start = anno['start']
            data_loc = '{}-{}'.format(noteId, start)
            text = anno['text']
            length = anno['length']
            dateFormat = anno['dateFormat']
            date_list = [text, dateFormat, length]
            json_dict[data_loc] = date_list
        return json_dict

    # load the json file and convert it to a untokenised dictionary
    # with key 'noteId-start-length'
    # with value ["text"(untokened),"dateFormat","length"]

    def json_dict_token(self, input):
        json_dict = {}
        for anno in input:
            noteId = anno['noteId']
            start = anno['start']
            text = anno['text']
            dateFormat = anno['dateFormat']
            sub_text = re.split(r'\s+', text)
            for sub in sub_text:
                leng = len(sub)
                data_loc = '{}-{}-{}'.format(noteId, start, leng)
                start = start + leng + 1
                # [text, dateFormat,length]
                date_list = [sub, dateFormat, leng]
                json_dict[data_loc] = date_list
        return json_dict

    def eval(self):
        self.eval_category_instance()
        self.eval_category_token()
        final_date_eval = dict()
        final_date_eval["date_location"] = self.date_loc_list
        final_date_eval["date_type"] = self.date_type_list
        print(final_date_eval)
        # expected json object for date
        # date_loc={
        #       "metric": “F1”/“precision”/“recall”,
        #       "value" (double): 0.89,
        #       "type":  “instance”/“token”
        #       "mode": “strict”/“relax”
        #       }
        # date_format={
        #       "metric": “F1”/“precision”/“recall”,
        #       "value" (double): 0.89
        #       }

        # output json file
        '''
        json_object = json.dumps(final_date_eval, indent = 4)
        with open("eval.json", "w") as outfile:
            outfile.write(json_object)
        '''
        # calculate true positive

        # instance based_eval
    # strict: length match, relax: length match +/- 2
    def eval_category_instance(self):
        sys_dict = self.sys_dict_seq
        gs_dict = self.gs_dict_seq
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.relax_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.relax_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "instance", "relax")
        # strict
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.strict_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if (key not in sys_dict.keys())\
                    or (key in sys_dict.keys() and not self.strict_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "instance", "strict")
        # data format, instance
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.date_format_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.date_format_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "date_format", "strict")

    def relax_cond(self, key, sys_dict, gs_dict):
        return abs(sys_dict[key][2]-gs_dict[key][2]) <= 2

    def strict_cond(self, key, sys_dict, gs_dict):
        return abs(sys_dict[key][2]-gs_dict[key][2]) == 0

    def date_format_cond(self, key, sys_dict, gs_dict):
        return (sys_dict[key][1] == gs_dict[key][1]) and abs(sys_dict[key][2] - gs_dict[key][2]) == 0

    def eval_category_token(self):
        # relax
        sys_dict = self.sys_dict_token
        gs_dict = self.gs_dict_token
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.strict_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.strict_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "token", "strict")

    def print_out(self, tp, fp, fn, type_up, type_lower):
        # precision (P): TP / (TP + FP)
        # Recall (R): TP / (TP + FN)
        # F1 score: 2 * ((P * R) / (P + R))
        precision = round(tp / (tp + fp), 2)
        recall = round(tp / (tp + fn), 2)
        F1 = round(2 * ((precision * recall) / (precision + recall)), 2)
        # print("F1 {}".format(F1))
        # print(type_up,type_lower)
        # print("tp: {},fp: {},fn: {}".format(tp,fp,fn))
        str_fmt = "{:<25}{:<15}{:<15}{:<20}"

        print(str_fmt.format(type_up, "F1", "Precision", "Recall"))

        print("{:-<25}{:-<15}{:-<15}{:-<20}".format("", "", "", ""))

        print(str_fmt.format(type_lower, F1,
                             precision,
                             recall))

        print("\n")
        eval_dict = {"F1": F1, "precision": precision, "recall": recall}
        date_loc = dict()
        date_type = dict()
        if type_up != 'date_format':
            for key in eval_dict.keys():
                date_loc = {"metric": key,
                            "value": eval_dict[key],
                            "type": type_up,
                            "mode": type_lower}
                self.date_loc_list.append(date_loc)
        else:
            for key in eval_dict.keys():
                date_type = {"metric": key,
                             "value": eval_dict[key]}
                self.date_type_list.append(date_type)


class NameEvaluation(object):
    # The evaluation of a prediction file.
    def __init__(self):
        self.gs_dict_seq = dict()
        self.sys_dict_seq = dict()
        self.gs_dict_token = dict()
        self.sys_dict_token = dict()
        self.person_loc_list = list()
        self.person_type_list = list()
    # load the json file and convert it to a dictionary with key

    def convert_dict(self, sys_file, gs_file):
        with open(gs_file) as f:
            gs = json.load(f)
            gs = gs['person_name_annotations']
        with open(sys_file) as f:
            sys = json.load(f)
            sys = sys['person_name_annotations']
        self.sys_dict_seq = self.json_dict_seq(sys)
        self.gs_dict_seq = self.json_dict_seq(gs)
        # print(self.sys_dict_seq)
        self.sys_dict_token = self.json_dict_token(sys)
        self.gs_dict_token = self.json_dict_token(gs)
        print(self.sys_dict_token)

    # load the json file and convert it to a untokenised dictionary
    # with key 'noteId-start-length'
    def json_dict_seq(self, input):
        json_dict = {}
        for anno in input:
            noteId = anno['noteId']
            start = anno['start']
            data_loc = '{}-{}'.format(noteId, start)
            text = anno['text']
            length = anno['length']
            person_type = anno['person_type']
            person_list = [text, person_type, length]
            json_dict[data_loc] = person_list
        return json_dict

    # load the json file and convert it to a untokenised dictionary
    # with key 'noteId-start-length'
    # with value ["text"(untokened),"persontype","length"]

    def json_dict_token(self, input):
        json_dict = {}
        for anno in input:
            noteId = anno['noteId']
            start = anno['start']
            text = anno['text']
            person_type = anno['person_type']
            sub_text = re.split(r'\s+', text)
            for sub in sub_text:
                leng = len(sub)
                data_loc = '{}-{}-{}'.format(noteId, start, leng)
                start = start + leng + 1
                # [text, persontype,length]
                person_list = [sub, person_type, leng]
                json_dict[data_loc] = person_list
        return json_dict

    def eval(self):
        self.eval_category_instance()
        self.eval_category_token()
        final_person_eval = dict()
        final_person_eval["person_location"] = self.person_loc_list
        final_person_eval["person_type"] = self.person_type_list
        print(final_person_eval)
        # expected json object for date
        # person_loc={
        #       "metric": “F1”/“precision”/“recall”,
        #       "value" (double): 0.89,
        #       "type":  “instance”/“token”
        #       "mode": “strict”/“relax”
        #       }
        # person_type={
        #       "metric": “F1”/“precision”/“recall”,
        #       "value" (double): 0.89
        #       }

        # output json file
        '''
        json_object = json.dumps(final_person_eval, indent = 4)
        with open("eval.json", "w") as outfile:
            outfile.write(json_object)
        '''
        # calculate true positive

        # instance based_eval
    # strict: length match, relax: length match +/- 2
    def eval_category_instance(self):
        sys_dict = self.sys_dict_seq
        gs_dict = self.gs_dict_seq
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.relax_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.relax_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "instance", "relax")
        # strict
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.strict_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if (key not in sys_dict.keys())\
                    or (key in sys_dict.keys() and not self.strict_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "instance", "strict")
        # data format, instance
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.person_type_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.person_type_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "person_type", "strict")

    def relax_cond(self, key, sys_dict, gs_dict):
        return abs(sys_dict[key][2]-gs_dict[key][2]) <= 2

    def strict_cond(self, key, sys_dict, gs_dict):
        return abs(sys_dict[key][2]-gs_dict[key][2]) == 0

    def person_type_cond(self, key, sys_dict, gs_dict):
        return (sys_dict[key][1] == gs_dict[key][1]) and abs(sys_dict[key][2] - gs_dict[key][2]) == 0

    def eval_category_token(self):
        # relax
        sys_dict = self.sys_dict_token
        gs_dict = self.gs_dict_token
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.strict_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.strict_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "token", "strict")

    def print_out(self, tp, fp, fn, type_up, type_lower):
        # precision (P): TP / (TP + FP)
        # Recall (R): TP / (TP + FN)
        # F1 score: 2 * ((P * R) / (P + R))
        precision = round(tp / (tp + fp), 2)
        recall = round(tp / (tp + fn), 2)
        F1 = round(2 * ((precision * recall) / (precision + recall)), 2)
        # print("F1 {}".format(F1))
        # print(type_up,type_lower)
        # print("tp: {},fp: {},fn: {}".format(tp,fp,fn))
        str_fmt = "{:<25}{:<15}{:<15}{:<20}"

        print(str_fmt.format(type_up, "F1", "Precision", "Recall"))

        print("{:-<25}{:-<15}{:-<15}{:-<20}".format("", "", "", ""))

        print(str_fmt.format(type_lower, F1,
                             precision,
                             recall))

        print("\n")
        eval_dict = {"F1": F1, "precision": precision, "recall": recall}
        person_loc = dict()
        person_type = dict()
        if type_up != 'person_type':
            for key in eval_dict.keys():
                person_loc = {"metric": key,
                              "value": eval_dict[key],
                              "type": type_up,
                              "mode": type_lower}
                self.person_loc_list.append(person_loc)
        else:
            for key in eval_dict.keys():
                person_type = {"metric": key,
                               "value": eval_dict[key]}
                self.person_type_list.append(person_type)


class AddressEvaluation(object):
    # The evaluation of a prediction file.
    def __init__(self):
        self.gs_dict_seq = dict()
        self.sys_dict_seq = dict()
        self.gs_dict_token = dict()
        self.sys_dict_token = dict()
        self.address_loc_list = list()
        self.address_type_list = list()
    # load the json file and convert it to a dictionary with key

    def convert_dict(self, sys_file, gs_file):
        with open(gs_file) as f:
            gs = json.load(f)
            gs = gs['physical_location_annotations']
        with open(sys_file) as f:
            sys = json.load(f)
            sys = sys['physical_location_annotations']
        self.sys_dict_seq = self.json_dict_seq(sys)
        self.gs_dict_seq = self.json_dict_seq(gs)
        # print(self.sys_dict_seq)
        self.sys_dict_token = self.json_dict_token(sys)
        self.gs_dict_token = self.json_dict_token(gs)
        print(self.sys_dict_token)

    # load the json file and convert it to a untokenised dictionary
    # with key 'noteId-start-length'
    def json_dict_seq(self, input):
        json_dict = {}
        for anno in input:
            noteId = anno['noteId']
            start = anno['start']
            data_loc = '{}-{}'.format(noteId, start)
            text = anno['text']
            length = anno['length']
            address_type = anno['address_type']
            address_list = [text, address_type, length]
            json_dict[data_loc] = address_list
        return json_dict

    # load the json file and convert it to a untokenised dictionary
    # with key 'noteId-start-length'
    # with value ["text"(untokened),"addresstype","length"]

    def json_dict_token(self, input):
        json_dict = {}
        for anno in input:
            noteId = anno['noteId']
            start = anno['start']
            text = anno['text']
            address_type = anno['address_type']
            sub_text = re.split(r'\s+', text)
            for sub in sub_text:
                leng = len(sub)
                data_loc = '{}-{}-{}'.format(noteId, start, leng)
                start = start + leng + 1
                # [text, addresstype,length]
                address_list = [sub, address_type, leng]
                json_dict[data_loc] = address_list
        return json_dict

    def eval(self):
        self.eval_category_instance()
        self.eval_category_token()
        final_address_eval = dict()
        final_address_eval["address_location"] = self.address_loc_list
        final_address_eval["address_type"] = self.address_type_list
        print(final_address_eval)
        # expected json object for date
        # address_loc={
        #       "metric": “F1”/“precision”/“recall”,
        #       "value" (double): 0.89,
        #       "type":  “instance”/“token”
        #       "mode": “strict”/“relax”
        #       }
        # address_type={
        #       "metric": “F1”/“precision”/“recall”,
        #       "value" (double): 0.89
        #       }

        # output json file
        '''
        json_object = json.dumps(final_address_eval, indent = 4)
        with open("eval.json", "w") as outfile:
            outfile.write(json_object)
        '''
        # calculate true positive

        # instance based_eval
    # strict: length match, relax: length match +/- 2
    def eval_category_instance(self):
        sys_dict = self.sys_dict_seq
        gs_dict = self.gs_dict_seq
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.relax_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.relax_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "instance", "relax")
        # strict
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.strict_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if (key not in sys_dict.keys())\
                    or (key in sys_dict.keys() and not self.strict_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "instance", "strict")
        # data format, instance
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.address_type_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.address_type_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "address_type", "strict")

    def relax_cond(self, key, sys_dict, gs_dict):
        return abs(sys_dict[key][2]-gs_dict[key][2]) <= 2

    def strict_cond(self, key, sys_dict, gs_dict):
        return abs(sys_dict[key][2]-gs_dict[key][2]) == 0

    def address_type_cond(self, key, sys_dict, gs_dict):
        return (sys_dict[key][1] == gs_dict[key][1]) and abs(sys_dict[key][2] - gs_dict[key][2]) == 0

    def eval_category_token(self):
        # relax
        sys_dict = self.sys_dict_token
        gs_dict = self.gs_dict_token
        tp = 0
        fp = 0
        fn = 0
        for key in sys_dict.keys():
            if key in gs_dict.keys() and self.strict_cond(key, sys_dict, gs_dict):
                tp = tp + 1
            else:
                fp = fp + 1
        for key in gs_dict.keys():
            if key not in sys_dict.keys() or \
                    (key in sys_dict.keys() and not self.strict_cond(key, sys_dict, gs_dict)):
                fn = fn + 1
        self.print_out(tp, fp, fn, "token", "strict")

    def print_out(self, tp, fp, fn, type_up, type_lower):
        # precision (P): TP / (TP + FP)
        # Recall (R): TP / (TP + FN)
        # F1 score: 2 * ((P * R) / (P + R))
        precision = round(tp / (tp + fp), 2)
        recall = round(tp / (tp + fn), 2)
        F1 = round(2 * ((precision * recall) / (precision + recall)), 2)
        # print("F1 {}".format(F1))
        # print(type_up,type_lower)
        # print("tp: {},fp: {},fn: {}".format(tp, fp, fn))
        str_fmt = "{:<25}{:<15}{:<15}{:<20}"

        print(str_fmt.format(type_up, "F1", "Precision", "Recall"))

        print("{:-<25}{:-<15}{:-<15}{:-<20}".format("", "", "", ""))

        print(str_fmt.format(type_lower, F1,
                             precision,
                             recall))

        print("\n")
        eval_dict = {"F1": F1, "precision": precision, "recall": recall}
        address_loc = dict()
        address_type = dict()
        if type_up != 'address_type':
            for key in eval_dict.keys():
                address_loc = {"metric": key,
                               "value": eval_dict[key],
                               "type": type_up,
                               "mode": type_lower}
                self.address_loc_list.append(address_loc)
        else:
            for key in eval_dict.keys():
                address_type = {"metric": key,
                                "value": eval_dict[key]}
                self.address_type_list.append(address_type)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='import input and goldstandard for comparison')
    parser.add_argument('--input', help='add input files')
    parser.add_argument('--gs', help='add goldstandard files')
    args = parser.parse_args()
    # Running the date eval module
    de = DateEvaluation()
    de.convert_dict(args.input, args.gs)
    de.eval()
    # Running the person name eval module
    pe = NameEvaluation()
    pe.convert_dict(args.input, args.gs)
    pe.eval()
    # Running the address eval module
    ae = AddressEvaluation()
    ae.convert_dict(args.input, args.gs)
    ae.eval()
