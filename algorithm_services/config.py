import os.path

# configs
debug = True
templates_auto_reload = True
explain_template_loading = False
template_folder = './algorithm_services/templates'

config = {
    "DEBUG": debug,
    "TEMPLATES_AUTO_RELOAD": templates_auto_reload,
    "EXPLAIN_TEMPLATE_LOADING": explain_template_loading,
    "TEMPLATE_FOLDER": os.path.abspath(template_folder)
}
