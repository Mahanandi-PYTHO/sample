class OnResourceNotFoundException(Exception):
    """
    Raise exception on resource not found
    """
    def __init__(self, message, code):
        self.status = 404
        self.payload = ({'hint' : 'Resource DoesNot Exists'})
        self.message = message
        self.app_code = code
        super(OnResourceNotFoundException, self).__init__()

class OnInvalidRequestDataException(Exception):
    """
    Raise exception on resource not found
    """
    def __init__(self, message, code):
        self.status = 400
        self.payload = ({'hint' : 'Invalid Request Data Provided'})
        self.message = message
        self.app_code = code
        super(OnInvalidRequestDataException, self).__init__()

class OnDBTransactionFailedException(Exception):
    """
    Raise exception on db transaction failed
    """
    def __init__(self, message, code):
        self.status = 400
        self.payload = ({'hint' : 'Record Failed To Store'})
        self.message = message
        self.app_code = code
        super(OnDBTransactionFailedException, self).__init__()

class OnAuthenticationFailedException(Exception):
    """
    Raise exception on resource not found
    """
    def __init__(self, message, code):
        self.status = 401
        self.payload = ({'hint' : 'Request Unauthorised'})
        self.message = message
        self.app_code = code
        super(OnAuthenticationFailedException, self).__init__()