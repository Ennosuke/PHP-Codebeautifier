import sublime, sublime_plugin, subprocess, os

class PhpCbfCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        settings = sublime.load_settings("phpcbf.sublime-settings")
        syntaxes = settings.get('syntaxes')
        cur_syntax = self.view.settings().get('syntax')
        if cur_syntax not in syntaxes:
            return
        path = settings.get('path', "")
        level = settings.get('level', 'psr2')
        patch = settings.get('patch', False)
        suffix = settings.get('suffix', '')
        sniffs = settings.get('sniffs', '')
        tab_width = settings.get('tab_width', False)
        if not patch:
            patch = "--no-patch"
        else:
            patch = ""
        encoding = self.view.encoding()
        if encoding == 'Undefined':
            encoding = settings.get('encoding', 'UTF-8')
        if not path:
            path = "phpcbf"
        if suffix:
            suffix = ' --suffix='+suffix
        sniff_string = ''
        if sniffs:
            sniff_string = ' --sniffs='
            for sniff in sniffs:
                sniff_string += sniff+','
            sniff_string.rtrim(',')
        if tab_width:
            tab_width = ' --tab_width='+tab_width
        file_name = self.view.file_name()
        if file_name:
            call = path+" "+patch+suffix+sniff_string+tab_width+' --standard='+level+" --encoding="+encoding+" "+file_name
            try:
                output = subprocess.check_output(call, shell=True,universal_newlines=True)
            except subprocess.CalledProcessError as e:
                print(e.output)
                sublime.status_message("An error occured while fixing, please check the console")
            else:
                sublime.status_message("All fixable errors have been fixed")
        else:
            sublime.status_message("Please save the file first")
class PhpCbfListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        settings = sublime.load_settings("phpcbf.sublime-settings")
        if(settings.get('on_save', True)):
            view.run_command('php_cbf')
    def on_load(self, view):
        settings = sublime.load_settings("phpcbf.sublime-settings")
        if(settings.get('on_load', True)):
            view.run_command('php_cbf')




        




