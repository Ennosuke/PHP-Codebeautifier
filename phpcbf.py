import sublime, sublime_plugin, subprocess, os

class Pref:

    project_file = None

    keys = [
        "path",
        "level",
        "encoding",
        "on_save",
        "on_load",
        "syntaxes",
        "suffix",
        "sniffs",
        "tab_width"
    ]

    def load(self):
        self.settings = sublime.load_settings('phpcbf.sublime-settings')

        if sublime.active_window() is not None and sublime.active_window().active_view() is not None:
            project_settings = sublime.active_window().active_view().settings()
            if project_settings.has("phpcbf"):
                project_settings.clear_on_change('phpcbf')
                self.project_settings = project_settings.get('phpcbf')
                project_settings.add_on_change('phpcbf', pref.load)
            else:
                self.project_settings = {}
        else:
            self.project_settings = {}

        for key in self.keys:
            self.settings.clear_on_change(key)
            setattr(self, key, self.get_setting(key))
            self.settings.add_on_change(key, pref.load)

    def get_setting(self, key):
        if key in self.project_settings:
            return self.project_settings.get(key)
        else:
            return self.settings.get(key)

    def set_setting(self, key, value):
        if key in self.project_settings:
            self.project_settings[key] = value
        else:
            self.settings.set(key, value)

pref = Pref()

def plugin_loaded():
    pref.load()


class PhpCbfCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        syntaxes = pref.syntaxes
        cur_syntax = self.view.settings().get('syntax')
        if cur_syntax not in syntaxes:
            return
        path = pref.path
        level = pref.level
        suffix = pref.suffix
        sniffs = pref.sniffs
        tab_width = pref.tab_width
        encoding = self.view.encoding()
        if encoding == 'Undefined':
            encoding = pref.encoding
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
            call = path+" "+suffix+sniff_string+tab_width+' --standard='+level+" --encoding="+encoding+" "+file_name
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
        if(pref.on_save):
            view.run_command('php_cbf')
    def on_load(self, view):
        if(pref.on_load):
            view.run_command('php_cbf')




        




