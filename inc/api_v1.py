import os
import logging
import apie

class v1(apie.Endpoint):
    def __init__(this, name="Eons Infrastructure Technologies API version 1"):
        super().__init__(name)

        # We will not use the request, only the apie config (or a predecessor)
        this.fetchFromRequest = []

        this.static = True

        this.allowedNext.append('package')
        this.staticKWArgs.append('package_package_authenticator')
        this.staticKWArgs.append('package_upload_url')
        this.staticKWArgs.append('package_upload_map')
        # upload_files is not static. downstream 'files' arg will grab.
        this.staticKWArgs.append('package_download_url')
        this.staticKWArgs.append('package_download_map')
        this.staticKWArgs.append('package_download_secondary_field')
        this.staticKWArgs.append('package_delete_url')
        this.staticKWArgs.append('package_delete_map')
        this.staticKWArgs.append('package_list_url')
        this.staticKWArgs.append('package_list_map')

        this.helpText = '''\
Version 1 of the EIT API.
For more info, check out the allowed next Endpoints; each is a different resource which you can manage through this.
'''

    def Call(this):
        # All we need to do right now is grab args from the config.
        pass