import pickle

def save_object(obj, filename):
    """[save an object as .pickle file]

    Args:
        obj (obj): [object to save]
        filename ([str]): [filename]
    """
    st = open(filename, "wb")
    pickle.dump(obj, st)
    st.close()

def load_object(filename):
    """[load an object from .pickle file]

    Args:
        filename ([str]): [file where load the object]

    Returns:
        [obj]: [obj loaded by the file]
    """
    st = open(filename,"rb")
    obj = pickle.load(st)
    st.close()
    return obj