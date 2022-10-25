import os
import logging
import apie

class v1(apie.Endpoint):
    def __init__(this, name="Eons Infrastructure Technologies API version 1"):
        super().__init__(name)

        # We will not use the request, only the apie config (or a predecessor)
        this.fetchFromRequest = []

        this.static = True

        this.staticKWArgs.append('resources')

    # Required Endpoint method. See that class for details.
    def GetHelpText(this):
        return '''\
Version 1 of the EIT API.
This Endpoint utilizes APIE's Resource Paradigm in order to give you access to the resources listed in allowed_next.
'''

    def ValidateStaticArgs(this):
        if (this.staticArgsValid):
            return
        
        super().ValidateStaticArgs()
        
        this.allowedNext = this.resources.keys()

        # Constructing a class for each resource allows us to cache the operations and any other configuration we'd like in memory.
        # This should be faster than reconfiguring a single resource object for each request.
        for resource in this.allowedNext:
            classStr = f'''\
from api_resource import resource
class {resource}(resource):
    def __init__(this, name="{resource}"):
        super().__init__(name)

        this.operations = {this.resources[resource]}
'''
            logging.debug(f"Defining resource:\n{classStr}")
            code = compile(classStr, '', 'exec')
            exec(code)

    def Call(this):
        # All we need to do right now is grab args from the config.
        pass