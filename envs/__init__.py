import os

def env(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.getenv(key, default)
    true_vals = ('True','true',1,'1')
    false_vals = ('False','false',0,'0')
    if val in true_vals:
        val = True
    elif val in false_vals:
        val = False
    return val
 
