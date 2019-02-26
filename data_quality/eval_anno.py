# -*- coding: utf-8 -*-

import json
import sys

from dee_metric import measure_event_table_filling
from event_type import event_type_fields_list

def load_json(json_file_path, encoding='utf-8', **kwargs):
    with open(json_file_path, 'r', encoding=encoding) as fin:
        tmp_json = json.load(fin, **kwargs)
    return tmp_json


if __name__ == '__main__':
    if not sys.version.startswith('3'):
        raise Exception('This program only supports python 3, and we only test it with python 3.6')

    doc_anno_list = load_json('./anno_100doc.json')
    ds_record_mat_list = []
    gold_record_mat_list = []
    for doc_anno_obj in doc_anno_list:
        ds_record_mat_list.append(doc_anno_obj['DSEvents'])  # event tables produced by distant supervision
        gold_record_mat_list.append(doc_anno_obj['GoldEvents'])  # event tables annotated by human

    g_metric, _, _ = measure_event_table_filling(ds_record_mat_list, gold_record_mat_list, event_type_fields_list)
    print('Quality of DS Labels: Precision {:.1f} Recall {:.1f} F1 {:.1f}'.format(*[s*100 for s in g_metric]))
