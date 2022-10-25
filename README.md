# Eons Infrastructure Technologies Application Program Interface Version 1

This version of the EIT API utilizes [APIE's Resource Paradigm](https://github.com/eons-dev/bin_apie/#resource-paradigm) in order to give you access to the resources offered by Eons Infrastructure Technologies.

You are welcome to use this apie Endpoint for your own api. Simply specify the resources you would like to use and the available operations for each in your apie.json. Also be sure to use the proper Authenticator to restrict access to your resources.

Here's an example resource configuration:
```json
"resources": {
	"package": {
		"list": "list_implementation_external",
		"upload": "upload_implementation_external",
		"download": "download_implementation_external",
		"delete": "delete_implementation_external"
	}
}
```