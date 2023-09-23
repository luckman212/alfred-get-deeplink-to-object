#!/usr/bin/env python3

"""
constructs a URI to the currently selected Alfred workflow object
https://www.alfredforum.com/topic/18390-get-currently-edited-workflow-uri/
"""

import os
import sys
import json
import subprocess

WF_URI_BASE = 'alfredpreferences://navigateto/workflows>workflow'

"""disabled to remove dependency on pyobjc
sys.path.insert(0, './lib')

try:
    from AppKit import NSPasteboard
except ModuleNotFoundError:
    print('pyobjc_missing', end='')
    exit(1)

def read_wf_config_from_pasteboard():
    wf_config = None
    pasteboard = NSPasteboard.generalPasteboard()
    items = pasteboard.pasteboardItems()
    #print(f'pb has {len(items)} items')
    for item in items:
        for itype in item.types():
            #print(f'type: {itype}')
            if itype == 'com.runningwithcrayons.alfred.workflow.editor.prefab':
                wf_config = item.stringForType_(itype)
    return wf_config
"""

def exit_with_error():
    print('Error: copy a workflow object (configuration) to the pasteboard first.')
    exit(1)

def read_wf_config_from_pasteboard():
    try:
        output = subprocess.check_output(['./read_wfobj_from_pasteboard']).decode()
        assert len(output)
    except:
        return None
    return output

def read_last_wf_uid():
    history_path = os.path.expanduser("~/Library/Application Support/Alfred/history.json")
    try:
        with open(history_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading or parsing Alfred's workflow history file: {e}")
        exit(2)
    value = data.get('preferences', {}).get('workflows', [None])[0]
    return value

if __name__ == "__main__":
    WF_CONFIG = read_wf_config_from_pasteboard()
    if not WF_CONFIG:
        exit_with_error()
    else:
        WF_CONFIG_JSON = json.loads(WF_CONFIG)
        SELECTED_OBJECT_UID = WF_CONFIG_JSON["data"]["items"][0]["uid"]
    WF_UID = read_last_wf_uid()
    if WF_UID:
        print(f'{WF_URI_BASE}>{WF_UID}>{SELECTED_OBJECT_UID}')
        exit(0)
    else:
        exit_with_error()
