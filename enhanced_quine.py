#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import sys

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def run_quine():
    config = load_config()
    lang = config.get('language', 'en')
    
    # Core Quine Logic
    s='s=%r;print(s%%s)';print(s%s)
    
    if lang == 'zh':
        # This print would technically break the "strict" Quine property 
        # unless it's part of the quine string itself.
        # Ideally, a configurable Quine would inject the config into the source string.
        pass

if __name__ == "__main__":
    run_quine()
