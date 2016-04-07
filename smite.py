__version__ = '1.0'
__author__  = 'Chris-The-Tuner'
 
import b3
import b3.events
import b3.plugin
import urllib2

class SmitePlugin(b3.plugin.Plugin):
    requiresConfigFile = False

    def startup(self):
        # get the admin plugin so we can register commands
        self._adminPlugin = self.console.getPlugin('admin')
        if not self._adminPlugin:
            # something is wrong, can't start without admin plugin
            self.error('Could not find admin plugin')
            return False
 
        # Register commands
        self._adminPlugin.registerCommand(self, 'smite', 20, self.cmd_smite)
        
    def cmd_smite(self, data, client=None, cmd=None):
        input = self._adminPlugin.parseUserCmd(data)
        if not data:
            client.message('^7 correct syntax is !smite <playername or partialname>')
            return False
        else:
            if  len([x for x in data if x.isspace()]) < 0:
                client.message('^7 correct syntax is !smite <playername or partialname>')
            else:
                input = data.split(' ',1)
                scname = input[0]
             	sclient = self._adminPlugin.findClientPrompt(scname, client)
                if not sclient: return False
                client.message("I'm smiting !")
                self.console.write("smite %s" % (sclient.cid))
        return True
