import os  # Import the os module for interacting with the operating system
from box.exceptions import BoxValueError  # Import BoxValueError from box.exceptions module
import yaml  # Import the yaml module for YAML parsing
from cnnClassifier import logger  # Import logger from cnnClassifier module
import json  # Import the json module for JSON serialization and deserialization
import joblib  # Import the joblib module for saving and loading binary files
from ensure import ensure_annotations  # Import ensure_annotations from ensure module
from box import ConfigBox  # Import ConfigBox from box module
from pathlib import Path  # Import Path class from pathlib module
from typing import Any  # Import Any from typing module for type hinting
import base64  # Import base64 module for base64 encoding and decoding

# Define a function to read YAML files and return a ConfigBox object
@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: config box type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e
    
# Define a function to create directories
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories is to be created
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at:{path}")
            

# Define a function to save data to a JSON file
@ensure_annotations
def save_json(path:Path, data:dict):
    """
    save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to save in json file
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        
        logger.info(f"json file:{path} saved successfully")
        
# Define a function to load data from a JSON file      
@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    """load json file data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dicts
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded successfully from:{path}")
        return ConfigBox(content)
    
# Define a function to save binary data to a file
@ensure_annotations
def save_bin(data:Any, path:Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary file
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved successfully ats: {path}")

# Define a function to load binary data from a file  
@ensure_annotations
def load_bin(path:Path)-> Any:
    """load binary file

    Args:
        path (Path): path to binary file

    Returns:
        Any: data loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from:{path}")
    return data

# Define a function to get the size of a file in KB
@ensure_annotations
def get_size(path:Path):
    """get size in KB

    Args:
        path (Path): path of the file
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

# Define a function to decode a base64-encoded image and save it to a file
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


# Define a function to encode an image into base64 format
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())