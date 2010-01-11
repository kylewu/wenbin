import py2exe,  distutils
distutils.core.setup(
                    windows = [
                               {"script": "main.py", 
                               "icon_resources": [(1, "icon.ico")]
                               }
                               ], 
					options={"py2exe":{"includes":["sip"]}},
                    )
